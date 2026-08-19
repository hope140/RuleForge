from __future__ import annotations

import sys
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ruleforge.audit import audit_rules, resolve_conflicts  # noqa: E402
from ruleforge.fetch import FetchError, fetch_source  # noqa: E402
from ruleforge.manifest import load_manifest  # noqa: E402
from ruleforge.model import Source  # noqa: E402
from ruleforge.parsers import parse_resource  # noqa: E402


class RuleForgeTests(unittest.TestCase):
    def test_fetch_retries_transient_network_errors(self) -> None:
        source = Source("test", "filter", "surge", "demo", "direct", "https://example.test", "surge")
        response = Mock()
        response.status = 200
        response.read.return_value = b"DOMAIN,example.com\n"
        response.__enter__ = Mock(return_value=response)
        response.__exit__ = Mock(return_value=False)
        with tempfile.TemporaryDirectory() as temp_dir:
            with patch("ruleforge.fetch.urllib.request.urlopen", side_effect=[urllib.error.URLError("reset"), response]) as urlopen:
                with patch("ruleforge.fetch.time.sleep"):
                    result = fetch_source(source, temp_dir, attempts=3)
            self.assertEqual(result.text, "DOMAIN,example.com\n")
            self.assertEqual(urlopen.call_count, 2)

    def test_fetch_does_not_retry_http_404(self) -> None:
        source = Source("test", "filter", "surge", "demo", "direct", "https://example.test", "surge")
        error = urllib.error.HTTPError(source.url, 404, "Not Found", None, None)
        with tempfile.TemporaryDirectory() as temp_dir:
            with patch("ruleforge.fetch.urllib.request.urlopen", side_effect=error) as urlopen:
                with self.assertRaisesRegex(FetchError, "HTTP 404"):
                    fetch_source(source, temp_dir, attempts=3)
            self.assertEqual(urlopen.call_count, 1)

    def test_manifest_has_unique_seed_sources(self) -> None:
        for filename, target in (("quantumultx.yaml", "quantumult-x"), ("mihomo.yaml", "mihomo")):
            manifest, sources = load_manifest(ROOT / "sources" / filename)
            self.assertEqual(manifest["target"], target)
            self.assertEqual(len(sources), 94)
            self.assertEqual(len({source.id for source in sources}), 94)
            self.assertEqual(len({source.url for source in sources}), 94)

    def test_mihomo_manifest_uses_native_clash_sources(self) -> None:
        _, sources = load_manifest(ROOT / "sources" / "mihomo.yaml")
        blackmatrix = [source for source in sources if source.id.startswith("blackmatrix-")]
        self.assertEqual(len(blackmatrix), 85)
        self.assertTrue(all(source.format == "clash" for source in blackmatrix))
        self.assertTrue(all(source.parser == "clash-classical" for source in blackmatrix))
        self.assertTrue(all("/rule/Clash/" in source.url for source in blackmatrix))
        self.assertTrue(all(source.url.endswith(".yaml") for source in blackmatrix))

    def test_surge_domain_is_rendered_as_quantumultx_host(self) -> None:
        source = Source("test", "filter", "surge", "demo", "direct", "https://example.test", "surge")
        result = parse_resource("DOMAIN-SUFFIX,Example.COM,no-resolve\n", source)
        self.assertEqual(result.issues, ())
        self.assertEqual(result.rules[0].rule_type, "HOST-SUFFIX")
        self.assertEqual(result.rules[0].value, "example.com")
        self.assertEqual(result.rules[0].options, ("no-resolve",))
        self.assertEqual(result.rules[0].to_quantumultx(), "host-suffix,example.com,direct,no-resolve")

    def test_quantumultx_policy_is_replaced_by_manifest_policy(self) -> None:
        source = Source("test", "filter", "quantumult-x", "demo", "AI", "https://example.test", "quantumult-x")
        result = parse_resource("HOST,chat.example.com,OpenAI\n", source)
        self.assertEqual(result.rules[0].policy, "AI")
        self.assertEqual(result.rules[0].options, ())

    def test_inline_source_comments_do_not_enter_rule_values(self) -> None:
        source = Source("test", "filter", "surge", "demo", "reject", "https://example.test", "surge")
        result = parse_resource("DOMAIN,example.com // explanatory note\n", source)
        self.assertEqual(result.issues, ())
        self.assertEqual(result.rules[0].value, "example.com")
        self.assertEqual(result.rules[0].to_quantumultx(), "host,example.com,reject")

    def test_unsupported_source_options_are_not_rendered_for_quantumultx(self) -> None:
        source = Source("test", "filter", "surge", "demo", "AI", "https://example.test", "surge")
        result = parse_resource("DOMAIN-SUFFIX,example.com,extended-matching\n", source)
        self.assertEqual(result.rules[0].options, ("extended-matching",))
        self.assertEqual(result.rules[0].to_quantumultx(), "host-suffix,example.com,AI")

    def test_clash_payload_is_rendered_as_policy_free_mihomo_classical(self) -> None:
        source = Source(
            "blackmatrix-test",
            "filter",
            "clash",
            "ai",
            "AI",
            "https://example.test/rules.yaml",
            "clash-classical",
        )
        result = parse_resource(
            "payload:\n  - DOMAIN,Chat.Example.COM\n  - DOMAIN-SUFFIX,example.org,extended-matching\n",
            source,
        )
        self.assertEqual(result.issues, ())
        self.assertEqual(result.rules[0].to_mihomo(), "DOMAIN,chat.example.com")
        self.assertEqual(result.rules[1].to_mihomo(), "DOMAIN-SUFFIX,example.org")

    def test_mihomo_rejects_user_agent_rules(self) -> None:
        source = Source("test", "filter", "surge", "demo", "AI", "https://example.test", "surge")
        rule = parse_resource("USER-AGENT,Example*\n", source).rules[0]
        with self.assertRaisesRegex(ValueError, "unsupported Mihomo rule type: USER-AGENT"):
            rule.to_mihomo()

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

    def test_blackmatrix_wins_policy_conflict(self) -> None:
        reject = Source("rulego-test", "filter", "surge", "demo", "reject", "https://reject.test", "surge")
        blackmatrix = Source(
            "blackmatrix-test", "filter", "quantumult-x", "demo", "direct", "https://blackmatrix.test", "quantumult-x"
        )
        rejected_rule = parse_resource("DOMAIN,example.com\n", reject).rules[0]
        preferred_rule = parse_resource("HOST,example.com\n", blackmatrix).rules[0]
        audit = audit_rules((rejected_rule, preferred_rule))
        resolution = resolve_conflicts(audit)
        self.assertEqual(len(audit.kept_rules), 2)
        self.assertEqual(len(resolution.preferred_decisions), 1)
        self.assertEqual(len(resolution.unresolved_decisions), 0)
        self.assertEqual(resolution.rules, (preferred_rule,))

    def test_direct_wins_reject_and_specific_rule_wins_broad_rule(self) -> None:
        reject = Source("rulego-reject", "filter", "surge", "demo", "reject", "https://reject.test", "surge")
        direct = Source("rulego-direct", "filter", "surge", "demo", "direct", "https://direct.test", "surge")
        broad = Source("rulego-broad", "filter", "surge", "demo", "全球加速", "https://broad.test", "surge")
        exact_reject = parse_resource("DOMAIN,exact.other.com\n", reject).rules[0]
        exact_direct = parse_resource("DOMAIN,exact.other.com\n", direct).rules[0]
        specific = parse_resource("DOMAIN,specific.example.com\n", direct).rules[0]
        broad_rule = parse_resource("DOMAIN-SUFFIX,example.com\n", broad).rules[0]
        audit = audit_rules((exact_reject, exact_direct, specific, broad_rule))
        resolution = resolve_conflicts(audit)
        self.assertEqual(len(resolution.direct_decisions), 1)
        self.assertEqual(len(resolution.specific_decisions), 1)
        self.assertIn(exact_direct, resolution.rules)
        self.assertIn(specific, resolution.rules)
        self.assertNotIn(exact_reject, resolution.rules)
        self.assertNotIn(broad_rule, resolution.rules)

    def test_business_category_boundaries_are_applied(self) -> None:
        def source(source_id: str, category: str, policy: str) -> Source:
            return Source(source_id, "filter", "quantumult-x", category, policy, "https://example.test", "quantumult-x")

        cases = (
            ("lens.l.google.com", source("blackmatrix-google-voice", "google-voice", "美国节点"), source("blackmatrix-google", "google", "谷歌服务")),
            ("crashlytics.com", source("blackmatrix-apple", "apple", "苹果服务"), source("blackmatrix-google", "google", "谷歌服务")),
            ("deepmind.com", source("blackmatrix-gemini", "ai", "AI"), source("blackmatrix-google", "google", "谷歌服务")),
            ("perplexity.ai", source("rulego-ai", "ai", "AI"), source("rulego-proxy", "proxy", "全球加速")),
            ("smoot.apple.com", source("rulego-ai", "ai", "AI"), source("rulego-proxy", "proxy", "全球加速")),
            ("apple-relay.apple.com", source("rulego-ai", "ai", "AI"), source("rulego-proxy", "proxy", "全球加速")),
            ("apple-relay.cloudflare.com", source("rulego-ai", "ai", "AI"), source("rulego-proxy", "proxy", "全球加速")),
            ("naver.com", source("rulego-media", "global-media", "国际媒体"), source("rulego-proxy", "proxy", "全球加速")),
            ("npmjs.com", source("blackmatrix-github", "github", "GitHub"), source("blackmatrix-npmjs", "developer", "全球加速")),
            ("bilibili.tv", source("blackmatrix-global", "global-media", "国际媒体"), source("blackmatrix-china", "china-streaming", "direct")),
            ("akadns.net", source("blackmatrix-apple", "apple", "苹果服务"), source("blackmatrix-microsoft", "microsoft", "全球加速")),
        )
        rules = []
        for value, left_source, right_source in cases:
            rules.extend(
                (
                    parse_resource(f"HOST,{value}\n", left_source).rules[0],
                    parse_resource(f"HOST,{value}\n", right_source).rules[0],
                )
            )
        resolution = resolve_conflicts(audit_rules(rules))
        selected = {rule.value: rule.policy for rule in resolution.rules}
        self.assertEqual(selected["lens.l.google.com"], "美国节点")
        self.assertEqual(selected["crashlytics.com"], "谷歌服务")
        self.assertEqual(selected["deepmind.com"], "AI")
        self.assertEqual(selected["perplexity.ai"], "AI")
        self.assertEqual(selected["smoot.apple.com"], "AI")
        self.assertEqual(selected["apple-relay.apple.com"], "AI")
        self.assertEqual(selected["apple-relay.cloudflare.com"], "全球加速")
        self.assertEqual(selected["naver.com"], "国际媒体")
        self.assertEqual(selected["npmjs.com"], "全球加速")
        self.assertEqual(selected["bilibili.tv"], "国际媒体")
        self.assertEqual(selected["akadns.net"], "全球加速")

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
            self.assertIn("host,example.com,direct", path.read_text(encoding="utf-8"))

    def test_category_output_is_directly_importable_with_complete_rules(self) -> None:
        from ruleforge.render import render_category_filters

        source = Source("test", "filter", "surge", "ai", "AI", "https://example.test", "surge")
        rules = parse_resource("DOMAIN,example.com\nDOMAIN-SUFFIX,example.org\n", source).rules
        with tempfile.TemporaryDirectory() as temp_dir:
            entries = render_category_filters(rules, Path(temp_dir), relative_prefix="categories")
            self.assertEqual(entries[0]["category"], "ai")
            content = (Path(temp_dir) / "ai.list").read_text(encoding="utf-8")
            self.assertIn("host,example.com,AI\n", content)
            self.assertIn("host-suffix,example.org,AI\n", content)

    def test_mihomo_outputs_preserve_category_order_and_policy_mapping(self) -> None:
        from ruleforge.render import (
            render_mihomo_category_filters,
            render_mihomo_rule_providers,
            render_mihomo_rules,
        )

        reject = Source("reject", "filter", "surge", "reject", "reject", "https://r.test", "surge")
        ai = Source("ai", "filter", "surge", "ai", "AI", "https://a.test", "surge")
        rules = (
            parse_resource("DOMAIN,ai.example\n", ai).rules[0],
            parse_resource("DOMAIN-SUFFIX,ads.example\n", reject).rules[0],
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            entries = render_mihomo_category_filters(
                rules, root / "safe", relative_prefix="outputs/mihomo/categories/safe"
            )
            self.assertEqual([entry["category"] for entry in entries], ["reject", "ai"])
            self.assertIn("DOMAIN,ai.example\n", (root / "safe" / "ai.list").read_text(encoding="utf-8"))
            self.assertNotIn(",AI\n", (root / "safe" / "ai.list").read_text(encoding="utf-8"))
            render_mihomo_rule_providers(entries, root / "providers.yaml", repository_base_url="https://raw.test")
            render_mihomo_rules(entries, root / "rules.yaml")
            providers = (root / "providers.yaml").read_text(encoding="utf-8")
            route_rules = (root / "rules.yaml").read_text(encoding="utf-8")
            self.assertIn("behavior: classical", providers)
            self.assertIn("format: text", providers)
            self.assertLess(route_rules.index("RULE-SET,reject,REJECT"), route_rules.index("RULE-SET,ai,AI"))

    def test_mihomo_profile_references_every_category_and_policy(self) -> None:
        _, sources = load_manifest(ROOT / "sources" / "mihomo.yaml")
        content = (ROOT / "profiles" / "mihomo" / "config.example.yaml").read_text(encoding="utf-8")
        categories = {source.category for source in sources}
        self.assertEqual(len(categories), 26)
        for category in categories:
            self.assertIn(f"  {category}:", content)
            self.assertIn(f"RULE-SET,{category},", content)
        for policy in {source.policy for source in sources} - {"direct", "reject", "proxy"}:
            self.assertIn(f"name: {policy}", content)


if __name__ == "__main__":
    unittest.main()
