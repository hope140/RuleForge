from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
import ipaddress
from pathlib import Path

from .audit import Conflict, ConflictDecision, ResolutionResult
from .model import Rule
from .routing import rule_sort_key
from .runtime import RouteProbe, order_rules_for_first_match, rule_matches, simulate_route


_DOMAIN_RULE_TYPES = {"HOST", "HOST-SUFFIX", "HOST-KEYWORD", "HOST-WILDCARD"}
_NETWORK_RULE_TYPES = {"IP-CIDR", "IP6-CIDR"}
_AUTO_SPECIFIC_TYPES = {"HOST", "HOST-SUFFIX", "IP-CIDR", "IP6-CIDR"}
_CONFIDENCE_RANK = {"low": 0, "medium": 1, "high": 2}
_APPLE_POLICY = "苹果服务"
_APPLE_SERVICE_SUFFIXES = ("apple.com", "icloud.com", "mzstatic.com")
_APPLE_SERVICE_HOSTS = {
    "apple-relay.cloudflare.com",
    "apple-relay.fastly-edge.com",
    "cp4.cloudflare.com",
}


def _rule_ref(rule: Rule | None) -> dict[str, object] | None:
    if rule is None:
        return None
    return {
        "source_id": rule.source_id,
        "category": rule.category,
        "policy": rule.policy,
        "rule_type": rule.rule_type,
        "value": rule.value,
        "line_number": rule.line_number,
    }


def _probe_ref(probe: RouteProbe | None) -> dict[str, object] | None:
    if probe is None:
        return None
    return {
        "domain": probe.domain,
        "ip": probe.ip,
        "process": probe.process,
        "destination_port": probe.destination_port,
        "inbound_port": probe.inbound_port,
    }


def _network(rule: Rule) -> ipaddress.IPv4Network | ipaddress.IPv6Network | None:
    if rule.rule_type not in _NETWORK_RULE_TYPES:
        return None
    try:
        return ipaddress.ip_network(rule.value, strict=False)
    except ValueError:
        return None


def _wildcard_example(pattern: str) -> str:
    result = pattern.replace("*", "probe").replace("?", "a")
    return result.lstrip(".") or "probe.example"


def _domain_probe(conflict: Conflict) -> RouteProbe | None:
    candidates: list[str] = []
    for rule in (conflict.left, conflict.right):
        if rule.rule_type == "HOST":
            candidates.append(rule.value)
        elif rule.rule_type == "HOST-SUFFIX":
            candidates.extend((rule.value, "probe." + rule.value))
        elif rule.rule_type == "HOST-WILDCARD":
            candidates.append(_wildcard_example(rule.value))

    keywords = [
        rule.value
        for rule in (conflict.left, conflict.right)
        if rule.rule_type == "HOST-KEYWORD"
    ]
    if keywords:
        candidates.append("probe-" + "-".join(keywords) + ".example")

    for candidate in dict.fromkeys(candidates):
        probe = RouteProbe(domain=candidate)
        if rule_matches(conflict.left, probe) and rule_matches(conflict.right, probe):
            return probe
    return None


def _network_probe(conflict: Conflict) -> RouteProbe | None:
    left = _network(conflict.left)
    right = _network(conflict.right)
    if left is None or right is None or left.version != right.version or not left.overlaps(right):
        return None
    narrower = left if left.prefixlen >= right.prefixlen else right
    probe = RouteProbe(ip=str(narrower.network_address))
    if rule_matches(conflict.left, probe) and rule_matches(conflict.right, probe):
        return probe
    return None


def conflict_probe(conflict: Conflict) -> RouteProbe | None:
    types = {conflict.left.rule_type, conflict.right.rule_type}
    if types <= _DOMAIN_RULE_TYPES:
        return _domain_probe(conflict)
    if types <= _NETWORK_RULE_TYPES:
        return _network_probe(conflict)
    return None


def _is_apple_service_probe(probe: RouteProbe | None) -> bool:
    if probe is None or not probe.domain:
        return False
    domain = probe.domain.casefold().rstrip(".")
    return domain in _APPLE_SERVICE_HOSTS or any(
        domain == suffix or domain.endswith("." + suffix)
        for suffix in _APPLE_SERVICE_SUFFIXES
    )


def _probe_for_rule(rule: Rule) -> RouteProbe | None:
    if rule.rule_type in {"HOST", "HOST-SUFFIX"}:
        return RouteProbe(domain=rule.value)
    if rule.rule_type == "HOST-KEYWORD" and "." in rule.value and "*" not in rule.value:
        return RouteProbe(domain=rule.value)
    return None


