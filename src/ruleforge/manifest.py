from __future__ import annotations

import re
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from .model import Source


class ManifestError(ValueError):
    pass


_ALLOWED_ROOT_FIELDS = {"schema_version", "target", "sources", "description", "notes"}
_ALLOWED_SOURCE_FIELDS = {
    "id",
    "kind",
    "format",
    "category",
    "policy",
    "url",
    "parser",
    "enabled",
    "notes",
    "resolver",
}
_ALLOWED_TARGETS = {"quantumult-x", "mihomo"}
_ALLOWED_COMBINATIONS = {
    ("filter", "surge", "surge"),
    ("filter", "quantumult-x", "quantumult-x"),
    ("filter", "clash", "clash-classical"),
    ("inline", "quantumult-x", "quantumult-x"),
    ("inline", "clash", "inline"),
}


def _scalar(value: str) -> Any:
    value = value.strip()
    if not value:
        return ""
    if (value.startswith("\"") and value.endswith("\"")) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    try:
        return int(value)
    except ValueError:
        return value


def _assign(target: dict[str, Any], text: str, line_number: int) -> None:
    if ":" not in text:
        raise ManifestError(f"line {line_number}: expected key: value")
    key, value = text.split(":", 1)
    key = key.strip()
    if not key:
        raise ManifestError(f"line {line_number}: empty key")
    if key in target:
        raise ManifestError(f"line {line_number}: duplicate field: {key}")
    target[key] = _scalar(value)


def _parse_subset_yaml(path: Path) -> dict[str, Any]:
    """Parse the intentionally small YAML subset used by the source manifest.

    Keeping the seed manifest dependency-free is deliberate. The parser is
    strict and only supports top-level scalars plus a list of flat mappings.
    It is not intended to be a general YAML implementation.
    """

    root: dict[str, Any] = {}
    sources: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    in_sources = False

    for line_number, raw_line in enumerate(
        path.read_text(encoding="utf-8-sig").splitlines(), start=1
    ):
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        stripped = raw_line.strip()
        if stripped == "sources:":
            if indent != 0:
                raise ManifestError(f"line {line_number}: sources must be top-level")
            if "sources" in root:
                raise ManifestError(f"line {line_number}: duplicate field: sources")
            root["sources"] = sources
            in_sources = True
            continue
        if in_sources:
            if stripped.startswith("-"):
                if indent < 2:
                    raise ManifestError(f"line {line_number}: invalid source indentation")
                current = {}
                sources.append(current)
                remainder = stripped[1:].strip()
                if remainder:
                    _assign(current, remainder, line_number)
                continue
            if current is None or indent < 4:
                raise ManifestError(f"line {line_number}: invalid source field")
            _assign(current, stripped, line_number)
            continue
        if indent != 0:
            raise ManifestError(f"line {line_number}: unexpected indentation")
        _assign(root, stripped, line_number)

    return root


def load_manifest(path: str | Path) -> tuple[dict[str, Any], list[Source]]:
    manifest_path = Path(path)
    data = _parse_subset_yaml(manifest_path)
    required_root = {"schema_version", "target", "sources"}
    missing_root = required_root - data.keys()
    if missing_root:
        raise ManifestError(f"missing manifest fields: {', '.join(sorted(missing_root))}")
    unknown_root = set(data) - _ALLOWED_ROOT_FIELDS
    if unknown_root:
        raise ManifestError(f"unknown manifest fields: {', '.join(sorted(unknown_root))}")
    if type(data["schema_version"]) is not int or data["schema_version"] != 1:
        raise ManifestError("schema_version must be integer 1")
    if type(data["target"]) is not str or data["target"] not in _ALLOWED_TARGETS:
        raise ManifestError(f"unsupported target: {data['target']!r}")
    for field in ("description", "notes"):
        if field in data and type(data[field]) is not str:
            raise ManifestError(f"manifest field {field} must be a string")
    if not isinstance(data["sources"], list):
        raise ManifestError("sources must be a list")

    sources: list[Source] = []
    seen_ids: set[str] = set()
    seen_urls: set[str] = set()
    category_policies: dict[str, str] = {}
    required_source = {"id", "kind", "format", "category", "policy", "url", "parser", "enabled"}
    for index, item in enumerate(data["sources"], start=1):
        if not isinstance(item, dict):
            raise ManifestError(f"source {index} must be a mapping")
        unknown = set(item) - _ALLOWED_SOURCE_FIELDS
        if unknown:
            raise ManifestError(f"source {index} has unknown fields: {', '.join(sorted(unknown))}")
        missing = required_source - item.keys()
        if missing:
            raise ManifestError(f"source {index} missing fields: {', '.join(sorted(missing))}")
        for field in ("id", "kind", "format", "category", "policy", "url", "parser"):
            if type(item[field]) is not str:
                raise ManifestError(f"source {index} field {field} must be a string")
        if type(item["enabled"]) is not bool:
            raise ManifestError(f"source {index} field enabled must be a boolean")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", item["category"]):
            raise ManifestError(f"source {index} category must use lowercase kebab-case")
        if not item["policy"].strip() or any(char in item["policy"] for char in ",\r\n"):
            raise ManifestError(f"source {index} policy must be nonempty and contain no commas or newlines")
        if "notes" in item and type(item["notes"]) is not str:
            raise ManifestError(f"source {index} field notes must be a string")
        resolver = item.get("resolver", "")
        if type(resolver) is not str or resolver not in {"", "magicrule"}:
            raise ManifestError(f"source {index} has unsupported resolver: {resolver!r}")
        if resolver == "magicrule":
            client = "QuantumultX" if data["target"] == "quantumult-x" else "Mihomo"
            parts = urlsplit(item["url"])
            expected = ("quantumult-x", "quantumult-x") if client == "QuantumultX" else ("clash", "clash-classical")
            if (item["kind"] != "filter" or (item["format"], item["parser"]) != expected
                    or parts.scheme != "https" or parts.netloc != "magicrule.pages.dev"
                    or parts.path != f"/data/index/{client}.json" or not parts.fragment or parts.query):
                raise ManifestError(f"source {index} has invalid MagicRule index URL or format")
        combination = (item["kind"], item["format"], item["parser"])
        if combination not in _ALLOWED_COMBINATIONS:
            raise ManifestError(
                f"source {index} has unsupported kind/format/parser combination: "
                f"{combination!r}"
            )
        source_id = item["id"]
        url = item["url"]
        if source_id in seen_ids:
            raise ManifestError(f"duplicate source id: {source_id}")
        if url in seen_urls:
            raise ManifestError(f"duplicate source url: {url}")
        if not url.startswith(("https://", "http://", "inline:")):
            raise ManifestError(f"source {source_id} must use HTTP(S) or inline data: {url}")
        seen_ids.add(source_id)
        seen_urls.add(url)
        if item["enabled"]:
            previous_policy = category_policies.get(item["category"])
            if previous_policy is not None and previous_policy != item["policy"]:
                raise ManifestError(
                    f"category {item['category']} has mixed policies: "
                    f"{previous_policy!r} and {item['policy']!r}"
                )
            category_policies[item["category"]] = item["policy"]
        sources.append(
            Source(
                id=source_id,
                kind=item["kind"],
                format=item["format"],
                category=item["category"],
                policy=item["policy"],
                url=url,
                parser=item["parser"],
                enabled=item["enabled"],
                notes=item.get("notes", ""),
                resolver=resolver,
            )
        )
    if not any(source.enabled for source in sources):
        raise ManifestError("manifest must contain at least one enabled source")
    return data, sources
