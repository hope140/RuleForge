from __future__ import annotations

import ipaddress

from .model import Rule

# This is the single category order used by target renderers and routing-order
# tests.  More specific categories appear before broad business fallbacks.
ROUTING_CATEGORY_ORDER = (
    "direct-exception",
    "reject",
    "privacy",
    "ai",
    "google-voice",
    "youtube",
    "netflix",
    "tiktok",
    "telegram",
    "spotify",
    "developer",
    "github",
    "apple",
    "social",
    "google",
    "microsoft",
    "cloud",
    "china-media",
    "global-media",
    "alipay",
    "wechat",
    "china-services",
    "china-streaming",
    "china-direct",
    "proxy-exception",
    "proxy",
)


# These are business-level first-match requirements used when rule specificity
# cannot distinguish two overlapping selectors.  A renderer may still use
# this category order for whole category providers, while the route simulator
# orders individual selectors by specificity first.
ROUTING_CATEGORY_CONSTRAINTS = (
    ("direct-exception", "reject"),
    ("direct-exception", "privacy"),
    ("reject", "china-services"),
    ("reject", "china-streaming"),
    ("reject", "proxy"),
    ("privacy", "china-services"),
    ("privacy", "proxy"),
    ("ai", "google"),
    ("ai", "global-media"),
    ("ai", "developer"),
    ("ai", "github"),
    ("google-voice", "google"),
    ("youtube", "google"),
    ("youtube", "global-media"),
    ("tiktok", "global-media"),
    ("netflix", "global-media"),
    ("developer", "github"),
    ("social", "google"),
    ("github", "proxy"),
    ("telegram", "proxy"),
    ("china-media", "china-streaming"),
    ("global-media", "proxy"),
    ("proxy-exception", "proxy"),
)

_APPLE_SERVICE_SUFFIXES = ("apple.com", "icloud.com", "mzstatic.com")
_APPLE_SERVICE_HOSTS = {
    "apple-relay.cloudflare.com",
    "apple-relay.fastly-edge.com",
    "cp4.cloudflare.com",
}


def category_sort_key(category: str) -> tuple[int, str]:
    try:
        return ROUTING_CATEGORY_ORDER.index(category), category
    except ValueError:
        return len(ROUTING_CATEGORY_ORDER), category


def routing_order_violations(
    order: tuple[str, ...] = ROUTING_CATEGORY_ORDER,
) -> tuple[tuple[str, str], ...]:
    rank = {category: index for index, category in enumerate(order)}
    return tuple(
        (before, after)
        for before, after in ROUTING_CATEGORY_CONSTRAINTS
        if rank.get(before, len(order)) >= rank.get(after, len(order))
    )


def rule_specificity_key(rule: Rule) -> tuple[int, int, int, str, str]:
    """Return a deterministic first-match key within a category."""

    if rule.rule_type == "HOST":
        return 0, 0, -len(rule.value), rule.rule_type, rule.value
    if rule.rule_type == "HOST-SUFFIX":
        return 1, -rule.value.count("."), -len(rule.value), rule.rule_type, rule.value
    if rule.rule_type == "HOST-WILDCARD":
        return 2, -rule.value.count("."), -len(rule.value), rule.rule_type, rule.value
    if rule.rule_type == "HOST-KEYWORD":
        return 3, 0, -len(rule.value), rule.rule_type, rule.value
    if rule.rule_type in {"IP-CIDR", "IP6-CIDR"}:
        try:
            prefix = ipaddress.ip_network(rule.value, strict=False).prefixlen
        except ValueError:
            prefix = -1
        return 1, 0, -prefix, rule.rule_type, rule.value
    return 4, 0, 0, rule.rule_type, rule.value


def _is_apple_service_rule(rule: Rule) -> bool:
    if rule.category != "apple" or rule.rule_type not in {"HOST", "HOST-SUFFIX"}:
        return False
    value = rule.value.casefold().rstrip(".")
    return value in _APPLE_SERVICE_HOSTS or any(
        value == suffix or value.endswith("." + suffix)
        for suffix in _APPLE_SERVICE_SUFFIXES
    )


def _security_sort_rank(rule: Rule) -> int:
    if rule.category == "direct-exception" and rule.policy.casefold() == "direct":
        return 0
    if rule.policy.casefold() == "reject":
        return 1
    # The Apple service contract is an explicit value/category preference and
    # therefore sits above ordinary specificity, but below security rules.
    if _is_apple_service_rule(rule):
        return 2
    return 3


def rule_sort_key(
    rule: Rule,
) -> tuple[int, tuple[int, int, int, str, str], tuple[int, str], str]:
    """Return the effective first-match order for individual rules.

    Category order is a fallback.  It must not put a broad rule from an
    earlier category ahead of a more specific selector from another category,
    such as ``gvt1.com`` versus ``redirector.offline-maps.gvt1.com``.
    """

    return (
        _security_sort_rank(rule),
        rule_specificity_key(rule),
        category_sort_key(rule.category),
        rule.policy,
    )


def order_rules_for_category_providers(
    rules: list[Rule] | tuple[Rule, ...],
    *,
    priority_rules: list[Rule] | tuple[Rule, ...] = (),
) -> tuple[Rule, ...]:
    """Model the active order of category providers plus priority overrides."""

    priority = tuple(sorted(priority_rules, key=rule_sort_key))
    priority_set = frozenset(priority)
    grouped: dict[str, list[Rule]] = {}
    for rule in rules:
        if rule in priority_set:
            continue
        grouped.setdefault(rule.category, []).append(rule)

    ordered: list[Rule] = []
    priority_inserted = False
    for category in sorted(grouped, key=category_sort_key):
        ordered.extend(
            sorted(
                grouped[category],
                key=lambda rule: (rule_specificity_key(rule), rule.policy),
            )
        )
        if category == "privacy" and priority:
            ordered.extend(priority)
            priority_inserted = True
    if priority and not priority_inserted:
        ordered[0:0] = priority
    return tuple(ordered)
