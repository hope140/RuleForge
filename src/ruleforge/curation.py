from __future__ import annotations

from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Iterable

from .model import Rule


# These are shared SaaS/cloud surfaces found in third-party AI lists.  A root
# suffix is dropped from the AI category, while explicitly named service
# endpoints such as anthropic.auth0.com remain eligible for review and routing.
SHARED_INFRA_SUFFIXES = frozenset(
    {
        "auth0.com",
        "algolia.net",
        "identrust.com",
        "intercom.io",
        "intercomcdn.com",
        "launchdarkly.com",
        "segment.io",
        "sentry.io",
        "stripe.com",
    }
)

# These roots are intentionally broader than the AI curation list.  They are
# used by the semantic audit as a warning signal for every dedicated service
# category.  A subdomain such as ``service.example.amazonaws.com`` is not a
# root and remains eligible for normal rule review.
SHARED_INFRASTRUCTURE_ROOTS = frozenset(
    {
        "amazonaws.com",
        "us-west-2.amazonaws.com",
        "azure.com",
        "azureedge.net",
        "azurefd.net",
        "cloudflare.com",
        "cloudflare.net",
        "fastly.net",
        "akamaized.net",
        "akamaihd.net",
        "digicert.com",
        "onetrust.com",
        "sentry.io",
        "statsig.com",
        "statsigapi.net",
        "intercom.io",
        "intercomcdn.com",
        "segment.io",
        "launchdarkly.com",
        # These two are third-party consent surfaces also seen in media
        # lists; keeping them here makes the audit useful outside AI.
        "cookielaw.org",
        "auth0.com",
        "algolia.net",
        "identrust.com",
        "stripe.com",
    }
)

# The Copilot upstream list contains a mixture of Copilot endpoints and
# ordinary Bing/Microsoft/MSN infrastructure.  These exact hosts are
# removed only when they arrive in the AI category; the Microsoft/Bing
# category remains responsible for the ordinary service traffic.
AI_EXCLUDED_HOSTS = frozenset(
    {
        "api.msn.com",
        "assets.msn.com",
        "in.appcenter.ms",
        "location.microsoft.com",
        "odc.officeapps.live.com",
        "r.bing.com",
        "self.events.data.microsoft.com",
        "services.bingapis.com",
        "www.bing.com",
    }
)

# Known upstream rules whose selector is a whole shared service surface.  The
# exclusions are deliberately narrow and do not remove more specific hosts
# below the same provider root.
CATEGORY_RULE_EXCLUSIONS = frozenset(
    {
        ("netflix", "HOST-SUFFIX", "cookielaw.org"),
        ("netflix", "HOST-SUFFIX", "onetrust.com"),
        ("netflix", "HOST-SUFFIX", "us-west-2.amazonaws.com"),
        ("apple", "HOST-SUFFIX", "digicert.com"),
        ("global-media", "HOST", "www.amazon.com"),
    }
)

# RuleGo's generic direct exception would otherwise mask Google's more
# specific redirector ownership in the Mihomo target.
ROUTING_RULE_EXCLUSIONS = frozenset(
    {("direct-exception", "HOST", "redirector.gvt1.com")}
)

# Generic proxy lists occasionally repeat a service endpoint that already has
# an explicit AI/Apple owner.  Remove only the known endpoint, not the whole
# parent domain.
BUSINESS_RULE_EXCLUSIONS = frozenset(
    {("proxy", "HOST", "gateway.icloud.com")}
)

# Keep the source manifests stable while correcting a few high-confidence
# business ownership exceptions from upstream classifications.
CATEGORY_RECLASSIFICATIONS = {
    ("tiktok", "HOST-SUFFIX", "trae.ai"): ("ai", "AI", "ai-tool"),
    ("tiktok", "HOST-SUFFIX", "marscode.com"): ("ai", "AI", "ai-tool"),
    ("proxy", "HOST", "amp-api.podcasts.apple.com"): (
        "apple",
        "苹果服务",
        "apple-service",
    ),
    ("ai", "HOST-SUFFIX", "gateway.icloud.com"): (
        "apple",
        "苹果服务",
        "apple-service",
    ),
}