def _apple_contract_rule(rule: Rule) -> Rule:
    rule_type = (
        "HOST-SUFFIX"
        if rule.rule_type in {"HOST-SUFFIX", "HOST-KEYWORD"}
        else "HOST"
    )
    return Rule(
        source_id="apple-service-contract",
        source_format="contract",
        category="apple",
        policy=_APPLE_POLICY,
        rule_type=rule_type,
        value=rule.value,
        raw=f"{rule_type},{rule.value}",
    )


def _candidate_covers(covering: Rule, covered: Rule) -> bool:
    if (
        covering == covered
        or covering.policy != covered.policy
        or covering.category != covered.category
        or covering.rule_type != "HOST-SUFFIX"
        or covered.rule_type not in {"HOST", "HOST-SUFFIX"}
    ):
        return False
    probe = RouteProbe(domain=covered.value)
    return rule_matches(covering, probe)


def _is_more_specific_winner(conflict: Conflict, winner: Rule) -> bool:
    loser = conflict.right if winner == conflict.left else conflict.left
    if conflict.relation == "host-inside-host-suffix":
        return winner.rule_type == "HOST" and loser.rule_type == "HOST-SUFFIX"
    if conflict.relation == "nested-host-suffix":
        return (
            winner.rule_type == loser.rule_type == "HOST-SUFFIX"
            and len(winner.value) > len(loser.value)
        )
    if conflict.relation == "host-keyword-overlap":
        if winner.rule_type != loser.rule_type:
            return winner.rule_type != "HOST-KEYWORD"
        return len(winner.value) > len(loser.value)
    if conflict.relation == "host-wildcard-overlap":
        return winner.rule_type != "HOST-WILDCARD" and loser.rule_type == "HOST-WILDCARD"
    if conflict.relation == "ip-cidr-overlap":
        winner_network = _network(winner)
        loser_network = _network(loser)
        return bool(
            winner_network is not None
            and loser_network is not None
            and winner_network != loser_network
            and winner_network.subnet_of(loser_network)
        )
    return False


def _decision_confidence(decision: ConflictDecision) -> tuple[str, str]:
    reason = decision.reason
    if "explicit direct-exception" in reason or "Reject rules take precedence" in reason:
        return "high", "security-contract"
    if "configured business-category priority" in reason:
        return "high", "business-contract"
    if "more specific rule" in reason:
        return "medium", "specificity"
    if "Blackmatrix" in reason:
        return "low", "source-fallback"
    return "low", "category-order-fallback"


def _candidate_eligible(decision: ConflictDecision, confidence: str, method: str) -> bool:
    winner = decision.winner
    loser = decision.loser
    if winner is None or loser is None:
        return False
    if method == "security-contract":
        return True
    if confidence not in {"high", "medium"}:
        return False
    if not _is_more_specific_winner(decision.conflict, winner):
        return False
    return winner.rule_type in _AUTO_SPECIFIC_TYPES


@dataclass(frozen=True)
class PriorityPreviewItem:
    relation: str
    expected_rule: Rule
    compared_rule: Rule
    actual_rule: Rule | None
    probe: RouteProbe | None
    confidence: str
    method: str
    status: str
    disposition_reason: str
    reason: str

    def to_dict(self) -> dict[str, object]:
        return {
            "relation": self.relation,
            "confidence": self.confidence,
            "method": self.method,
            "status": self.status,
            "disposition_reason": self.disposition_reason,
            "reason": self.reason,
            "probe": _probe_ref(self.probe),
            "expected_rule": _rule_ref(self.expected_rule),
            "compared_rule": _rule_ref(self.compared_rule),
            "actual_rule": _rule_ref(self.actual_rule),
            "expected_policy": self.expected_rule.policy,
            "actual_policy": self.actual_rule.policy if self.actual_rule is not None else None,
        }


