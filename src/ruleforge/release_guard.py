"""Check both staged rule targets before publishing."""
from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path

from .preflight import TARGETS, is_sharp_drop


@dataclass(frozen=True)
class ReleaseCounts:
    sources: dict[str, int]
    safe_categories: dict[str, int]
    declared_categories: set[str]


def load_counts(directory: Path, target: str) -> ReleaseCounts:
    summary = directory / "build.json"
    try:
        data = json.loads(summary.read_text(encoding="utf-8"))
        manifest = data["manifest"]
        if manifest["target"] != target:
            raise ValueError(f"expected a {target} build")
        if any(data[key] != 0 for key in ("fetch_error_count", "parse_issue_count", "unresolved_conflict_count")):
            raise ValueError("build has fetch, parse or unresolved conflict errors")

        enabled = {item["id"]: item["category"] for item in manifest["sources"] if item["enabled"]}
        sources = {item["id"]: item["rule_count"] for item in data["sources"]}
        if (not enabled or enabled.keys() != sources.keys()
                or len(sources) != len(data["sources"]) or len(sources) != data["enabled_source_count"]
                or any(type(count) is not int or count <= 0 for count in sources.values())):
            raise ValueError("source counts disagree with the enabled sources in the manifest")

        safe = directory / "categories" / "safe"
        declared = set(enabled.values())
        categories = {}
        for item in data["safe_categories"]:
            category, count = item["category"], item["rule_count"]
            filename = category + ".list"
            if (Path(filename).name != filename or item["filename"] != filename
                    or category in categories or type(count) is not int or count < 0):
                raise ValueError(f"invalid safe category metadata: {category!r}")
            lines = (safe / filename).read_text(encoding="utf-8-sig").splitlines()
            actual = sum(1 for line in lines if line.strip() and not line.lstrip().startswith("#"))
            if actual != count:
                raise ValueError(f"safe category {category}: build.json has {count}, file has {actual}")
            categories[category] = count

        missing = declared - categories.keys()
        if missing:
            raise ValueError(f"enabled categories missing from safe outputs: {', '.join(sorted(missing))}")
        extra = {path.name for path in safe.glob("*.list")} - {name + ".list" for name in categories}
        if extra:
            raise ValueError(f"unlisted safe files: {', '.join(sorted(extra))}")
        return ReleaseCounts(sources, categories, declared)
    except (KeyError, TypeError, OSError, ValueError) as exc:
        raise ValueError(f"{summary}: {exc}") from exc


def compare_counts(
    label: str, old: dict[str, int], new: dict[str, int], *, removed_by_manifest: set[str]
) -> tuple[list[str], list[str]]:
    notes, failures = [], []
    for name in sorted(old.keys() | new.keys()):
        before, after = old.get(name), new.get(name)
        if before is None:
            notes.append(f"{label} {name}: added (— → {after})")
        elif after is None and name in removed_by_manifest:
            notes.append(f"{label} {name}: removed by candidate manifest ({before} → —)")
        elif after is None:
            failures.append(f"{label} {name}: missing ({before} → —)")
        elif (after == 0 and before > 0) or is_sharp_drop(before, after):
            failures.append(f"{label} {name}: {before} → {after}")
    return notes, failures


def check_release(baseline: Path, candidate: Path) -> int:
    if baseline.resolve() == candidate.resolve():
        print("Release blocked: baseline and candidate must be different directories.")
        return 1
    if not baseline.is_dir():
        print(f"Release blocked: baseline directory is missing: {baseline}")
        return 1

    first_release = not any((baseline / target).exists() for target in TARGETS)
    blocked = False
    print("## RuleForge release rule-count check")
    for target in TARGETS:
        try:
            new = load_counts(candidate / target, target)
            if first_release:
                print(f"- {target}: first generation, candidate counts and safe files verified.")
                continue
            old = load_counts(baseline / target, target)
        except ValueError as exc:
            print(f"- BLOCK {target}: {exc}")
            blocked = True
            continue

        for label, before, after, removed in (
            ("source", old.sources, new.sources, old.sources.keys() - new.sources.keys()),
            ("safe category", old.safe_categories, new.safe_categories,
             old.declared_categories - new.declared_categories),
        ):
            notes, failures = compare_counts(label, before, after, removed_by_manifest=removed)
            for note in notes:
                print(f"- {target} {note}")
            for failure in failures:
                print(f"- BLOCK {target} {failure}")
            blocked |= bool(failures)

    print("\nRelease blocked. Published outputs were preserved." if blocked else "\nRelease rule-count check passed.")
    return int(blocked)
