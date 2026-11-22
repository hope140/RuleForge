from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ruleforge.cli import main
from ruleforge.preflight import TARGETS


def snapshot(root, target, sources, categories):
    directory = root / target
    safe = directory / "categories" / "safe"
    safe.mkdir(parents=True)
    (directory / "build.json").write_text(json.dumps({
        "manifest": {
            "target": target,
            "sources": [{"id": name, "category": category, "enabled": True} for name, category in sources],
        },
        "sources": [{"id": name, "rule_count": count} for (name, _), count in sources.items()],
        "enabled_source_count": len(sources),
        "safe_categories": [
            {"category": name, "filename": name + ".list", "rule_count": count}
            for name, count in categories.items()
        ],
        "fetch_error_count": 0,
        "parse_issue_count": 0,
        "unresolved_conflict_count": 0,
    }), encoding="utf-8")
    for name, count in categories.items():
        (safe / (name + ".list")).write_text(
            "# comment\n" + "".join(f"DOMAIN,example{i}.test\n" for i in range(count)),
            encoding="utf-8",
        )


class ReleaseGuardTests(unittest.TestCase):
    def setUp(self):
        scratch = tempfile.TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        self.baseline = Path(scratch.name) / "baseline"
        self.candidate = Path(scratch.name) / "candidate"
        self.baseline.mkdir()

    def check_release(self):
        output = io.StringIO()
        with redirect_stdout(output):
            rc = main(["check-release", "--baseline", str(self.baseline), "--candidate", str(self.candidate)])
        return rc, output.getvalue()

    def test_blocks_source_and_safe_category_drops_across_targets(self):
        for target in TARGETS:
            snapshot(self.baseline, target, {("tracking", "privacy"): 90}, {"privacy": 87})
        snapshot(self.candidate, "quantumult-x", {("tracking", "privacy"): 45}, {"privacy": 87})
        snapshot(self.candidate, "mihomo", {("tracking", "privacy"): 90}, {"privacy": 43})
        rc, output = self.check_release()
        self.assertEqual(rc, 1)
        self.assertIn("BLOCK quantumult-x source tracking: 90 → 45", output)
        self.assertIn("BLOCK mihomo safe category privacy: 87 → 43", output)

    def test_minor_drops_and_explicit_manifest_removal_pass(self):
        for target in TARGETS:
            snapshot(self.baseline, target, {("small", "ai"): 10, ("retired", "cloud"): 80}, {"ai": 10, "cloud": 80})
            snapshot(self.candidate, target, {("small", "ai"): 8, ("new", "privacy"): 2}, {"ai": 8, "privacy": 2})
        rc, output = self.check_release()
        self.assertEqual(rc, 0)
        self.assertIn("source retired: removed by candidate manifest (80 → —)", output)
        self.assertIn("safe category cloud: removed by candidate manifest (80 → —)", output)

    def test_first_generation_and_missing_candidate_file(self):
        for target in TARGETS:
            snapshot(self.candidate, target, {("test", "ai"): 2}, {"ai": 2})
        rc, output = self.check_release()
        self.assertEqual(rc, 0)
        self.assertIn("first generation", output)
        (self.candidate / "mihomo/categories/safe/ai.list").unlink()
        rc, output = self.check_release()
        self.assertEqual(rc, 1)
        self.assertIn("BLOCK mihomo", output)
        self.assertIn("ai.list", output)

    def test_partial_baseline_is_an_error_and_nonempty_category_cannot_vanish(self):
        snapshot(self.baseline, "mihomo", {("tiny", "ai"): 2}, {"ai": 2})
        for target in TARGETS:
            snapshot(self.candidate, target, {("tiny", "ai"): 2}, {"ai": 0})
        rc, output = self.check_release()
        self.assertEqual(rc, 1)
        self.assertIn("BLOCK quantumult-x", output)
        self.assertIn("BLOCK mihomo safe category ai: 2 → 0", output)
