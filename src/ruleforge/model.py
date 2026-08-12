from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


QUANTUMULTX_OPTIONS = {
    "no-resolve",
    "force-cellular",
    "multi-interface",
    "multi-interface-balance",
}


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
        return self.rule_type, self.value, self.options

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
