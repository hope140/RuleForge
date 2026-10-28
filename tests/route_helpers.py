"""Read emitted routing order without applying the generator's sorting logic.

These probes cover explicit domain/IP rules only. GeoSite, GEOIP, process
discovery and DNS resolution require a client/kernel, not this test reader.
"""
from __future__ import annotations

from pathlib import Path
from urllib.parse import urlparse

from ruleforge.model import MIHOMO_OPTIONS, Rule, Source
from ruleforge.parsers import parse_resource


def policy_name(value: str) -> str:
    return {"DIRECT": "direct", "REJECT": "reject", "proxy": "全球加速"}.get(value, value)


def _parse(text: str, category: str, policy: str, target: str) -> list[Rule]:
    source = Source("emitted", "filter", target, category, policy_name(policy), "inline:test", "inline")
    parsed = parse_resource(text, source)
    if parsed.issues:
        raise AssertionError(parsed.issues)
    return list(parsed.rules)


def qx_routes(root: Path, config: Path) -> list[Rule]:
    rules = []
    section = ""
    for line in config.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("["):
            section = line
        if section != "[filter_remote]" or not line.startswith("https://"):
            continue
        url, *fields = (field.strip() for field in line.split(","))
        settings = dict(field.split("=", 1) for field in fields if "=" in field)
        if settings.get("enabled", "true") == "false":
            continue
        relative = urlparse(url).path.split("/outputs/", 1)[1]
        path = root / "outputs" / relative
        for row in path.read_text(encoding="utf-8").splitlines():
            if not row.strip() or row.startswith("#"):
                continue
            policy = settings.get("force-policy", row.split(",")[2])
            rules.extend(_parse(row, path.stem, policy, "quantumult-x"))
    return rules


def mihomo_routes(root: Path, config: Path) -> list[Rule]:
    rules = []
    body = config.read_text(encoding="utf-8").split("\nrules:\n", 1)[1]
    for line in body.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if not line.startswith("- "):
            raise AssertionError(f"unexpected routing content: {line}")
        row = line[2:]
        if row.split(",", 1)[0] in {"GEOSITE", "GEOIP", "MATCH"}:
            continue
        kind, value, policy, *options = row.split(",")
        if policy.casefold() in MIHOMO_OPTIONS:
            raise AssertionError(f"option in policy column: {row}")
        if kind == "RULE-SET":
            text = (root / "outputs/mihomo/categories/safe" / f"{value}.list").read_text(encoding="utf-8")
            rules.extend(_parse(text, value, policy, "clash"))
        else:
            rules.extend(_parse(row, "inline", policy, "clash"))
    return rules


def active_routes(root: Path, target: str, *, profile: bool = False) -> list[Rule]:
    if target == "quantumult-x":
        path = "profiles/quantumult-x/config.example.conf" if profile else "outputs/quantumult-x/filter_remote.safe.conf"
        return qx_routes(root, root / path)
    path = "profiles/mihomo/config.example.yaml" if profile else "outputs/mihomo/rules.safe.yaml"
    return mihomo_routes(root, root / path)
