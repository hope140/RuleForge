from __future__ import annotations

from dataclasses import dataclass
import fnmatch
import ipaddress
from typing import Iterable

from .curation import SharedInfrastructureRisk, audit_shared_infrastructure
from .model import Rule
from .routing import category_sort_key, rule_sort_key


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
class RoutingConstraint:
    """A first-match ordering requirement for two overlapping rules."""

    before: Rule
    after: Rule
    reason: str

    def to_dict(self) -> dict[str, object]:
        def rule_ref(rule: Rule) -> dict[str, object]:
            return {
                "source_id": rule.source_id,
                "category": rule.category,
                "rule_type": rule.rule_type,
                "value": rule.value,
                "policy": rule.policy,
            }

        return {
            "before": rule_ref(self.before),
            "after": rule_ref(self.after),
            "reason": self.reason,
        }


@dataclass(frozen=True)
class ResolutionResult:
    rules: tuple[Rule, ...]
    decisions: tuple[ConflictDecision, ...]
    rejected_rules: frozenset[Rule]
    constraints: tuple[RoutingConstraint, ...] = ()

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
    def value_category_decisions(self) -> tuple[ConflictDecision, ...]:
        return tuple(item for item in self.decisions if item.decision == "prefer-value-category")

    @property
    def protective_reject_decisions(self) -> tuple[ConflictDecision, ...]:
        return tuple(item for item in self.decisions if item.decision == "prefer-reject")

    @property
    def fallback_decisions(self) -> tuple[ConflictDecision, ...]:
        return tuple(item for item in self.decisions if item.decision == "prefer-fallback")

    @property
    def priority_override_rules(self) -> tuple[Rule, ...]:
        """Rules that need an active first-match override across providers.

        Category files are consumed as whole providers by both targets.  When
        a cross-category constraint points from a later category to an earlier
        one, the winning rule is duplicated into a small priority resource so
        the generated client configuration can enforce the same decision.
        """

        candidates = {
            constraint.before
            for constraint in self.constraints
            if category_sort_key(constraint.before.category)
            >= category_sort_key(constraint.after.category)
        }
        return tuple(sorted(candidates, key=rule_sort_key))

    @property
    def ordered_overlap_decisions(self) -> tuple[ConflictDecision, ...]:
        return tuple(item for item in self.decisions if item.decision == "ordered-overlap")

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
            "value_category_preferred_conflict_count": len(self.value_category_decisions),
            "protective_reject_conflict_count": len(self.protective_reject_decisions),
            "fallback_conflict_count": len(self.fallback_decisions),
            "priority_override_rule_count": len(self.priority_override_rules),
            "ordered_overlap_count": len(self.ordered_overlap_decisions),
            "unresolved_conflict_count": len(self.unresolved_decisions),
            "decisions": [item.to_dict() for item in self.decisions],
            "routing_constraints": [item.to_dict() for item in self.constraints],
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
            "value_category_preferred_conflict_count": len(self.value_category_decisions),
            "protective_reject_conflict_count": len(self.protective_reject_decisions),
            "fallback_conflict_count": len(self.fallback_decisions),
            "priority_override_rule_count": len(self.priority_override_rules),
            "ordered_overlap_count": len(self.ordered_overlap_decisions),
            "unresolved_conflict_count": len(self.unresolved_decisions),
        }


@dataclass(frozen=True)
class AuditResult:
    kept_rules: tuple[Rule, ...]
    duplicates: tuple[Duplicate, ...]
    conflicts: tuple[Conflict, ...]
    shared_infrastructure_risks: tuple[SharedInfrastructureRisk, ...] = ()

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
            "shared_infrastructure_risk_count": len(self.shared_infrastructure_risks),
            "duplicates": [item.to_dict() for item in self.duplicates],
            "conflicts": [item.to_dict() for item in self.conflicts],
            "shared_infrastructure_risks": [
                item.to_dict() for item in self.shared_infrastructure_risks
            ],
        }


def _parent_domains(value: str) -> Iterable[str]:
    parts = value.split(".")
    for index in range(1, len(parts)):
        yield ".".join(parts[index:])


_NETWORK_RULE_TYPES = {"IP-CIDR", "IP6-CIDR"}


def _network(rule: Rule) -> ipaddress.IPv4Network | ipaddress.IPv6Network | None:
    if rule.rule_type not in _NETWORK_RULE_TYPES:
        return None
    try:
        return ipaddress.ip_network(rule.value, strict=False)
    except ValueError:
        return None


