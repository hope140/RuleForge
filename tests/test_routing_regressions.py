from __future__ import annotations

import itertools
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ruleforge.model import Rule
from ruleforge.routing import order_rules_for_category_providers
from ruleforge.runtime import RouteProbe, simulate_route


class ProviderOrderRegressionTests(unittest.TestCase):
    def test_priorities_follow_all_available_security_providers(self) -> None:
        security = (
            Rule("direct", "clash", "direct-exception", "direct", "HOST-SUFFIX", "blocked.example.com"),
            Rule("reject", "clash", "reject", "reject", "HOST-SUFFIX", "blocked.example.com"),
            Rule("privacy", "clash", "privacy", "reject", "HOST-SUFFIX", "blocked.example.com"),
        )
        broad = Rule("ai", "clash", "ai", "AI", "HOST-SUFFIX", "example.com")
        priority = Rule("google", "clash", "google", "Google", "HOST", "blocked.example.com")
        for count in range(len(security) + 1):
            for selected in itertools.combinations(security, count):
                with self.subTest(categories=[rule.category for rule in selected]):
                    actual = order_rules_for_category_providers(
                        [*selected, broad, priority], priority_rules=[priority],
                    )
                    # The emitted provider retains its rule even when the same
                    # selector also appears in the earlier priority resource.
                    self.assertEqual(actual, (*selected, priority, broad, priority))
                    route = simulate_route(actual, RouteProbe(domain=priority.value))
                    self.assertIsNotNone(route)
                    self.assertEqual(route.policy, selected[0].policy if selected else "Google")

    def test_priority_resource_keeps_the_resolved_constraint_order(self) -> None:
        owner = Rule("ai", "clash", "ai", "AI", "HOST-SUFFIX", "x.ai")
        specific = Rule("social", "clash", "social", "Social", "HOST", "api.x.ai")
        actual = order_rules_for_category_providers(
            [specific, owner], priority_rules=[owner, specific],
        )
        self.assertEqual(actual, (owner, specific, owner, specific))
        route = simulate_route(actual, RouteProbe(domain="api.x.ai"))
        self.assertIsNotNone(route)
        self.assertEqual(route.policy, "AI")


if __name__ == "__main__":
    unittest.main()
