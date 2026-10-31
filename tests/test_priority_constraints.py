from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ruleforge.audit import ResolutionResult, RoutingConstraint, audit_rules, resolve_conflicts
from ruleforge.model import Rule
from ruleforge.render import render_mihomo_rules, render_quantumultx_priority_overrides
from ruleforge.routing import order_rules_for_category_providers
from ruleforge.runtime import RouteProbe, simulate_route


class PriorityConstraintTests(unittest.TestCase):
    def rules(self):
        return (
            Rule("ai", "clash", "ai", "AI", "HOST-SUFFIX", "x.ai"),
            Rule("social", "clash", "social", "Social", "HOST", "api.x.ai"),
            Rule("netflix", "clash", "netflix", "Netflix", "HOST-KEYWORD", "x.ai"),
            Rule("privacy", "clash", "privacy", "reject", "HOST", "tracker.example.com"),
        )

    def test_promoted_rules_include_predecessors_in_constraint_order(self):
        ai, social, _, _ = self.rules()
        result = resolve_conflicts(audit_rules(self.rules()))
        self.assertEqual(result.priority_override_rules, (ai, social))
        ordered = order_rules_for_category_providers(
            result.rules, priority_rules=result.priority_override_rules,
        )
        self.assertEqual(simulate_route(ordered, RouteProbe(domain="api.x.ai")).policy, "AI")
        self.assertEqual(simulate_route(ordered, RouteProbe(domain="other.x.ai")).policy, "AI")

    def test_renderers_preserve_resolved_priority_order(self):
        ai, social, _, _ = self.rules()
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "priority.txt"
            render_quantumultx_priority_overrides((ai, social), path)
            rules = [line for line in path.read_text(encoding="utf-8").splitlines() if not line.startswith("#")]
            self.assertEqual(rules, [ai.to_quantumultx(), social.to_quantumultx()])
            render_mihomo_rules([], path, priority_rules=(ai, social))
            rules = path.read_text(encoding="utf-8").splitlines()
            self.assertLess(rules.index("  - DOMAIN-SUFFIX,x.ai,AI"), rules.index("  - DOMAIN,api.x.ai,Social"))

    def test_cyclic_constraints_cannot_be_published_as_resolved(self):
        ai, social, _, _ = self.rules()
        result = ResolutionResult(
            (ai, social), (), frozenset(),
            (RoutingConstraint(ai, social, "first"), RoutingConstraint(social, ai, "second")),
        )
        with self.assertRaisesRegex(ValueError, "cyclic routing constraints"):
            _ = result.priority_override_rules

    def test_business_priority_cannot_cross_the_fixed_security_prefix(self):
        rules = (
            Rule("google", "clash", "google", "Google", "HOST", "googletraveladservices.com"),
            Rule("direct", "clash", "direct-exception", "direct", "HOST-SUFFIX", "googletraveladservices.com"),
            Rule("reject", "clash", "reject", "reject", "HOST-KEYWORD", "adservice"),
        )
        result = resolve_conflicts(audit_rules(rules))
        ordered = order_rules_for_category_providers(
            result.rules, priority_rules=result.priority_override_rules,
        )
        self.assertEqual(simulate_route(ordered, RouteProbe(domain=rules[0].value)).policy, "direct")

    def test_reviewed_microsoft_direct_endpoints_survive_priority_promotion(self):
        for hostname in ("ctldl.windowsupdate.com", "officecdn.microsoft.com", "azuremigrate.download.prss.microsoft.com"):
            with self.subTest(hostname=hostname):
                rules = (
                    Rule("microsoft", "clash", "microsoft", "Microsoft", "HOST", hostname),
                    Rule("direct", "clash", "china-direct", "direct", "HOST-SUFFIX", hostname),
                    Rule("microsoft", "clash", "microsoft", "Microsoft", "HOST-KEYWORD", "microsoft"),
                )
                result = resolve_conflicts(audit_rules(rules))
                ordered = order_rules_for_category_providers(result.rules, priority_rules=result.priority_override_rules)
                self.assertEqual(simulate_route(ordered, RouteProbe(domain=hostname)).policy, "direct")

    def test_microsoft_direct_contract_does_not_expand_a_broad_direct_rule(self):
        for hostname, suffix in (
            ("officecdn.microsoft.com", "microsoft.com"),
            ("login.microsoft.com", "login.microsoft.com"),
            ("unreviewed.download.prss.microsoft.com", "unreviewed.download.prss.microsoft.com"),
        ):
            with self.subTest(hostname=hostname, suffix=suffix):
                rules = (
                    Rule("microsoft", "clash", "microsoft", "Microsoft", "HOST", hostname),
                    Rule("direct", "clash", "china-direct", "direct", "HOST-SUFFIX", suffix),
                )
                result = resolve_conflicts(audit_rules(rules))
                ordered = order_rules_for_category_providers(result.rules, priority_rules=result.priority_override_rules)
                self.assertEqual(simulate_route(ordered, RouteProbe(domain=hostname)).policy, "Microsoft")

    def test_cyclic_build_preserves_existing_output(self):
        from ruleforge.cli import main

        ai, social, _, _ = self.rules()
        result = ResolutionResult(
            (ai, social), (), frozenset(),
            (RoutingConstraint(ai, social, "first"), RoutingConstraint(social, ai, "second")),
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = root / "manifest.yaml"
            manifest.write_text(
                "schema_version: 1\ntarget: quantumult-x\nsources:\n"
                "  - id: local-demo\n    kind: inline\n    format: quantumult-x\n"
                "    category: ai\n    policy: AI\n    url: inline:HOST,example.com\n"
                "    parser: quantumult-x\n    enabled: true\n", encoding="utf-8",
            )
            output = root / "output"
            output.mkdir()
            sentinel = output / "old.list"
            sentinel.write_bytes(b"host,old.example.com,AI\n")
            with patch("ruleforge.cli.resolve_conflicts", return_value=result):
                self.assertEqual(main(["build", "--manifest", str(manifest), "--output-dir", str(output)]), 1)
            self.assertEqual(sentinel.read_bytes(), b"host,old.example.com,AI\n")
            self.assertEqual(list(output.iterdir()), [sentinel])
            self.assertEqual(list(root.glob(".ruleforge-staging-*")), [])


if __name__ == "__main__":
    unittest.main()