def _wildcard_matches_value(pattern: str, value: str) -> bool:
    # A suffix rule represents both its base domain and subdomains. Testing
    # both forms catches the common wildcard shapes without pretending to
    # solve arbitrary wildcard-language containment.
    return any(
        fnmatch.fnmatchcase(candidate, pattern)
        for candidate in (value, "probe." + value)
    )


def audit_rules(rules: Iterable[Rule]) -> AuditResult:
    kept: list[Rule] = []
    duplicates: list[Duplicate] = []
    conflicts: list[Conflict] = []
    exact: dict[tuple[str, str, tuple[str, ...]], list[Rule]] = {}
    for rule in rules:
        group = exact.setdefault(rule.identity_key, [])
        previous_same_policy = next(
            (previous for previous in group if previous.policy == rule.policy),
            None,
        )
        if previous_same_policy is not None:
            duplicates.append(Duplicate(previous_same_policy, rule))
            continue
        for previous in group:
            if previous.policy != rule.policy:
                conflicts.append(
                    Conflict("exact-policy", "same-rule-different-policy", previous, rule)
                )
        group.append(rule)
        kept.append(rule)

    host_exact: dict[str, list[Rule]] = {}
    host_suffix: dict[str, list[Rule]] = {}
    host_keyword: list[Rule] = []
    host_wildcard: list[Rule] = []
    for rule in kept:
        if rule.rule_type == "HOST":
            host_exact.setdefault(rule.value, []).append(rule)
        elif rule.rule_type == "HOST-SUFFIX":
            host_suffix.setdefault(rule.value, []).append(rule)
        elif rule.rule_type == "HOST-KEYWORD":
            host_keyword.append(rule)
        elif rule.rule_type == "HOST-WILDCARD":
            host_wildcard.append(rule)

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

    specific_domain_rules = [
        rule
        for rule in kept
        if rule.rule_type in {"HOST", "HOST-SUFFIX", "HOST-WILDCARD"}
    ]
    for keyword_rule in host_keyword:
        for other in specific_domain_rules:
            if keyword_rule.value in other.value:
                add_overlap(keyword_rule, other, "host-keyword-overlap")
        for other in host_keyword:
            if keyword_rule is other:
                continue
            if keyword_rule.value in other.value or other.value in keyword_rule.value:
                add_overlap(keyword_rule, other, "host-keyword-overlap")

    for wildcard_rule in host_wildcard:
        for other_rules in [*host_exact.values(), *host_suffix.values()]:
            for other in other_rules:
                if _wildcard_matches_value(wildcard_rule.value, other.value):
                    add_overlap(wildcard_rule, other, "host-wildcard-overlap")

    network_rules = [
        (rule, network)
        for rule in kept
        if (network := _network(rule)) is not None
    ]
    for index, (left_rule, left_network) in enumerate(network_rules):
        for right_rule, right_network in network_rules[index + 1 :]:
            if left_rule.identity_key == right_rule.identity_key:
                continue
            if left_network.version == right_network.version and left_network.overlaps(right_network):
                add_overlap(left_rule, right_rule, "ip-cidr-overlap")

    return AuditResult(
        tuple(kept),
        tuple(duplicates),
        tuple(conflicts),
        audit_shared_infrastructure(kept),
    )


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
    frozenset(("ai", "global-media")): "ai",
    frozenset(("developer", "github")): "developer",
    frozenset(("china-media", "global-media")): "china-media",
    frozenset(("china-streaming", "global-media")): "global-media",
    frozenset(("china-direct", "global-media")): "global-media",
    frozenset(("google", "social")): "social",
    frozenset(("github", "proxy")): "github",
    frozenset(("tiktok", "global-media")): "tiktok",
    frozenset(("youtube", "global-media")): "youtube",
    frozenset(("social", "netflix")): "netflix",
    frozenset(("proxy", "telegram")): "telegram",
    frozenset(("apple", "microsoft")): "microsoft",
    frozenset(("spotify", "global-media")): "spotify",
    frozenset(("netflix", "global-media")): "netflix",
    frozenset(("global-media", "china-services")): "china-services",
    frozenset(("google", "direct-exception")): "direct-exception",
    frozenset(("global-media", "proxy")): "global-media",
    frozenset(("ai", "proxy")): "ai",
    frozenset(("china-direct", "proxy")): "china-direct",
    frozenset(("google", "proxy")): "google",
    frozenset(("youtube", "proxy")): "youtube",
    frozenset(("apple", "proxy")): "apple",
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
    (frozenset(("ai", "github")), "githubcopilot.com"): "ai",
    (frozenset(("ai", "social")), "grok.com"): "ai",
    (frozenset(("ai", "social")), "x.ai"): "ai",
    (frozenset(("ai", "apple")), "gspe1-ssl.ls.apple.com"): "apple",
    (frozenset(("ai", "apple")), "guzzoni.apple.com"): "apple",
    (frozenset(("ai", "tiktok")), "byteoversea.com"): "tiktok",
    (frozenset(("ai", "developer")), "grazie.ai"): "developer",
    (frozenset(("ai", "developer")), "jetbrains.ai"): "developer",
    (frozenset(("ai", "proxy")), "openai.com"): "ai",
    (frozenset(("ai", "proxy")), "chatgpt.com"): "ai",
    (frozenset(("ai", "proxy")), "copilot.microsoft.com"): "ai",
    (frozenset(("ai", "proxy")), "gateway.icloud.com"): "ai",
    (frozenset(("github", "proxy")), "githubusercontent.com"): "github",
    (frozenset(("github", "proxy")), "github.global.ssl.fastly.net"): "github",
    (frozenset(("github", "proxy")), "github.com"): "github",
    (frozenset(("github", "proxy")), "github.io"): "github",
    (frozenset(("github", "proxy")), "github.blog"): "github",
    (frozenset(("github", "proxy")), "githubassets.com"): "github",
    (frozenset(("youtube", "global-media")), "youtube.com"): "youtube",
    (frozenset(("youtube", "global-media")), "youtubei.googleapis.com"): "youtube",
    (frozenset(("youtube", "global-media")), "yt3.ggpht.com"): "youtube",
    (frozenset(("youtube", "global-media")), "withyoutube.com"): "youtube",
    (frozenset(("youtube", "global-media")), "youtubeeducation.com"): "youtube",
    (frozenset(("youtube", "global-media")), "youtubegaming.com"): "youtube",
    (frozenset(("youtube", "global-media")), "youtubekids.com"): "youtube",
    (frozenset(("youtube", "global-media")), "youtube-nocookie.com"): "youtube",
    (frozenset(("youtube", "global-media")), "googlevideo.com"): "youtube",
    (frozenset(("google", "global-media")), "googlevideo.com"): "google",
    (frozenset(("tiktok", "global-media")), "tiktok.com"): "tiktok",
    (frozenset(("tiktok", "global-media")), "tiktokcdn.com"): "tiktok",
    (frozenset(("tiktok", "global-media")), "tiktokcdn-eu.com"): "tiktok",
    (frozenset(("tiktok", "global-media")), "tiktokv.com"): "tiktok",
    (frozenset(("tiktok", "global-media")), "musical.ly"): "tiktok",
    (frozenset(("tiktok", "global-media")), "tiktokcdn-"): "tiktok",
    (frozenset(("spotify", "global-media")), "-spotify-com"): "spotify",
    (frozenset(("spotify", "global-media")), "spotify.com"): "spotify",
    (frozenset(("google", "global-media")), "youtubei.googleapis.com"): "google",
    (frozenset(("google", "proxy")), "appspot.com"): "google",
    (frozenset(("google", "proxy")), ".blogspot"): "google",
    (frozenset(("google", "proxy")), "blogspot"): "google",
    (frozenset(("apple", "global-media")), "tv.applemusic.com"): "apple",
    (frozenset(("apple", "proxy")), "apple.news"): "apple",
    (frozenset(("apple", "proxy")), "apple.comscoreresearch.com"): "apple",
    (frozenset(("google", "direct-exception")), "redirector.gvt1.com"): "google",
}