_AUDIT_EXEMPT_CATEGORIES = frozenset({"reject", "privacy"})
_BROAD_CATEGORY_RISK = frozenset(
    {"proxy", "proxy-exception", "microsoft", "cloud", "global-media"}
)

# Cloud provider ASNs that host unrelated third-party services; a whole ASN
# must never be pinned to a single service category (see curation notes).
# 14061=Hetzner, 20473=Vultr, 132203=Tencent Cloud International (its
# WeChat-derived entry force-DIRECTed api.assrt.net and other tenants).
SHARED_INFRA_ASNS = frozenset({"14061", "20473", "132203"})


@dataclass(frozen=True)
class CurationPolicy:
    shared_infra_suffixes: frozenset[str] = SHARED_INFRA_SUFFIXES
    shared_infra_asns: frozenset[str] = SHARED_INFRA_ASNS
    ai_excluded_hosts: frozenset[str] = AI_EXCLUDED_HOSTS
    category_rule_exclusions: frozenset[tuple[str, str, str]] = CATEGORY_RULE_EXCLUSIONS
    routing_rule_exclusions: frozenset[tuple[str, str, str]] = ROUTING_RULE_EXCLUSIONS
    business_rule_exclusions: frozenset[tuple[str, str, str]] = BUSINESS_RULE_EXCLUSIONS
    category_reclassifications: dict[tuple[str, str, str], tuple[str, str, str]] = field(
        default_factory=lambda: dict(CATEGORY_RECLASSIFICATIONS)
    )


def load_curation_policy(path: str | Path | None = None) -> CurationPolicy:
    """Load the auditable curation list, with built-in safe defaults."""

    policy_path = (
        Path(path)
        if path is not None
        else Path(__file__).resolve().parents[2] / "curation/ai.drop.list"
    )
    if not policy_path.exists():
        return CurationPolicy()
    suffixes: set[str] = set()
    asns: set[str] = set()
    hosts: set[str] = set()
    for line_number, raw_line in enumerate(
        policy_path.read_text(encoding="utf-8-sig").splitlines(), start=1
    ):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [part.strip() for part in line.split(",", 1)]
        if len(parts) != 2 or not parts[1]:
            raise ValueError(f"invalid curation entry at {policy_path}:{line_number}")
        rule_type, value = parts[0].upper(), parts[1].casefold()
        if rule_type == "IP-ASN":
            asns.add(value)
        elif rule_type == "DOMAIN-SUFFIX":
            suffixes.add(value.rstrip("."))
        elif rule_type in {"DOMAIN", "HOST"}:
            hosts.add(value.rstrip("."))
        else:
            raise ValueError(
                f"unsupported curation entry at {policy_path}:{line_number}: {rule_type}"
            )
    return CurationPolicy(frozenset(suffixes), frozenset(asns), frozenset(hosts))


@dataclass(frozen=True)
class CurationDrop:
    rule: Rule
    reason: str

    def to_dict(self) -> dict[str, object]:
        return {
            "source_id": self.rule.source_id,
            "category": self.rule.category,
            "policy": self.rule.policy,
            "rule_type": self.rule.rule_type,
            "value": self.rule.value,
            "line_number": self.rule.line_number,
            "raw": self.rule.raw,
            "reason": self.reason,
        }


@dataclass(frozen=True)
class CurationMove:
    """A rule whose business category was corrected during curation."""

    original: Rule
    replacement: Rule
    reason: str

    def to_dict(self) -> dict[str, object]:
        return {
            "source_id": self.original.source_id,
            "rule_type": self.original.rule_type,
            "value": self.original.value,
            "from_category": self.original.category,
            "from_policy": self.original.policy,
            "to_category": self.replacement.category,
            "to_policy": self.replacement.policy,
            "reason": self.reason,
        }


@dataclass(frozen=True)
class SharedInfrastructureRisk:
    """A warning for a dedicated category claiming a shared root domain."""

    rule: Rule
    risk: str = "high"
    reason: str = "shared-infrastructure-root"

    def to_dict(self) -> dict[str, object]:
        return {
            "category": self.rule.category,
            "rule": f"{self.rule.rule_type},{self.rule.value}",
            "risk": self.risk,
            "reason": self.reason,
            "source_id": self.rule.source_id,
            "policy": self.rule.policy,
            "rule_type": self.rule.rule_type,
            "value": self.rule.value,
        }


