from __future__ import annotations

import itertools
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ruleforge.audit import audit_rules, resolve_conflicts
from ruleforge.cli import main
from ruleforge.model import Rule


def exact_rule(category: str, policy: str) -> Rule:
    return Rule(category, "clash", category, policy, "HOST", "same.example")


class ExactConflictRegressionTests(unittest.TestCase):
    def test_unique_direct_winner_resolves_lower_priority_disagreement(self) -> None:
        ai = exact_rule("ai", "AI")
        social = exact_rule("social", "Social")
        reject = exact_rule("reject", "reject")
        for rules in itertools.permutations((ai, social, reject)):
            with self.subTest(order=[rule.category for rule in rules]):
                result = resolve_conflicts(audit_rules(rules))
                self.assertEqual(result.rules, (reject,))
                self.assertEqual(result.rejected_rules, frozenset((ai, social)))
                self.assertEqual(result.unresolved_decisions, ())
                superseded = [item for item in result.decisions if item.decision == "superseded-exact"]
                self.assertEqual(len(superseded), 1)
                self.assertEqual(superseded[0].winner, reject)
                self.assertIn("every other", superseded[0].reason)
                self.assertEqual(result.to_summary_dict()["resolved_conflict_count"], 3)

    def test_two_undecided_strong_candidates_remain_unresolved(self) -> None:
        rules = (exact_rule("ai", "AI"), exact_rule("apple", "Apple"), exact_rule("proxy", "Proxy"))
        result = resolve_conflicts(audit_rules(rules))
        self.assertEqual(result.rules, ())
        self.assertEqual(len(result.unresolved_decisions), 1)
        self.assertEqual(result.rejected_rules, frozenset(rules))
        self.assertFalse(any(item.decision == "superseded-exact" for item in result.decisions))

    def test_an_indirect_win_cannot_resolve_or_revive_undecided_candidates(self) -> None:
        # AI beats Microsoft, which beats China Direct. There is no existing
        # AI/China Direct preference, so a transitive guess is not authority.
        rules = (exact_rule("ai", "AI"), exact_rule("microsoft", "Microsoft"), exact_rule("china-direct", "direct"))
        result = resolve_conflicts(audit_rules(rules))
        self.assertEqual(result.rules, ())
        self.assertEqual(len(result.unresolved_decisions), 1)
        self.assertEqual(result.rejected_rules, frozenset(rules))
        self.assertFalse(any(item.decision == "superseded-exact" for item in result.decisions))

    def test_strict_build_accepts_the_unique_exact_winner(self) -> None:
        for target in ("quantumult-x", "mihomo"):
            with self.subTest(target=target), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                manifest = root / "manifest.yaml"
                output = root / "output"
                source_format = "clash" if target == "mihomo" else target
                parser = "inline" if target == "mihomo" else target
                lines = ["schema_version: 1", f"target: {target}", "sources:"]
                for category, policy in (("ai", "AI"), ("social", "Social"), ("reject", "reject")):
                    lines.extend((
                        f"  - id: {category}", "    kind: inline", f"    format: {source_format}",
                        f"    category: {category}", f"    policy: {policy}",
                        f'    url: "inline:HOST,same.example,{policy}"', f"    parser: {parser}", "    enabled: true",
                    ))
                manifest.write_text("\n".join(lines) + "\n", encoding="utf-8")
                result = main([
                    "build", "--manifest", str(manifest), "--output-dir", str(output),
                    "--cache-dir", str(root / "cache"), "--fail-on-conflict",
                ])
                self.assertEqual(result, 0)
                build = json.loads((output / "build.json").read_text(encoding="utf-8"))
                self.assertEqual(build["unresolved_conflict_count"], 0)
                self.assertEqual(build["resolved_rule_count"], 1)
                rows = (output / "categories/safe/reject.list").read_text(encoding="utf-8").splitlines()
                self.assertEqual([row for row in rows if row and not row.startswith("#")],
                                 ["DOMAIN,same.example" if target == "mihomo" else "host,same.example,reject"])


if __name__ == "__main__":
    unittest.main()
