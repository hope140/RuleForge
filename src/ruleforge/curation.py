from __future__ import annotations

from dataclasses import dataclass
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

SHARED_INFRA_ASNS = frozenset({"14061", "20473"})


@dataclass(frozen=True)
class CurationPolicy:
    shared_infra_suffixes: frozenset[str] = SHARED_INFRA_SUFFIXES
    shared_infra_asns: frozenset[str] = SHARED_INFRA_ASNS


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
        else:
            raise ValueError(
                f"unsupported curation entry at {policy_path}:{line_number}: {rule_type}"
            )
    return CurationPolicy(frozenset(suffixes), frozenset(asns))


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
class CurationResult:
    rules: tuple[Rule, ...]
    dropped: tuple[CurationDrop, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "kept_rule_count": len(self.rules),
            "dropped_rule_count": len(self.dropped),
            "dropped": [item.to_dict() for item in self.dropped],
        }


def _drop_reason(rule: Rule, policy: CurationPolicy) -> str | None:
    if rule.category != "ai":
        return None
    if rule.rule_type == "IP-ASN" and rule.value in policy.shared_infra_asns:
        return "shared-infrastructure-asn"
    if (
        rule.rule_type in {"HOST", "HOST-SUFFIX"}
        and rule.value in policy.shared_infra_suffixes
    ):
        return "shared-infrastructure-root-suffix"
    return None


def curate_rules(
    rules: Iterable[Rule],
    *,
    policy: CurationPolicy | None = None,
) -> CurationResult:
    active_policy = policy or load_curation_policy()
    kept: list[Rule] = []
    dropped: list[CurationDrop] = []
    for rule in rules:
        reason = _drop_reason(rule, active_policy)
        if reason is None:
            kept.append(rule)
        else:
            dropped.append(CurationDrop(rule, reason))
    return CurationResult(tuple(kept), tuple(dropped))