@dataclass(frozen=True)
class PriorityPreviewResult:
    target: str
    ordered_overlap_count: int
    live_cross_category_count: int
    discarded_overlap_count: int
    apple_contract_gap_count: int
    status_counts: dict[str, int]
    items: tuple[PriorityPreviewItem, ...]
    candidate_rules: tuple[Rule, ...]

    def summary_dict(self) -> dict[str, object]:
        return {
            "mode": "preview-only",
            "active": False,
            "target": self.target,
            "ordered_overlap_count": self.ordered_overlap_count,
            "live_cross_category_count": self.live_cross_category_count,
            "discarded_overlap_count": self.discarded_overlap_count,
            "apple_contract_gap_count": self.apple_contract_gap_count,
            "actual_policy_mismatch_count": (
                self.status_counts.get("preview-candidate", 0)
                + self.status_counts.get("review-required", 0)
            ),
            "preview_candidate_decision_count": self.status_counts.get("preview-candidate", 0),
            "preview_candidate_rule_count": len(self.candidate_rules),
            "review_required_count": self.status_counts.get("review-required", 0),
            "unwitnessed_count": self.status_counts.get("unwitnessed", 0),
            "status_counts": dict(sorted(self.status_counts.items())),
        }

    def to_dict(self) -> dict[str, object]:
        evidence_by_rule: dict[Rule, list[PriorityPreviewItem]] = defaultdict(list)
        for item in self.items:
            if item.status == "preview-candidate":
                evidence_by_rule[item.expected_rule].append(item)
        candidates = []
        for rule in self.candidate_rules:
            evidence = evidence_by_rule[rule]
            confidence = max(
                (item.confidence for item in evidence),
                key=lambda value: _CONFIDENCE_RANK[value],
            )
            rendered = rule.to_mihomo() if self.target == "mihomo" else rule.to_quantumultx()
            witnesses = []
            for item in evidence:
                value = item.probe.domain if item.probe and item.probe.domain else item.probe.ip if item.probe else None
                if value and value not in witnesses:
                    witnesses.append(value)
            candidates.append(
                {
                    "rule": _rule_ref(rule),
                    "rendered_rule": rendered,
                    "confidence": confidence,
                    "evidence_count": len(evidence),
                    "witnesses": witnesses,
                }
            )
        return {
            **self.summary_dict(),
            "override_candidates": candidates,
            "items": [item.to_dict() for item in self.items],
        }


def build_priority_preview(resolution: ResolutionResult, *, target: str) -> PriorityPreviewResult:
    live_rules = frozenset(resolution.rules)
    ordered_rules = order_rules_for_first_match(resolution.rules)
    issue_items: list[PriorityPreviewItem] = []
    statuses: Counter[str] = Counter()
    candidates: set[Rule] = set()
    live_count = 0
    discarded_count = 0
    apple_contract_gap_count = 0
    seen: set[tuple[Rule, Rule, str]] = set()

    for decision in resolution.ordered_overlap_decisions:
        winner = decision.winner
        loser = decision.loser
        if winner is None or loser is None or winner.category == loser.category:
            continue
        key = (winner, loser, decision.conflict.relation)
        if key in seen:
            continue
        seen.add(key)
        if winner not in live_rules or loser not in live_rules:
            discarded_count += 1
            continue
        live_count += 1
        probe = conflict_probe(decision.conflict)
        confidence, method = _decision_confidence(decision)
        actual = simulate_route(ordered_rules, probe) if probe is not None else None
        security_contract = (
            winner.policy.casefold() == "reject"
            or winner.category == "direct-exception"
            or (
                actual is not None
                and (
                    actual.policy.casefold() == "reject"
                    or actual.rule.category == "direct-exception"
                )
            )
        )
        apple_contract = _is_apple_service_probe(probe) and not security_contract
        if apple_contract:
            confidence, method = "high", "apple-service-contract"
        if probe is None:
            status = "unwitnessed"
            disposition_reason = "no-reliable-witness"
        elif actual is None:
            status = "review-required"
            disposition_reason = "no-current-match"
        elif apple_contract and actual.policy == _APPLE_POLICY:
            status = "enforced" if actual.rule == winner else "equivalent-policy"
            disposition_reason = "apple-policy-already-active"
        elif apple_contract and winner.policy != _APPLE_POLICY:
            status = "review-required"
            disposition_reason = "apple-policy-missing"
        elif actual.policy == winner.policy:
            status = "enforced" if actual.rule == winner else "equivalent-policy"
            disposition_reason = "expected-policy-already-active"
        elif actual.rule != loser:
            # A decision about winner/loser is not enough authority to move the
            # winner ahead of an unrelated third rule. A separate direct
            # overlap decision may still propose the same winner safely.
            status = "review-required"
            disposition_reason = "third-rule-interference"
        elif _candidate_eligible(decision, confidence, method):
            status = "preview-candidate"
            disposition_reason = "direct-blocker-candidate"
            candidates.add(winner)
        else:
            status = "review-required"
            disposition_reason = "not-auto-eligible"
        statuses[status] += 1
        if status not in {"enforced", "equivalent-policy"}:
            issue_items.append(
                PriorityPreviewItem(
                    relation=decision.conflict.relation,
                    expected_rule=winner,
                    compared_rule=loser,
                    actual_rule=actual.rule if actual is not None else None,
                    probe=probe,
                    confidence=confidence,
                    method=method,
                    status=status,
                    disposition_reason=disposition_reason,
                    reason=decision.reason,
                )
            )

    existing_apple_candidate_values = {
        item.expected_rule.value
        for item in issue_items
        if item.status == "preview-candidate" and item.expected_rule.policy == _APPLE_POLICY
    }
    seen_apple_gaps: set[tuple[str, str]] = set()
    for rule in resolution.rules:
        if (
            rule.policy in {_APPLE_POLICY, "reject"}
            or rule.category == "direct-exception"
        ):
            continue
        probe = _probe_for_rule(rule)
        if not _is_apple_service_probe(probe):
            continue
        actual = simulate_route(ordered_rules, probe)
        if (
            actual is None
            or actual.policy in {_APPLE_POLICY, "reject"}
            or actual.rule.category == "direct-exception"
            or rule.value in existing_apple_candidate_values
        ):
            continue
        expected = _apple_contract_rule(rule)
        key = (expected.rule_type, expected.value)
        if key in seen_apple_gaps:
            continue
        seen_apple_gaps.add(key)
        apple_contract_gap_count += 1
        statuses["preview-candidate"] += 1
        candidates.add(expected)
        issue_items.append(
            PriorityPreviewItem(
                relation="apple-service-contract",
                expected_rule=expected,
                compared_rule=actual.rule,
                actual_rule=actual.rule,
                probe=probe,
                confidence="high",
                method="apple-service-contract",
                status="preview-candidate",
                disposition_reason="apple-contract-candidate",
                reason="Apple-related traffic is unified under the Apple service policy.",
            )
        )

    issue_items.sort(
        key=lambda item: (
            item.status,
            -_CONFIDENCE_RANK[item.confidence],
            rule_sort_key(item.expected_rule),
            item.relation,
        )
    )
    candidate_rules = tuple(
        sorted(
            (
                candidate
                for candidate in candidates
                if not any(
                    _candidate_covers(other, candidate)
                    for other in candidates
                    if other != candidate
                )
            ),
            key=rule_sort_key,
        )
    )
    return PriorityPreviewResult(
        target=target,
        ordered_overlap_count=len(resolution.ordered_overlap_decisions),
        live_cross_category_count=live_count,
        discarded_overlap_count=discarded_count,
        apple_contract_gap_count=apple_contract_gap_count,
        status_counts=dict(statuses),
        items=tuple(issue_items),
        candidate_rules=candidate_rules,
    )


