from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .model import Rule


@dataclass(frozen=True)
class Duplicate:
    kept: Rule
    dropped: Rule

    def to_dict(self) -> dict[str, object]:
        return {"kept": self.kept.to_dict(), "dropped": self.dropped.to_dict()}


@dataclass(frozen=True)
class Conflict:
    kind: str
    relation: str
    left: Rule
    right: Rule

    def to_dict(self) -> dict[str, object]:
        return {
            "kind": self.kind,
            "relation": self.relation,
            "left": self.left.to_dict(),
            "right": self.right.to_dict(),
        }


@dataclass(frozen=True)
class ConflictDecision:
    conflict: Conflict
    decision: str
    winner: Rule | None = None
    loser: Rule | None = None
    reason: str = ""

    def to_dict(self) -> dict[str, object]:
        def rule_ref(rule: Rule | None) -> dict[str, object] | None:
            if rule is None:
                return None
            return {
                "source_id": rule.source_id,
                "category": rule.category,
                "rule_type": rule.rule_type,
                "value": rule.value,
                "policy": rule.policy,
            }

        return {
            "kind": self.conflict.kind,
            "relation": self.conflict.relation,
            "decision": self.decision,
            "winner": rule_ref(self.winner),
            "loser": rule_ref(self.loser),
            "reason": self.reason,
        }


@dataclass(frozen=True)
class ResolutionResult:
    rules: tuple[Rule, ...]
    decisions: tuple[ConflictDecision, ...]
    rejected_rules: frozenset[Rule]

    @property
    def preferred_decisions(self) -> tuple[ConflictDecision, ...]:
        return tuple(item for item in self.decisions if item.decision != "unresolved")

    @property
    def blackmatrix_decisions(self) -> tuple[ConflictDecision, ...]:
        return tuple(item for item in self.decisions if item.decision == "prefer-blackmatrix")

    @property
    def direct_decisions(self) -> tuple[ConflictDecision, ...]:
        return tuple(item for item in self.decisions if item.decision == "prefer-direct")

    @property
    def specific_decisions(self) -> tuple[ConflictDecision, ...]:
        return tuple(item for item in self.decisions if item.decision == "prefer-specific")

    @property
    def category_decisions(self) -> tuple[ConflictDecision, ...]:
        return tuple(item for item in self.decisions if item.decision == "prefer-category")

    @property
    def unresolved_decisions(self) -> tuple[ConflictDecision, ...]:
        return tuple(item for item in self.decisions if item.decision == "unresolved")

    def to_dict(self) -> dict[str, object]:
        return {
            "resolved_rule_count": len(self.rules),
            "rejected_rule_count": len(self.rejected_rules),
            "resolved_conflict_count": len(self.preferred_decisions),
            "blackmatrix_preferred_conflict_count": len(self.blackmatrix_decisions),
            "direct_preferred_conflict_count": len(self.direct_decisions),
            "specific_preferred_conflict_count": len(self.specific_decisions),
            "category_preferred_conflict_count": len(self.category_decisions),
            "unresolved_conflict_count": len(self.unresolved_decisions),
            "decisions": [item.to_dict() for item in self.decisions],
        }

    def to_summary_dict(self) -> dict[str, int]:
        return {
            "resolved_rule_count": len(self.rules),
            "rejected_rule_count": len(self.rejected_rules),
            "resolved_conflict_count": len(self.preferred_decisions),
            "blackmatrix_preferred_conflict_count": len(self.blackmatrix_decisions),
            "direct_preferred_conflict_count": len(self.direct_decisions),
            "specific_preferred_conflict_count": len(self.specific_decisions),
            "category_preferred_conflict_count": len(self.category_decisions),
            "unresolved_conflict_count": len(self.unresolved_decisions),
        }


@dataclass(frozen=True)
class AuditResult:
    kept_rules: tuple[Rule, ...]
    duplicates: tuple[Duplicate, ...]
    conflicts: tuple[Conflict, ...]

    @property
    def conflicted_rules(self) -> frozenset[Rule]:
        result: set[Rule] = set()
        for conflict in self.conflicts:
            result.add(conflict.left)
            result.add(conflict.right)
        return frozenset(result)

    @property
    def safe_rules(self) -> tuple[Rule, ...]:
        conflicted = self.conflicted_rules
        return tuple(rule for rule in self.kept_rules if rule not in conflicted)

    def to_dict(self) -> dict[str, object]:
        return {
            "kept_rule_count": len(self.kept_rules),
            "safe_rule_count": len(self.safe_rules),
            "conflicted_rule_count": len(self.conflicted_rules),
            "duplicate_count": len(self.duplicates),
            "conflict_count": len(self.conflicts),
            "duplicates": [item.to_dict() for item in self.duplicates],
            "conflicts": [item.to_dict() for item in self.conflicts],
        }


