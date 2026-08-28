from __future__ import annotations

from pathlib import Path
from typing import Any

from .model import Source


class ManifestError(ValueError):
    pass


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

    root["sources"] = sources
    return root


def load_manifest(path: str | Path) -> tuple[dict[str, Any], list[Source]]:
    manifest_path = Path(path)
    data = _parse_subset_yaml(manifest_path)
    required_root = {"schema_version", "target", "sources"}
    missing_root = required_root - data.keys()
    if missing_root:
        raise ManifestError(f"missing manifest fields: {', '.join(sorted(missing_root))}")

    sources: list[Source] = []
    seen_ids: set[str] = set()
    seen_urls: set[str] = set()
    required_source = {"id", "kind", "format", "category", "policy", "url", "parser", "enabled"}
    for index, item in enumerate(data["sources"], start=1):
        missing = required_source - item.keys()
        if missing:
            raise ManifestError(f"source {index} missing fields: {', '.join(sorted(missing))}")
        source_id = str(item["id"])
        url = str(item["url"])
        if source_id in seen_ids:
            raise ManifestError(f"duplicate source id: {source_id}")
        if url in seen_urls:
            raise ManifestError(f"duplicate source url: {url}")
        if not url.startswith(("https://", "http://", "inline:")):
            raise ManifestError(f"source {source_id} must use HTTP(S) or inline data: {url}")
        seen_ids.add(source_id)
        seen_urls.add(url)
        sources.append(
            Source(
                id=source_id,
                kind=str(item["kind"]),
                format=str(item["format"]),
                category=str(item["category"]),
                policy=str(item["policy"]),
                url=url,
                parser=str(item["parser"]),
                enabled=bool(item["enabled"]),
                notes=str(item.get("notes", "")),
            )
        )
    return data, sources