@dataclass(frozen=True)
class CurationResult:
    rules: tuple[Rule, ...]
    dropped: tuple[CurationDrop, ...]
    moved: tuple[CurationMove, ...] = ()

    def to_dict(self) -> dict[str, object]:
        return {
            "kept_rule_count": len(self.rules),
            "dropped_rule_count": len(self.dropped),
            "moved_rule_count": len(self.moved),
            "dropped": [item.to_dict() for item in self.dropped],
            "moved": [item.to_dict() for item in self.moved],
        }


def _drop_reason(rule: Rule, policy: CurationPolicy) -> str | None:
    # A whole cloud-provider ASN is too broad to pin to any single service:
    # one blanket policy would force-route every tenant of the provider
    # (e.g. api.assrt.net on Tencent Cloud international was pinned DIRECT by
    # the WeChat category and then reset by the censor).  ASN entries are
    # therefore dropped from every category and left to downstream rules.
    # The configurable root SaaS suffix list stays limited to AI; the small
    # set of independently confirmed Netflix/Apple/media corrections is
    # handled by category-specific exclusions below.
    if rule.rule_type == "IP-ASN" and rule.value in policy.shared_infra_asns:
        return "shared-infrastructure-asn"
    if (
        rule.category == "ai"
        and rule.rule_type == "HOST"
        and rule.value in policy.ai_excluded_hosts
    ):
        return "shared-microsoft-infrastructure-host"
    if rule.category != "ai":
        if (rule.category, rule.rule_type, rule.value) in policy.routing_rule_exclusions:
            return "specificity-routing-correction"
        if (rule.category, rule.rule_type, rule.value) in policy.business_rule_exclusions:
            return "business-category-correction"
        return (
            "shared-infrastructure-root"
            if (rule.category, rule.rule_type, rule.value)
            in policy.category_rule_exclusions
            else None
        )
    if (
        rule.rule_type in {"HOST", "HOST-SUFFIX"}
        and rule.value in policy.shared_infra_suffixes
    ):
        return "shared-infrastructure-root-suffix"
    if (rule.category, rule.rule_type, rule.value) in policy.routing_rule_exclusions:
        return "specificity-routing-correction"
    if (rule.category, rule.rule_type, rule.value) in policy.business_rule_exclusions:
        return "business-category-correction"
    if (rule.category, rule.rule_type, rule.value) in policy.category_rule_exclusions:
        return "shared-infrastructure-root"
    return None


def audit_shared_infrastructure(
    rules: Iterable[Rule],
    *,
    roots: Iterable[str] = SHARED_INFRASTRUCTURE_ROOTS,
) -> tuple[SharedInfrastructureRisk, ...]:
    """Find exact shared-infrastructure roots claimed by service categories.

    Only an exact HOST/HOST-SUFFIX root is reported.  A named service host
    below a provider root remains available for ordinary category review.
    """

    normalized_roots = frozenset(value.casefold().rstrip(".") for value in roots)
    return tuple(
        SharedInfrastructureRisk(
            rule,
            risk="medium" if rule.category in _BROAD_CATEGORY_RISK else "high",
        )
        for rule in rules
        if rule.category not in _AUDIT_EXEMPT_CATEGORIES
        if rule.rule_type in {"HOST", "HOST-SUFFIX"}
        and rule.value.casefold().rstrip(".") in normalized_roots
    )


def curate_rules(
    rules: Iterable[Rule],
    *,
    policy: CurationPolicy | None = None,
) -> CurationResult:
    active_policy = policy or load_curation_policy()
    kept: list[Rule] = []
    dropped: list[CurationDrop] = []
    moved: list[CurationMove] = []
    for rule in rules:
        reason = _drop_reason(rule, active_policy)
        if reason is not None:
            dropped.append(CurationDrop(rule, reason))
            continue
        move = active_policy.category_reclassifications.get(
            (rule.category, rule.rule_type, rule.value)
        )
        if move is None:
            kept.append(rule)
            continue
        category, policy_name, move_reason = move
        replacement = replace(rule, category=category, policy=policy_name)
        kept.append(replacement)
        moved.append(CurationMove(rule, replacement, move_reason))
    return CurationResult(tuple(kept), tuple(dropped), tuple(moved))