def _parent_domains(value: str) -> Iterable[str]:
    parts = value.split(".")
    for index in range(1, len(parts)):
        yield ".".join(parts[index:])


def audit_rules(rules: Iterable[Rule]) -> AuditResult:
    kept: list[Rule] = []
    duplicates: list[Duplicate] = []
    conflicts: list[Conflict] = []
    exact: dict[tuple[str, str, tuple[str, ...]], Rule] = {}
    for rule in rules:
        previous = exact.get(rule.identity_key)
        if previous is None:
            exact[rule.identity_key] = rule
            kept.append(rule)
            continue
        if previous.policy == rule.policy:
            duplicates.append(Duplicate(previous, rule))
        else:
            conflicts.append(Conflict("exact-policy", "same-rule-different-policy", previous, rule))
            kept.append(rule)

    host_exact: dict[str, list[Rule]] = {}
    host_suffix: dict[str, list[Rule]] = {}
    for rule in kept:
        if rule.rule_type == "HOST":
            host_exact.setdefault(rule.value, []).append(rule)
        elif rule.rule_type == "HOST-SUFFIX":
            host_suffix.setdefault(rule.value, []).append(rule)

    seen_pairs: set[tuple[int, int, str]] = set()

    def add_overlap(left: Rule, right: Rule, relation: str) -> None:
        if left.policy == right.policy:
            return
        pair = (id(left), id(right), relation)
        reverse = (id(right), id(left), relation)
        if pair in seen_pairs or reverse in seen_pairs:
            return
        seen_pairs.add(pair)
        conflicts.append(Conflict("semantic-overlap", relation, left, right))

    for value, exact_rules in host_exact.items():
        for suffix in (value, *_parent_domains(value)):
            for suffix_rule in host_suffix.get(suffix, []):
                for exact_rule in exact_rules:
                    add_overlap(exact_rule, suffix_rule, "host-inside-host-suffix")

    suffix_values = sorted(host_suffix)
    for index, left_value in enumerate(suffix_values):
        for right_value in suffix_values[index + 1 :]:
            if left_value.endswith("." + right_value):
                for left in host_suffix[left_value]:
                    for right in host_suffix[right_value]:
                        add_overlap(left, right, "nested-host-suffix")
            elif right_value.endswith("." + left_value):
                for left in host_suffix[left_value]:
                    for right in host_suffix[right_value]:
                        add_overlap(left, right, "nested-host-suffix")

    return AuditResult(tuple(kept), tuple(duplicates), tuple(conflicts))


def _is_blackmatrix(rule: Rule) -> bool:
    return rule.source_id.lower().startswith("blackmatrix")


def _is_policy(rule: Rule, name: str) -> bool:
    return rule.policy.casefold() == name.casefold()


_CATEGORY_PREFERENCES: dict[frozenset[str], str] = {
    frozenset(("google-voice", "google")): "google-voice",
    frozenset(("apple", "google")): "google",
    frozenset(("ai", "google")): "ai",
    frozenset(("youtube", "google")): "youtube",
    frozenset(("google", "china-direct")): "google",
    frozenset(("apple", "china-direct")): "apple",
    frozenset(("developer", "github")): "developer",
    frozenset(("china-streaming", "global-media")): "global-media",
}

_VALUE_CATEGORY_PREFERENCES: dict[tuple[frozenset[str], str], str] = {
    (frozenset(("ai", "proxy")), "perplexity.ai"): "ai",
    (frozenset(("ai", "proxy")), "meta.ai"): "ai",
    (frozenset(("ai", "proxy")), "grok.com"): "ai",
    (frozenset(("ai", "proxy")), "x.ai"): "ai",
    (frozenset(("ai", "proxy")), "smoot.apple.com"): "ai",
    (frozenset(("ai", "proxy")), "apple-relay.apple.com"): "ai",
    (frozenset(("ai", "proxy")), "apple-relay.cloudflare.com"): "proxy",
    (frozenset(("ai", "proxy")), "apple-relay.fastly-edge.com"): "proxy",
    (frozenset(("ai", "proxy")), "cp4.cloudflare.com"): "proxy",
    (frozenset(("global-media", "proxy")), "naver.com"): "global-media",
    (frozenset(("global-media", "proxy")), "s3-ap-southeast-1.amazonaws.com"): "proxy",
    (frozenset(("apple", "microsoft")), "akadns.net"): "microsoft",
}