def render_priority_preview_markdown(result: PriorityPreviewResult, path: str | Path) -> None:
    summary = result.summary_dict()
    lines = [
        "# RuleForge 优先规则预览",
        "",
        "> 仅供审阅，当前模板和正式路由不会引用这些候选规则。",
        "",
        "## 摘要",
        "",
        f"- 目标：`{result.target}`",
        f"- 存活的跨分类重叠：{result.live_cross_category_count}",
        f"- 实际策略不一致：{summary['actual_policy_mismatch_count']}",
        f"- Apple 统一策略缺口：{summary['apple_contract_gap_count']}",
        f"- 可自动生成的候选规则：{len(result.candidate_rules)}",
        f"- 仍需审阅：{summary['review_required_count']}",
        f"- 无法构造验证样例：{summary['unwitnessed_count']}",
        "",
        "## 候选优先规则",
        "",
        "| 规则 | 分类 | 策略 | 可信度 | 证据数 | 验证样例 |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    data = result.to_dict()
    for candidate in data["override_candidates"]:
        rule = candidate["rule"]
        witnesses = "、".join(f"`{value}`" for value in candidate["witnesses"][:3])
        lines.append(
            f"| `{candidate['rendered_rule']}` | `{rule['category']}` | `{rule['policy']}` | "
            f"{candidate['confidence']} | {candidate['evidence_count']} | {witnesses} |"
        )
    if not result.candidate_rules:
        lines.append("| 无 |  |  |  | 0 |  |")

    lines.extend(
        [
            "",
            "## 未自动处理的差异",
            "",
            "| 验证样例 | 预期策略 | 当前策略 | 关系 | 原因 |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    review_items = [item for item in result.items if item.status != "preview-candidate"]
    for item in review_items:
        witness = item.probe.domain if item.probe and item.probe.domain else item.probe.ip if item.probe else "无法生成"
        actual_policy = item.actual_rule.policy if item.actual_rule is not None else "未命中"
        lines.append(
            f"| `{witness}` | `{item.expected_rule.policy}` | `{actual_policy}` | "
            f"`{item.relation}` | {item.disposition_reason} / {item.method} / {item.confidence} |"
        )
    if not review_items:
        lines.append("| 无 |  |  |  |  |")

    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