_EXACT_CATEGORY_PREFERENCES = {
    frozenset(("china-media", "global-media")),
}

_APPLE_SERVICE_SUFFIXES = ("apple.com", "icloud.com", "mzstatic.com")
_APPLE_SERVICE_HOSTS = {
    "apple-relay.cloudflare.com",
    "apple-relay.fastly-edge.com",
    "cp4.cloudflare.com",
}


def _preferred_category_rule(
    conflict: Conflict,
    preferred_category: str | None,
) -> tuple[Rule, Rule] | None:
    if preferred_category is None:
        return None
    if conflict.left.category == preferred_category and conflict.right.category != preferred_category:
        return conflict.left, conflict.right
    if conflict.right.category == preferred_category and conflict.left.category != preferred_category:
        return conflict.right, conflict.left
    return None


def _value_category_rule(conflict: Conflict) -> tuple[Rule, Rule] | None:
    categories = frozenset((conflict.left.category, conflict.right.category))
    for value in (conflict.left.value, conflict.right.value):
        preferred = _VALUE_CATEGORY_PREFERENCES.get((categories, value.casefold()))
        result = _preferred_category_rule(conflict, preferred)
        if result is not None:
            return result
    # Apple service ownership is an explicit business contract.  Keep it in
    # the value-category tier so a deliberately specific third-party rule
    # cannot reclassify an Apple endpoint merely by being a HOST rule.
    if "apple" in categories and "direct-exception" not in categories:
        apple_values = (conflict.left.value, conflict.right.value)
        if any(
            value.casefold() in _APPLE_SERVICE_HOSTS
            or any(
                value.casefold() == suffix
                or value.casefold().endswith("." + suffix)
                for suffix in _APPLE_SERVICE_SUFFIXES
            )
            for value in apple_values
        ):
            return _preferred_category_rule(conflict, "apple")
    return None


