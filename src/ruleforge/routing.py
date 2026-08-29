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


# These are business-level first-match requirements.  Rule-level specificity
# is handled by the audit result and target renderer; these constraints keep
# the broad category order from being accidentally inverted.
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


def rule_sort_key(rule: Rule) -> tuple[tuple[int, str], tuple[int, int, int, str, str], str]:
    return category_sort_key(rule.category), rule_specificity_key(rule), rule.policy
