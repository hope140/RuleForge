from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ruleforge.audit import audit_rules  # noqa: E402
from ruleforge.manifest import load_manifest  # noqa: E402
from ruleforge.model import Source  # noqa: E402
from ruleforge.parsers import parse_resource  # noqa: E402


class RuleForgeTests(unittest.TestCase):
    def test_manifest_has_unique_seed_sources(self) -> None:
        _, sources = load_manifest(ROOT / "sources" / "quantumultx.yaml")
        self.assertEqual(len(sources), 25)
        self.assertEqual(len({source.id for source in sources}), 25)
        self.assertEqual(len({source.url for source in sources}), 25)

    def test_surge_domain_is_rendered_as_quantumultx_host(self) -> None:
        source = Source("test", "filter", "surge", "demo", "direct", "https://example.test", "surge")
        result = parse_resource("DOMAIN-SUFFIX,Example.COM,no-resolve\n", source)
        self.assertEqual(result.issues, ())
        self.assertEqual(result.rules[0].rule_type, "HOST-SUFFIX")
        self.assertEqual(result.rules[0].value, "example.com")
        self.assertEqual(result.rules[0].options, ("no-resolve",))
        self.assertEqual(result.rules[0].to_quantumultx(), "HOST-SUFFIX,example.com,direct,no-resolve")

    def test_quantumultx_policy_is_replaced_by_manifest_policy(self) -> None:
        source = Source("test", "filter", "quantumult-x", "demo", "AI", "https://example.test", "quantumult-x")
        result = parse_resource("HOST,chat.example.com,OpenAI\n", source)
        self.assertEqual(result.rules[0].policy, "AI")
        self.assertEqual(result.rules[0].options, ())

    def test_exact_duplicate_and_policy_conflict_are_distinguished(self) -> None:
        direct = Source("direct", "filter", "surge", "demo", "direct", "https://direct.test", "surge")
        proxy = Source("proxy", "filter", "surge", "demo", "proxy", "https://proxy.test", "surge")
        same = parse_resource("DOMAIN,example.com\n", direct).rules[0]
        duplicate = parse_resource("DOMAIN,example.com\n", direct).rules[0]
        conflict = parse_resource("DOMAIN,example.com\n", proxy).rules[0]
        result = audit_rules((same, duplicate, conflict))
        self.assertEqual(len(result.duplicates), 1)
        self.assertEqual(len(result.conflicts), 1)
        self.assertEqual(result.conflicts[0].kind, "exact-policy")

    def test_host_suffix_overlap_is_reported(self) -> None:
        direct = Source("direct", "filter", "surge", "demo", "direct", "https://direct.test", "surge")
        proxy = Source("proxy", "filter", "surge", "demo", "proxy", "https://proxy.test", "surge")
        exact = parse_resource("DOMAIN,login.example.com\n", direct).rules[0]
        suffix = parse_resource("DOMAIN-SUFFIX,example.com\n", proxy).rules[0]
        result = audit_rules((exact, suffix))
        self.assertEqual(len(result.conflicts), 1)
        self.assertEqual(result.conflicts[0].relation, "host-inside-host-suffix")
        self.assertEqual(len(result.safe_rules), 0)

    def test_output_can_be_written_without_external_dependencies(self) -> None:
        from ruleforge.render import render_quantumultx

        source = Source("test", "filter", "surge", "demo", "direct", "https://example.test", "surge")
        rule = parse_resource("DOMAIN,example.com\n", source).rules[0]
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "rules.list"
            render_quantumultx((rule,), path)
            self.assertIn("HOST,example.com,direct", path.read_text(encoding="utf-8"))

    def test_category_output_groups_rules_and_omits_single_policy(self) -> None:
        from ruleforge.render import render_category_filters

        source = Source("test", "filter", "surge", "ai", "AI", "https://example.test", "surge")
        rules = parse_resource("DOMAIN,example.com\nDOMAIN-SUFFIX,example.org\n", source).rules
        with tempfile.TemporaryDirectory() as temp_dir:
            entries = render_category_filters(rules, Path(temp_dir), relative_prefix="categories")
            self.assertEqual(entries[0]["category"], "ai")
            content = (Path(temp_dir) / "ai.list").read_text(encoding="utf-8")
            self.assertIn("HOST,example.com\n", content)
            self.assertNotIn("HOST,example.com,AI", content)


if __name__ == "__main__":
    unittest.main()