def _category_rule(conflict: Conflict) -> tuple[Rule, Rule] | None:
    categories = frozenset((conflict.left.category, conflict.right.category))
    preferred_category = _VALUE_CATEGORY_PREFERENCES.get((categories, conflict.left.value))
    if preferred_category is None and conflict.left.value == conflict.right.value:
        preferred_category = _VALUE_CATEGORY_PREFERENCES.get((categories, conflict.right.value))
    if preferred_category is None:
        preferred_category = _CATEGORY_PREFERENCES.get(categories)
    if preferred_category is None:
        return None
    if conflict.left.category == preferred_category and conflict.right.category != preferred_category:
        return conflict.left, conflict.right
    if conflict.right.category == preferred_category and conflict.left.category != preferred_category:
        return conflict.right, conflict.left
    return None


def _specific_rule(conflict: Conflict) -> tuple[Rule, Rule] | None:
    if conflict.relation == "host-inside-host-suffix":
        if conflict.left.rule_type == "HOST" and conflict.right.rule_type == "HOST-SUFFIX":
            return conflict.left, conflict.right
        if conflict.right.rule_type == "HOST" and conflict.left.rule_type == "HOST-SUFFIX":
            return conflict.right, conflict.left
    if conflict.relation == "nested-host-suffix":
        if conflict.left.rule_type == "HOST-SUFFIX" and conflict.right.rule_type == "HOST-SUFFIX":
            if len(conflict.left.value) > len(conflict.right.value):
                return conflict.left, conflict.right
            if len(conflict.right.value) > len(conflict.left.value):
                return conflict.right, conflict.left
    return None


def resolve_conflicts(audit: AuditResult) -> ResolutionResult:
    """Resolve conflicts with an explicit Blackmatrix-first policy.

    The priority order is explicit: Blackmatrix, direct over reject, and a
    more specific host rule over a broader host rule. Conflicts that do not
    match one of these rules remain unresolved and both rules stay out of the
    resolved output. This avoids turning source order into an accidental
    policy decision.
    """

    rejected: set[Rule] = set()
    decisions: list[ConflictDecision] = []
    unresolved_rules: set[Rule] = set()
    for conflict in audit.conflicts:
        left_is_preferred = _is_blackmatrix(conflict.left)
        right_is_preferred = _is_blackmatrix(conflict.right)
        if left_is_preferred != right_is_preferred:
            winner = conflict.left if left_is_preferred else conflict.right
            loser = conflict.right if left_is_preferred else conflict.left
            decision = "prefer-blackmatrix"
            reason = "Blackmatrix is the configured primary source."
        elif _is_policy(conflict.left, "direct") != _is_policy(conflict.right, "direct"):
            left_is_direct = _is_policy(conflict.left, "direct")
            left_is_reject = _is_policy(conflict.left, "reject")
            right_is_direct = _is_policy(conflict.right, "direct")
            right_is_reject = _is_policy(conflict.right, "reject")
            if (left_is_direct and right_is_reject) or (right_is_direct and left_is_reject):
                winner = conflict.left if left_is_direct else conflict.right
                loser = conflict.right if left_is_direct else conflict.left
                decision = "prefer-direct"
                reason = "direct takes precedence over reject."
            else:
                specific = _specific_rule(conflict)
                if specific is not None:
                    winner, loser = specific
                    decision = "prefer-specific"
                    reason = "A specific host rule takes precedence over a broader host rule."
                else:
                    category_rule = _category_rule(conflict)
                    if category_rule is not None:
                        winner, loser = category_rule
                        decision = "prefer-category"
                        reason = "The configured business-category priority applies to this conflict."
                    else:
                        winner = loser = None
                        decision = "unresolved"
                        reason = "No configured priority applies to this conflict."
        else:
            specific = _specific_rule(conflict)
            if specific is not None:
                winner, loser = specific
                decision = "prefer-specific"
                reason = "A specific host rule takes precedence over a broader host rule."
            else:
                category_rule = _category_rule(conflict)
                if category_rule is not None:
                    winner, loser = category_rule
                    decision = "prefer-category"
                    reason = "The configured business-category priority applies to this conflict."
                else:
                    winner = loser = None
                    decision = "unresolved"
                    reason = "No configured priority applies to this conflict."

        if decision != "unresolved" and winner is not None and loser is not None:
            rejected.add(loser)
            decisions.append(
                ConflictDecision(
                    conflict=conflict,
                    decision=decision,
                    winner=winner,
                    loser=loser,
                    reason=reason,
                )
            )
        else:
            unresolved_rules.update((conflict.left, conflict.right))
            decisions.append(
                ConflictDecision(
                    conflict=conflict,
                    decision="unresolved",
                    reason=reason,
                )
            )

    rejected.update(unresolved_rules)
    resolved = tuple(rule for rule in audit.kept_rules if rule not in rejected)
    return ResolutionResult(tuple(resolved), tuple(decisions), frozenset(rejected))
