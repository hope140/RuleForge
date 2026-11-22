"""Read-only reporting for refreshed rule outputs."""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
import json
from pathlib import Path


TARGETS = ("quantumult-x", "mihomo")
EXTRA_FILES = {
    "quantumult-x": ("filter_remote.safe.conf", "priority-overrides.safe.list"),
    "mihomo": ("rules.safe.yaml",),
}


@dataclass
class Snapshot:
    sources: dict[str, dict]
    files: dict[str, tuple[str, ...]]
    expected: set[str]


def load_snapshot(directory: Path, target: str) -> Snapshot:
    path = directory / "build.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if data["manifest"]["target"] != target:
            raise ValueError(f"expected {target} build")
        if any(data[key] != 0 for key in ("fetch_error_count", "parse_issue_count", "unresolved_conflict_count")):
            raise ValueError("build reports fetch, parse or unresolved conflict errors")
        sources = {}
        for source in data["sources"]:
            key = source["id"]
            if (not isinstance(key, str) or key in sources
                    or type(source["rule_count"]) is not int or source["rule_count"] < 0
                    or not isinstance(source["sha256"], str)):
                raise ValueError("invalid or duplicate source metadata")
            sources[key] = source
        if not sources or len(sources) != data["enabled_source_count"]:
            raise ValueError("incomplete source metadata")
    except (ValueError, TypeError, KeyError) as exc:
        raise ValueError(f"{path}: {exc}") from exc

    expected = set(EXTRA_FILES[target])
    paths = set(expected)
    for kind in ("candidates", "safe"):
        root = f"categories/{kind}"
        paths.update(p.relative_to(directory).as_posix() for p in (directory / root).glob("*.list"))
        try:
            for category in data[f"{'candidate' if kind == 'candidates' else 'safe'}_categories"]:
                filename = category["filename"]
                if not isinstance(filename, str) or Path(filename).name != filename or not filename.endswith(".list"):
                    raise ValueError("invalid category filename")
                expected.add(f"{root}/{filename}")
        except (TypeError, KeyError) as exc:
            raise ValueError(f"{path}: invalid category metadata") from exc

    files = {}
    for relative in sorted(paths | expected):
        file = directory / relative
        if not file.exists():
            continue  # Compared as absent; never confuses a removed file with an empty file.
        lines = [line.strip() for line in file.read_text(encoding="utf-8-sig").splitlines()]
        files[relative] = tuple(
            line for line in lines
            if line and not line.startswith("#") and line not in {"[filter_remote]", "rules:"}
        )
    return Snapshot(sources, files, expected)


def count_alert(before: int, after: int) -> str:
    if after == 0:
        return "变空（此前有内容）" if before else "空文件"
    if before - after >= 10 and (before - after) * 10 >= before * 3:
        return "骤减"
    return ""


def source_rows(old: Snapshot, new: Snapshot) -> list[str]:
    rows = []
    for key in sorted(old.sources.keys() | new.sources.keys()):
        before, after = old.sources.get(key), new.sources.get(key)
        if before is None:
            rows.append(f"| {key} | 新增 | — → {after['rule_count']} | — → {after['sha256'][:12]} |")
        elif after is None:
            rows.append(f"| {key} | 移除 | {before['rule_count']} → — | {before['sha256'][:12]} → — |")
        else:
            changes = [
                label for field, label in (
                    ("sha256", "内容变化"), ("url", "来源地址变化"),
                    ("resolved_url", "实际地址变化"), ("rule_count", "规则数变化"),
                ) if before.get(field) != after.get(field)
            ]
            if changes:
                a, b = before["rule_count"], after["rule_count"]
                alert = count_alert(a, b)
                if alert:
                    changes.append(alert)
                rows.append(f"| {key} | {'、'.join(changes)} | {a} → {b} | {before['sha256'][:12]} → {after['sha256'][:12]} |")
    return rows


def file_rows(old: Snapshot, new: Snapshot) -> tuple[list[str], list[str]]:
    rows, alerts = [], []
    for name in sorted(old.files.keys() | new.files.keys() | old.expected | new.expected):
        before, after = old.files.get(name), new.files.get(name)
        a, b = Counter(before or ()), Counter(after or ())
        added, removed = sum((b - a).values()), sum((a - b).values())
        alert = ""
        if after is None and (before is not None or name in new.expected):
            alert = "文件缺失"
        elif before is None and name in old.expected:
            alert = "基线文件缺失"
        elif not after:
            alert = count_alert(len(before or ()), 0)
        elif before is not None:
            alert = count_alert(len(before), len(after))
        if alert:
            alerts.append(f"- `{name}`：{alert}")
        if before == after and not alert:
            continue
        if after is None:
            change = "缺失"
        elif before is None:
            change = "新增"
        elif before == after:
            change = "无变化"
        elif not added and not removed:
            change = "只调整顺序"
        else:
            change = "内容变化"
        rows.append(
            f"| `{name}` | {change} | {len(before) if before is not None else '—'} → "
            f"{len(after) if after is not None else '—'} | +{added} / −{removed} | {alert or '—'} |"
        )
    return rows, alerts


def render_target(baseline: Path, candidate: Path, target: str) -> str:
    old = load_snapshot(baseline / target, target)
    new = load_snapshot(candidate / target, target)
    sources = source_rows(old, new)
    files, alerts = file_rows(old, new)
    totals = [
        f"{kind} {sum(len(v) for k, v in old.files.items() if k.startswith(f'categories/{kind}/'))}"
        f" → {sum(len(v) for k, v in new.files.items() if k.startswith(f'categories/{kind}/'))}"
        for kind in ("safe", "candidates")
    ]
    out = [
        f"## {target}", "",
        f"来源 {len(old.sources)} → {len(new.sources)}（{len(sources)} 项变化）；"
        f"分类规则数：{'；'.join(totals)}。", "",
    ]
    if alerts:
        out += ["### 需要检查的文件", "", *alerts, ""]
    out += ["### 上游来源", ""]
    if sources:
        out += ["| 来源 ID | 变化 | 规则数 | SHA256 前 12 位 |", "| --- | --- | --- | --- |", *sources]
    else:
        out.append("没有变化。")
    out += ["", "### 生成文件", ""]
    if files:
        out += ["| 文件 | 变化 | 条目数 | 增删 | 提示 |", "| --- | --- | --- | --- | --- |", *files]
    else:
        out.append("没有变化。")
    return "\n".join(out)