def _category_rule(conflict: Conflict) -> tuple[Rule, Rule] | None:
    """Return the configured value or business-category preference."""

    return _value_category_rule(conflict) or _business_category_rule(conflict)


def _business_category_rule(conflict: Conflict) -> tuple[Rule, Rule] | None:
    categories = frozenset((conflict.left.category, conflict.right.category))
    return _preferred_category_rule(conflict, _CATEGORY_PREFERENCES.get(categories))


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
    if conflict.relation == "host-keyword-overlap":
        left_is_keyword = conflict.left.rule_type == "HOST-KEYWORD"
        right_is_keyword = conflict.right.rule_type == "HOST-KEYWORD"
        if left_is_keyword != right_is_keyword:
            return (
                (conflict.right, conflict.left)
                if left_is_keyword
                else (conflict.left, conflict.right)
            )
        if left_is_keyword and right_is_keyword:
            if len(conflict.left.value) > len(conflict.right.value):
                return conflict.left, conflict.right
            if len(conflict.right.value) > len(conflict.left.value):
                return conflict.right, conflict.left
    if conflict.relation == "host-wildcard-overlap":
        if conflict.left.rule_type == "HOST-WILDCARD" and conflict.right.rule_type != "HOST-WILDCARD":
            return conflict.right, conflict.left
        if conflict.right.rule_type == "HOST-WILDCARD" and conflict.left.rule_type != "HOST-WILDCARD":
            return conflict.left, conflict.right
    if conflict.relation == "ip-cidr-overlap":
        left_network = _network(conflict.left)
        right_network = _network(conflict.right)
        if left_network is not None and right_network is not None:
            if left_network.subnet_of(right_network) and left_network != right_network:
                return conflict.left, conflict.right
            if right_network.subnet_of(left_network) and left_network != right_network:
                return conflict.right, conflict.left
    return None


def _is_direct_exception(rule: Rule) -> bool:
    return rule.category == "direct-exception" and _is_policy(rule, "direct")


def _security_order(conflict: Conflict) -> tuple[Rule, Rule, str] | None:
    """Return the safe first-match order for reject/direct overlaps.

    Normal direct rules must not silently defeat an advertising or privacy
    reject rule.  A deliberately named ``direct-exception`` category is the
    only direct policy allowed to override reject.
    """

    left_reject = _is_policy(conflict.left, "reject")
    right_reject = _is_policy(conflict.right, "reject")
    if left_reject == right_reject:
        return None
    reject = conflict.left if left_reject else conflict.right
    other = conflict.right if left_reject else conflict.left
    if _is_direct_exception(other):
        return other, reject, "An explicit direct-exception may override reject."
    return reject, other, "Reject rules take precedence over ordinary direct or proxy rules."


def _source_order(conflict: Conflict) -> tuple[Rule, Rule, str] | None:
    # Source trust is only meaningful after the business category is known.
    # In particular, Blackmatrix must never decide whether a selector belongs
    # to AI, GitHub, Social, Google or another business category.
    if conflict.left.category != conflict.right.category:
        return None
    left_is_preferred = _is_blackmatrix(conflict.left)
    right_is_preferred = _is_blackmatrix(conflict.right)
    if left_is_preferred == right_is_preferred:
        return None
    winner = conflict.left if left_is_preferred else conflict.right
    loser = conflict.right if left_is_preferred else conflict.left
    return winner, loser, "Blackmatrix is the preferred source within this business category."


