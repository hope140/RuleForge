from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ruleforge.cli import main
from ruleforge.preflight import EXTRA_FILES, TARGETS, count_alert, render_target


def snapshot(root, target, rows, *, tail="", sources=None):
    directory = root / target
    directory.mkdir(parents=True, exist_ok=True)
    for file in EXTRA_FILES[target]:
        (directory / file).write_text("test,example.org\n", encoding="utf-8")
    category = directory / "categories/safe"
    category.mkdir(parents=True, exist_ok=True)
    if rows is not None:
        (category / "demo.list").write_text(f"# Generated at {tail}\n" + "\n".join(rows), encoding="utf-8")
    meta = sources if sources is not None else [{"id": "a", "sha256": "a" * 64, "rule_count": 10}]
    (directory / "build.json").write_text(json.dumps({
        "manifest": {"target": target}, "fetch_error_count": 0, "parse_issue_count": 0,
        "unresolved_conflict_count": 0, "enabled_source_count": len(meta), "sources": meta,
        "candidate_categories": [], "safe_categories": [{"filename": "demo.list"}],
    }), encoding="utf-8")


class PreflightTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.baseline = self.root / "baseline"
        self.candidate = self.root / "candidate"

    def test_comments_and_cache_metadata_are_not_changes(self):
        target = "quantumult-x"
        snapshot(self.baseline, target, ["HOST,x"], tail="old", sources=[
            {"id": "a", "sha256": "a" * 64, "rule_count": 10, "from_cache": True}])
        snapshot(self.candidate, target, ["HOST,x"], tail="new")
        report = render_target(self.baseline, self.candidate, target)
        self.assertEqual(report.count("没有变化。"), 2)

    def test_changes_include_source_diffs_and_actual_removed_rules(self):
        target = "mihomo"
        snapshot(self.baseline, target, [f"DOMAIN,{i}.test" for i in range(40)], sources=[
            {"id": "a", "sha256": "a" * 64, "rule_count": 40},
            {"id": "removed", "sha256": "b" * 64, "rule_count": 3}])
        snapshot(self.candidate, target, [f"DOMAIN,{i}.test" for i in range(20, 41)], sources=[
            {"id": "a", "sha256": "c" * 64, "rule_count": 21},
            {"id": "added", "sha256": "d" * 64, "rule_count": 2}])
        report = render_target(self.baseline, self.candidate, target)
        self.assertIn("内容变化、规则数变化、骤减", report)
        self.assertIn("| removed | 移除 |", report)
        self.assertIn("| added | 新增 |", report)
        self.assertIn("+1 / −20 | 骤减", report)
        self.assertEqual(count_alert(100, 70), "骤减")
        self.assertEqual(count_alert(20, 11), "")
        self.assertEqual(count_alert(100, 71), "")

    def test_empty_missing_and_order_only_are_distinct(self):
        target = "mihomo"
        snapshot(self.baseline, target, ["DOMAIN,x", "DOMAIN,y"])
        snapshot(self.candidate, target, ["DOMAIN,y", "DOMAIN,x"])
        self.assertIn("只调整顺序", render_target(self.baseline, self.candidate, target))
        file = self.candidate / target / "categories/safe/demo.list"
        file.write_text("# comment only\n", encoding="utf-8")
        self.assertIn("变空（此前有内容）", render_target(self.baseline, self.candidate, target))
        file.unlink()
        self.assertIn("文件缺失", render_target(self.baseline, self.candidate, target))
        (self.baseline / target / "categories/safe/demo.list").unlink()
        self.assertIn("文件缺失", render_target(self.baseline, self.candidate, target))

    def test_default_refresh_uses_private_output_and_reports_failed_build(self):
        for target in TARGETS:
            snapshot(self.baseline, target, ["DOMAIN,x"])
        report = self.root / "report.md"
        baseline_before = {p: p.read_bytes() for p in self.baseline.rglob("*") if p.is_file()}

        def fake_build(command, **kwargs):
            target_dir = Path(command[command.index("--output-dir") + 1])
            self.assertNotIn(self.baseline, target_dir.parents)
            self.assertIn("--refresh", command)
            self.assertIn("--fail-on-conflict", command)
            if target_dir.name == "mihomo":
                return subprocess.CompletedProcess(command, 2, "", "unresolved conflicts")
            snapshot(target_dir.parent, target_dir.name, ["DOMAIN,y"])
            return subprocess.CompletedProcess(command, 0, "", "")

        with patch("ruleforge.cli.subprocess.run", side_effect=fake_build) as runner:
            self.assertEqual(main(["preflight", "--baseline", str(self.baseline), "--report", str(report)]), 1)
        self.assertEqual(runner.call_count, 2)
        data = report.read_text(encoding="utf-8")
        self.assertIn("+1 / −1", data)
        self.assertIn("未生成可比较结果", data)
        self.assertEqual(baseline_before, {p: p.read_bytes() for p in self.baseline.rglob("*") if p.is_file()})

    def test_report_cannot_write_inside_baseline_or_replace_existing_report(self):
        for target in TARGETS:
            snapshot(self.baseline, target, ["DOMAIN,x"])
        args = ["preflight", "--baseline", str(self.baseline), "--candidate", str(self.baseline), "--report"]
        self.assertEqual(main([*args, str(self.baseline / "report.md")]), 1)
        self.assertFalse((self.baseline / "report.md").exists())
        report = self.root / "report.md"
        report.write_text("leave unchanged", encoding="utf-8")
        self.assertEqual(main([*args, str(report)]), 1)
        self.assertEqual(report.read_text(encoding="utf-8"), "leave unchanged")


if __name__ == "__main__":
    unittest.main()
