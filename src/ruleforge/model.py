from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


QUANTUMULTX_OPTIONS = {
    "no-resolve",
    "force-cellular",
    "multi-interface",
    "multi-interface-balance",
}

MIHOMO_TYPE_MAP = {
    "HOST": "DOMAIN",
    "HOST-SUFFIX": "DOMAIN-SUFFIX",
    "HOST-KEYWORD": "DOMAIN-KEYWORD",
    "HOST-WILDCARD": "DOMAIN-WILDCARD",
    "IP6-CIDR": "IP-CIDR6",
    "DEST-PORT": "DST-PORT",
}
MIHOMO_NATIVE_TYPES = {
    "IP-CIDR",
    "IP-ASN",
    "GEOIP",
    "PROCESS-NAME",
    "IN-PORT",
}
MIHOMO_OPTIONS = {"no-resolve", "src"}

# Keep these options in the source model for audit traceability, but do not
# let options discarded by both target renderers hide an otherwise identical
# rule from conflict detection.
AUDIT_IGNORED_OPTIONS = {"extended-matching", "resolve-on-remote", "force-remote"}
LITERAL_IP_RULE_TYPES = {"IP-CIDR", "IP6-CIDR"}


def _semantic_options(rule_type: str, options: tuple[str, ...]) -> tuple[str, ...]:
    result = []
    for option in options:
        name = option.split("=", 1)[0].casefold()
        if name in AUDIT_IGNORED_OPTIONS:
            continue
        # no-resolve does not change matching for a literal IP network.  If it
        # remains in the identity, the same CIDR can be rendered twice with
        # different policies and bypass exact-conflict detection.
        if rule_type in LITERAL_IP_RULE_TYPES and name == "no-resolve":
            continue
        result.append(option)
    return tuple(result)


@dataclass(frozen=True)
class Source:
    id: str
    kind: str
    format: str
    category: str
    policy: str
    url: str
    parser: str
    enabled: bool = True
    notes: str = ""


@dataclass(frozen=True)
class Rule:
    source_id: str
    source_format: str
    category: str
    policy: str
    rule_type: str
    value: str
    options: tuple[str, ...] = field(default_factory=tuple)
    line_number: int = 0
    raw: str = ""

    @property
    def identity_key(self) -> tuple[str, str, tuple[str, ...]]:
        return self.rule_type, self.value, _semantic_options(self.rule_type, self.options)

    @property
    def routed_key(self) -> tuple[str, str]:
        return self.rule_type, self.value

    def to_quantumultx(self, *, include_policy: bool = True) -> str:
        # Keep canonical rule types upper-case internally for parsing and
        # conflict analysis, but emit Quantumult X's native lower-case form.
        fields = [self.rule_type.lower(), self.value]
        if include_policy and self.policy:
            fields.append(self.policy)
        # Surge/Clash sources can carry options that are not accepted by a
        # Quantumult X remote filter resource. Keep only the native options
        # used by this profile; source options remain available in the audit
        # model for traceability.
        fields.extend(
            option
            for option in self.options
            if option.lower() in QUANTUMULTX_OPTIONS or option.lower().startswith("via-interface=")
        )
        return ",".join(fields)

    def to_mihomo(self) -> str:
        """Render a policy-free Mihomo classical rule.

        Policy routing belongs to the profile's ``RULE-SET`` line.  Reject
        unsupported types instead of silently publishing a resource that
        Mihomo cannot use.
        """

        rule_type = MIHOMO_TYPE_MAP.get(self.rule_type)
        if rule_type is None and self.rule_type in MIHOMO_NATIVE_TYPES:
            rule_type = self.rule_type
        if rule_type is None:
            raise ValueError(f"unsupported Mihomo rule type: {self.rule_type}")
        fields = [rule_type, self.value]
        fields.extend(option for option in self.options if option.lower() in MIHOMO_OPTIONS)
        return ",".join(fields)

    def to_dict(self) -> dict[str, Any]:
        return {
            "source_id": self.source_id,
            "source_format": self.source_format,
            "category": self.category,
            "policy": self.policy,
            "rule_type": self.rule_type,
            "value": self.value,
            "options": list(self.options),
            "line_number": self.line_number,
            "raw": self.raw,
        }