def _fallback_order(conflict: Conflict) -> tuple[Rule, Rule, str] | None:
    if conflict.left.category == conflict.right.category:
        return None
    left_key = category_sort_key(conflict.left.category)
    right_key = category_sort_key(conflict.right.category)
    if left_key == right_key:
        return None
    if left_key < right_key:
        return conflict.left, conflict.right, "The shared routing category order provides a stable first-match order."
    return conflict.right, conflict.left, "The shared routing category order provides a stable first-match order."


def _ordered_overlap_rule(conflict: Conflict) -> tuple[Rule, Rule, str] | None:
    security = _security_order(conflict)
    if security is not None:
        return security
    value_category = _value_category_rule(conflict)
    if value_category is not None:
        return (
            value_category[0],
            value_category[1],
            "An explicit value-category override provides the first-match order.",
        )
    specific = _specific_rule(conflict)
    if specific is not None:
        return specific[0], specific[1], "A more specific rule must be evaluated before its broader overlap."
    category = _business_category_rule(conflict)
    if category is not None:
        return category[0], category[1], "The configured business-category priority provides the first-match order."
    source = _source_order(conflict)
    if source is not None:
        return source
    return _fallback_order(conflict)


def _exact_conflict_rule(conflict: Conflict) -> tuple[Rule, Rule, str, str] | None:
    security = _security_order(conflict)
    if security is not None:
        winner, loser, reason = security
        decision = "prefer-direct-exception" if _is_direct_exception(winner) else "prefer-reject"
        return winner, loser, decision, reason
    value_category = _value_category_rule(conflict)
    if value_category is not None:
        winner, loser = value_category
        return winner, loser, "prefer-value-category", "An explicit value-category override applies to this exact conflict."
    specific = _specific_rule(conflict)
    if specific is not None:
        winner, loser = specific
        return winner, loser, "prefer-specific", "A more specific rule applies to this exact conflict."
    category = _business_category_rule(conflict)
    if category is not None:
        winner, loser = category
        return winner, loser, "prefer-category", "The configured business-category priority applies to this exact conflict."
    source = _source_order(conflict)
    if source is not None:
        winner, loser, reason = source
        return winner, loser, "prefer-blackmatrix", reason
    return None


def resolve_conflicts(audit: AuditResult) -> ResolutionResult:
    """Resolve exclusive conflicts and preserve ordered semantic overlaps.

    Exact selector conflicts are exclusive and select one policy.  Semantic
    overlaps are not exclusive: both rules stay in the output, while the
    preferred first-match rule is recorded as a routing constraint.  Only an
    unresolved exact conflict or an overlap with no stable ordering removes
    rules from the safe result.
    """

    rejected: set[Rule] = set()
    decisions: list[ConflictDecision] = []
    unresolved_rules: set[Rule] = set()
    constraints: list[RoutingConstraint] = []
    constraint_keys: set[tuple[Rule, Rule]] = set()

    for conflict in audit.conflicts:
        if conflict.kind == "exact-policy":
            exact = _exact_conflict_rule(conflict)
            if exact is not None:
                winner, loser, decision, reason = exact
                rejected.add(loser)
                decisions.append(ConflictDecision(conflict, decision, winner, loser, reason))
                continue
            unresolved_rules.update((conflict.left, conflict.right))
            decisions.append(
                ConflictDecision(
                    conflict=conflict,
                    decision="unresolved",
                    reason="No exact-conflict priority applies; both policies are excluded for safety.",
                )
            )
            continue

        ordered = _ordered_overlap_rule(conflict)
        if ordered is None:
            unresolved_rules.update((conflict.left, conflict.right))
            decisions.append(
                ConflictDecision(
                    conflict=conflict,
                    decision="unresolved",
                    reason="No stable first-match order applies; both rules are excluded for safety.",
                )
            )
            continue

        before, after, reason = ordered
        decisions.append(
            ConflictDecision(
                conflict=conflict,
                decision="ordered-overlap",
                winner=before,
                loser=after,
                reason=f"Both rules are retained. {reason}",
            )
        )
        if before.category != after.category and (before, after) not in constraint_keys:
            constraint_keys.add((before, after))
            constraints.append(RoutingConstraint(before, after, reason))

    rejected.update(unresolved_rules)
    resolved = tuple(rule for rule in audit.kept_rules if rule not in rejected)
    return ResolutionResult(
        tuple(resolved),
        tuple(decisions),
        frozenset(rejected),
        tuple(constraints),
    )
