from __future__ import annotations

from dataclasses import dataclass
import re

from .model import QUANTUMULTX_OPTIONS, Rule, Source


TYPE_MAP = {
    "DOMAIN": "HOST",
    "DOMAIN-SUFFIX": "HOST-SUFFIX",
    "DOMAIN-KEYWORD": "HOST-KEYWORD",
    "DOMAIN-WILDCARD": "HOST-WILDCARD",
    "IP-CIDR6": "IP6-CIDR",
}
KNOWN_TYPES = {
    "HOST",
    "HOST-SUFFIX",
    "HOST-KEYWORD",
    "HOST-WILDCARD",
    "IP-CIDR",
    "IP6-CIDR",
    "IP-ASN",
    "GEOIP",
    "USER-AGENT",
    "PROCESS-NAME",
    "DEST-PORT",
    "IN-PORT",
    "URL-REGEX",
}
KNOWN_OPTIONS = {
    "no-resolve",
    "extended-matching",
    "resolve-on-remote",
    "force-remote",
    "src",
}
COMMENT_PREFIXES = ("#", ";", "//")
INLINE_COMMENT_RE = re.compile(r"\s+(?://|#|;).*$")


@dataclass(frozen=True)
class ParseIssue:
    source_id: str
    line_number: int
    message: str
    raw: str

    def to_dict(self) -> dict[str, object]:
        return {
            "source_id": self.source_id,
            "line_number": self.line_number,
            "message": self.message,
            "raw": self.raw,
        }


@dataclass(frozen=True)
class ParseResult:
    rules: tuple[Rule, ...]
    issues: tuple[ParseIssue, ...]


def _normalize_value(rule_type: str, value: str) -> str:
    value = value.strip()
    if rule_type.startswith("HOST"):
        value = value.lower().rstrip(".")
    return value


def _options(source: Source, parts: list[str]) -> tuple[str, ...]:
    extras = [item.strip() for item in parts[2:] if item.strip()]
    if source.format.lower() in {"surge", "clash", "mihomo"}:
        # Surge commonly appends a policy as the third field.  The manifest
        # policy is the authoritative routing policy, so target policy names
        # must not become part of rule identity and hide exact conflicts.
        supported = KNOWN_OPTIONS | {item.casefold() for item in QUANTUMULTX_OPTIONS}
        return tuple(
            item
            for item in extras
            if item.split("=", 1)[0].casefold() in supported
            or item.casefold().startswith("via-interface=")
        )
    return tuple(item for item in extras if item.lower() in KNOWN_OPTIONS)


def _unwrap_clash_payload(raw: str, source: Source) -> str | None:
    if source.parser.lower() not in {"clash", "mihomo", "clash-classical"}:
        return raw
    if raw == "payload:":
        return None
    if raw.startswith("-"):
        raw = raw[1:].strip()
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in {"'", '"'}:
        raw = raw[1:-1].strip()
    return raw


def parse_resource(text: str, source: Source) -> ParseResult:
    rules: list[Rule] = []
    issues: list[ParseIssue] = []
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        raw = raw_line.strip()
        if not raw or raw.startswith(COMMENT_PREFIXES):
            continue
        raw = _unwrap_clash_payload(raw, source)
        if raw is None:
            continue
        stripped = INLINE_COMMENT_RE.sub("", raw).strip()
        if not stripped:
            continue
        parts = [part.strip() for part in stripped.split(",")]
        if len(parts) < 2:
            issues.append(ParseIssue(source.id, line_number, "expected comma-separated rule", stripped))
            continue
        original_type = parts[0].upper()
        rule_type = TYPE_MAP.get(original_type, original_type)
        if rule_type not in KNOWN_TYPES:
            issues.append(ParseIssue(source.id, line_number, f"unsupported rule type: {original_type}", stripped))
            continue
        value = _normalize_value(rule_type, parts[1])
        if not value:
            issues.append(ParseIssue(source.id, line_number, "empty rule value", stripped))
            continue
        rules.append(
            Rule(
                source_id=source.id,
                source_format=source.format,
                category=source.category,
                policy=source.policy,
                rule_type=rule_type,
                value=value,
                options=_options(source, parts),
                line_number=line_number,
                raw=raw,
            )
        )
    return ParseResult(tuple(rules), tuple(issues))
