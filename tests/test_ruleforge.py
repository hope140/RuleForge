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
from ruleforge.curation import curate_rules  # noqa: E402
from ruleforge.fetch import FetchError, fetch_source  # noqa: E402
from ruleforge.manifest import ManifestError, load_manifest  # noqa: E402
from ruleforge.model import Source  # noqa: E402
from ruleforge.parsers import parse_resource  # noqa: E402
from ruleforge.preview import build_priority_preview, conflict_probe  # noqa: E402
from ruleforge.routing import ROUTING_CATEGORY_ORDER, routing_order_violations  # noqa: E402
from ruleforge.runtime import RouteProbe, rule_matches, simulate_first_match  # noqa: E402


class RuleForgeTests(unittest.TestCase):
    def _write_inline_manifest(self, path: Path, payload: str = "HOST,example.com") -> None:
        path.write_text(
            "\n".join(
                (
                    "schema_version: 1",
                    "target: quantumult-x",
                    "sources:",
                    "  - id: inline-test",
                    "    kind: inline",
                    "    format: quantumult-x",
                    "    category: demo",
                    "    policy: direct",
                    f'    url: "inline:{payload}"',
                    "    parser: quantumult-x",
                    "    enabled: true",
                    "",
                )
            ),
            encoding="utf-8",
        )

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

    def test_empty_source_fails_without_replacing_existing_output(self) -> None:
        from ruleforge.cli import main

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = root / "manifest.yaml"
            output = root / "output"
            output.mkdir()
            sentinel = output / "sentinel.txt"
            sentinel.write_text("original\n", encoding="utf-8")
            self._write_inline_manifest(manifest, "# comments only")

            result = main(
                [
                    "build",
                    "--manifest",
                    str(manifest),
                    "--output-dir",
                    str(output),
                ]
            )

            self.assertEqual(result, 1)
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "original\n")
            self.assertFalse((output / "build.json").exists())
            self.assertEqual(list(root.glob(".ruleforge-staging-*")), [])

    def test_render_failure_keeps_existing_output_and_cleans_staging(self) -> None:
        from ruleforge.cli import main

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = root / "manifest.yaml"
            output = root / "output"
            output.mkdir()
            sentinel = output / "sentinel.txt"
            sentinel.write_text("original\n", encoding="utf-8")
            self._write_inline_manifest(manifest)

            with patch("ruleforge.cli.render_json", side_effect=OSError("render failed")):
                result = main(
                    [
                        "build",
                        "--manifest",
                        str(manifest),
                        "--output-dir",
                        str(output),
                    ]
                )

            self.assertEqual(result, 1)
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "original\n")
            self.assertFalse((output / "build.json").exists())
            self.assertEqual(list(root.glob(".ruleforge-staging-*")), [])
            self.assertEqual(list(root.glob(".ruleforge-backup-*")), [])

    def test_successful_build_publishes_staged_output(self) -> None:
        from ruleforge.cli import main

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = root / "manifest.yaml"
            output = root / "output"
            output.mkdir()
            sentinel = output / "sentinel.txt"
            sentinel.write_text("preserved\n", encoding="utf-8")
            self._write_inline_manifest(manifest)

            result = main(
                [
                    "build",
                    "--manifest",
                    str(manifest),
                    "--output-dir",
                    str(output),
                ]
            )

            self.assertEqual(result, 0)
            self.assertTrue((output / "build.json").is_file())
            self.assertTrue((output / "priority-preview.json").is_file())
            self.assertTrue((output / "priority-preview.md").is_file())
            self.assertTrue((output / "categories" / "safe" / "demo.list").is_file())
            import json

            preview = json.loads((output / "priority-preview.json").read_text(encoding="utf-8"))
            self.assertEqual(preview["mode"], "preview-only")
            self.assertFalse(preview["active"])
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "preserved\n")
            self.assertEqual(list(root.glob(".ruleforge-staging-*")), [])
            self.assertEqual(list(root.glob(".ruleforge-backup-*")), [])

    def test_manifest_has_unique_seed_sources(self) -> None:
        expected_counts = {"quantumultx.yaml": 96, "mihomo.yaml": 95}
        for filename, target in (("quantumultx.yaml", "quantumult-x"), ("mihomo.yaml", "mihomo")):
            manifest, sources = load_manifest(ROOT / "sources" / filename)
            self.assertEqual(manifest["target"], target)
            self.assertEqual(len(sources), expected_counts[filename])
            self.assertEqual(len({source.id for source in sources}), expected_counts[filename])
            self.assertEqual(len({source.url for source in sources}), expected_counts[filename])

    def test_manifest_rejects_invalid_root_schema_target_and_unknown_fields(self) -> None:
        base = """schema_version: 1
target: quantumult-x
description: test
sources:
  - id: demo
    kind: filter
    format: surge
    category: demo
    policy: direct
    url: https://example.test/rules.list
    parser: surge
    enabled: true
"""
        cases = (
            ("schema_version: 2", "schema_version must be integer 1"),
            ("schema_version: \"1\"", "schema_version must be integer 1"),
            ("target: unknown", "unsupported target"),
            ("unexpected: value", "unknown manifest fields"),
            ("    unexpected: value", "source 1 has unknown fields"),
        )
        for replacement, message in cases:
            with self.subTest(replacement=replacement), tempfile.TemporaryDirectory() as temp_dir:
                text = base.replace("schema_version: 1", replacement, 1)
                if replacement.startswith("    "):
                    text = base.replace("    enabled: true", "    enabled: true\n" + replacement, 1)
                elif replacement.startswith("unexpected:"):
                    text = base.replace("description: test", "description: test\n" + replacement, 1)
                elif replacement.startswith("target:"):
                    text = base.replace("target: quantumult-x", replacement, 1)
                path = Path(temp_dir) / "manifest.yaml"
                path.write_text(text, encoding="utf-8")
                with self.assertRaisesRegex(ManifestError, message):
                    load_manifest(path)

    def test_manifest_rejects_string_booleans_and_non_string_source_fields(self) -> None:
        base = """schema_version: 1
target: quantumult-x
sources:
  - id: demo
    kind: filter
    format: surge
    category: demo
    policy: direct
    url: https://example.test/rules.list
    parser: surge
    enabled: true
"""
        for field, value in (("enabled", '"false"'), ("enabled", 1), ("id", 1), ("url", 1)):
            with self.subTest(field=field, value=value), tempfile.TemporaryDirectory() as temp_dir:
                original = (
                    f"  - id: demo" if field == "id" else
                    f"    {field}: " + ("true" if field == "enabled" else "https://example.test/rules.list")
                )
                replacement = f"  - id: {value}" if field == "id" else f"    {field}: {value}"
                text = base.replace(original, replacement, 1)
                path = Path(temp_dir) / "manifest.yaml"
                path.write_text(text, encoding="utf-8")
                with self.assertRaisesRegex(ManifestError, f"field {field} .*string|field {field} .*boolean"):
                    load_manifest(path)

    def test_manifest_accepts_documented_notes_and_current_combinations(self) -> None:
        for filename in ("quantumultx.yaml", "mihomo.yaml"):
            manifest, sources = load_manifest(ROOT / "sources" / filename)
            self.assertIn("description", manifest)
            self.assertTrue(sources)

    def test_manifest_rejects_unknown_source_combination(self) -> None:
        text = """schema_version: 1
target: quantumult-x
sources:
  - id: demo
    kind: filter
    format: clash
    category: demo
    policy: direct
    url: https://example.test/rules.yaml
    parser: surge
    enabled: true
"""
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "manifest.yaml"
            path.write_text(text, encoding="utf-8")
            with self.assertRaisesRegex(ManifestError, "unsupported kind/format/parser combination"):
                load_manifest(path)

    def test_inline_source_is_local_and_does_not_require_network(self) -> None:
        source = Source(
            "local-apple-cma2",
            "inline",
            "quantumult-x",
            "apple",
            "苹果服务",
            "inline:HOST,cma2.itunes.apple.com",
            "quantumult-x",
        )
        resource = fetch_source(source, "unused-cache", offline=True)
        self.assertTrue(resource.from_cache)
        self.assertEqual(resource.text, "HOST,cma2.itunes.apple.com")

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

    def test_target_ignored_options_do_not_hide_policy_conflicts(self) -> None:
        ai = Source("rulego-ai", "filter", "surge", "ai", "AI", "https://ai.test", "surge")
        tiktok = Source(
            "blackmatrix-tiktok",
            "filter",
            "clash",
            "tiktok",
            "海外抖音",
            "https://tiktok.test",
            "clash-classical",
        )
        ai_rule = parse_resource(
            "DOMAIN-SUFFIX,byteoversea.com,extended-matching\n", ai
        ).rules[0]
        tiktok_rule = parse_resource("DOMAIN-SUFFIX,byteoversea.com\n", tiktok).rules[0]

        audit = audit_rules((ai_rule, tiktok_rule))
        resolution = resolve_conflicts(audit)

        self.assertEqual(len(audit.conflicts), 1)
        self.assertEqual(resolution.rules, (tiktok_rule,))

    def test_keyword_overlap_uses_business_category_precedence(self) -> None:
        google = Source(
            "blackmatrix-google",
            "filter",
            "clash",
            "google",
            "谷歌服务",
            "https://google.test",
            "clash-classical",
        )
        youtube = Source(
            "blackmatrix-youtube",
            "filter",
            "clash",
            "youtube",
            "YouTube",
            "https://youtube.test",
            "clash-classical",
        )
        broad = parse_resource("DOMAIN-KEYWORD,google\n", google).rules[0]
        specific = parse_resource("DOMAIN-SUFFIX,googlevideo.com\n", youtube).rules[0]

        audit = audit_rules((broad, specific))
        resolution = resolve_conflicts(audit)

        self.assertEqual(audit.conflicts[0].relation, "host-keyword-overlap")
        self.assertEqual(resolution.rules, (broad, specific))
        self.assertEqual(len(resolution.ordered_overlap_decisions), 1)

    def test_reject_precedes_a_broader_keyword_overlap(self) -> None:
        reject = Source("rulego-reject", "filter", "surge", "reject", "reject", "https://reject.test", "surge")
        google = Source(
            "blackmatrix-google",
            "filter",
            "clash",
            "google",
            "谷歌服务",
            "https://google.test",
            "clash-classical",
        )
        broad = parse_resource("DOMAIN-KEYWORD,adservice\n", reject).rules[0]
        specific = parse_resource("DOMAIN-SUFFIX,googleadservices.com\n", google).rules[0]

        resolution = resolve_conflicts(audit_rules((broad, specific)))

        self.assertEqual(resolution.rules, (broad, specific))
        self.assertEqual(len(resolution.ordered_overlap_decisions), 1)

    def test_china_media_wins_exact_conflict_with_global_media(self) -> None:
        china_media = Source(
            "rulego-china-media",
            "filter",
            "surge",
            "china-media",
            "港台番剧",
            "https://china-media.test",
            "surge",
        )
        global_media = Source(
            "blackmatrix-global-media-asian",
            "filter",
            "clash",
            "global-media",
            "国际媒体",
            "https://global-media.test",
            "clash-classical",
        )
        cn_rule = parse_resource("DOMAIN,www.bilibili.com\n", china_media).rules[0]
        global_rule = parse_resource("DOMAIN,www.bilibili.com\n", global_media).rules[0]

        resolution = resolve_conflicts(audit_rules((cn_rule, global_rule)))

        self.assertEqual(resolution.rules, (cn_rule,))

    def test_ip_cidr_overlap_prefers_narrower_business_rule(self) -> None:
        social = Source(
            "blackmatrix-social",
            "filter",
            "clash",
            "social",
            "全球加速",
            "https://social.test",
            "clash-classical",
        )
        netflix = Source(
            "blackmatrix-netflix",
            "filter",
            "clash",
            "netflix",
            "Netflix",
            "https://netflix.test",
            "clash-classical",
        )
        broad = parse_resource("IP-CIDR,34.224.0.0/12\n", social).rules[0]
        specific = parse_resource("IP-CIDR,34.226.14.0/24\n", netflix).rules[0]

        audit = audit_rules((broad, specific))
        resolution = resolve_conflicts(audit)

        self.assertEqual(audit.conflicts[0].relation, "ip-cidr-overlap")
        self.assertEqual(resolution.rules, (broad, specific))
        self.assertEqual(len(resolution.ordered_overlap_decisions), 1)

    def test_reject_beats_blackmatrix_for_an_exact_policy_conflict(self) -> None:
        reject = Source("rulego-test", "filter", "surge", "demo", "reject", "https://reject.test", "surge")
        blackmatrix = Source(
            "blackmatrix-test", "filter", "quantumult-x", "demo", "direct", "https://blackmatrix.test", "quantumult-x"
        )
        rejected_rule = parse_resource("DOMAIN,example.com\n", reject).rules[0]
        preferred_rule = parse_resource("HOST,example.com\n", blackmatrix).rules[0]
        audit = audit_rules((rejected_rule, preferred_rule))
        resolution = resolve_conflicts(audit)
        self.assertEqual(len(audit.kept_rules), 2)
        self.assertEqual(len(resolution.protective_reject_decisions), 1)
        self.assertEqual(len(resolution.unresolved_decisions), 0)
        self.assertEqual(resolution.rules, (rejected_rule,))

    def test_reject_beats_normal_direct_and_semantic_overlap_is_retained(self) -> None:
        reject = Source("rulego-reject", "filter", "surge", "demo", "reject", "https://reject.test", "surge")
        direct = Source("rulego-direct", "filter", "surge", "demo", "direct", "https://direct.test", "surge")
        broad = Source("rulego-broad", "filter", "surge", "demo", "全球加速", "https://broad.test", "surge")
        exact_reject = parse_resource("DOMAIN,exact.other.com\n", reject).rules[0]
        exact_direct = parse_resource("DOMAIN,exact.other.com\n", direct).rules[0]
        specific = parse_resource("DOMAIN,specific.example.com\n", direct).rules[0]
        broad_rule = parse_resource("DOMAIN-SUFFIX,example.com\n", broad).rules[0]
        audit = audit_rules((exact_reject, exact_direct, specific, broad_rule))
        resolution = resolve_conflicts(audit)
        self.assertEqual(len(resolution.direct_decisions), 0)
        self.assertEqual(len(resolution.protective_reject_decisions), 1)
        self.assertEqual(len(resolution.ordered_overlap_decisions), 1)
        self.assertIn(exact_reject, resolution.rules)
        self.assertNotIn(exact_direct, resolution.rules)
        self.assertIn(specific, resolution.rules)
        self.assertIn(broad_rule, resolution.rules)

    def test_direct_exception_can_override_reject(self) -> None:
        reject = Source("reject", "filter", "surge", "reject", "reject", "https://reject.test", "surge")
        exception = Source(
            "exception",
            "filter",
            "surge",
            "direct-exception",
            "direct",
            "https://exception.test",
            "surge",
        )
        rejected_rule = parse_resource("DOMAIN,example.com\n", reject).rules[0]
        exception_rule = parse_resource("DOMAIN,example.com\n", exception).rules[0]

        resolution = resolve_conflicts(audit_rules((rejected_rule, exception_rule)))

        self.assertEqual(resolution.rules, (exception_rule,))
        self.assertEqual(resolution.decisions[0].decision, "prefer-direct-exception")

    def test_surged_policy_field_does_not_hide_an_exact_conflict(self) -> None:
        direct = Source("direct", "filter", "surge", "demo", "direct", "https://direct.test", "surge")
        reject = Source("reject", "filter", "surge", "demo", "reject", "https://reject.test", "surge")
        direct_rule = parse_resource("DOMAIN,example.com,direct\n", direct).rules[0]
        reject_rule = parse_resource("DOMAIN,example.com,reject\n", reject).rules[0]

        audit = audit_rules((direct_rule, reject_rule))
        resolution = resolve_conflicts(audit)

        self.assertEqual(direct_rule.options, ())
        self.assertEqual(reject_rule.options, ())
        self.assertEqual(len(audit.conflicts), 1)
        self.assertEqual(resolution.rules, (reject_rule,))

    def test_option_order_does_not_hide_an_exact_duplicate(self) -> None:
        source = Source("source", "filter", "surge", "demo", "direct", "https://source.test", "surge")
        first = parse_resource("DOMAIN,example.com,no-resolve,extended-matching\n", source).rules[0]
        second = parse_resource("DOMAIN,example.com,extended-matching,no-resolve\n", source).rules[0]

        audit = audit_rules((first, second))

        self.assertEqual(len(audit.duplicates), 1)
        self.assertEqual(len(audit.conflicts), 0)

    def test_semantic_overlap_keeps_the_broad_rule_for_other_hosts(self) -> None:
        direct = Source("direct", "filter", "surge", "china-direct", "direct", "https://direct.test", "surge")
        proxy = Source("proxy", "filter", "surge", "proxy", "proxy", "https://proxy.test", "surge")
        broad = parse_resource("DOMAIN-SUFFIX,example.com\n", direct).rules[0]
        specific = parse_resource("DOMAIN,foo.example.com\n", proxy).rules[0]

        resolution = resolve_conflicts(audit_rules((broad, specific)))

        self.assertEqual(resolution.rules, (broad, specific))
        self.assertEqual(resolution.constraints[0].before, specific)
        self.assertEqual(resolution.constraints[0].after, broad)

    def test_ai_curation_drops_shared_infrastructure_but_keeps_explicit_endpoints(self) -> None:
        ai = Source("blackmatrix-openai", "filter", "clash", "ai", "AI", "https://ai.test", "clash-classical")
        rules = parse_resource(
            "IP-ASN,20473\nDOMAIN-SUFFIX,stripe.com\nDOMAIN-SUFFIX,openai.com\nDOMAIN,anthropic.auth0.com\n",
            ai,
        ).rules

        result = curate_rules(rules)

        self.assertEqual(
            {(rule.rule_type, rule.value) for rule in result.rules},
            {("HOST-SUFFIX", "openai.com"), ("HOST", "anthropic.auth0.com")},
        )
        self.assertEqual(
            {drop.reason for drop in result.dropped},
            {"shared-infrastructure-asn", "shared-infrastructure-root-suffix"},
        )

    def test_routing_category_order_satisfies_declared_constraints(self) -> None:
        self.assertEqual(routing_order_violations(), ())

    def test_mihomo_profile_uses_the_shared_routing_category_order(self) -> None:
        content = (ROOT / "profiles" / "mihomo" / "config.example.yaml").read_text(encoding="utf-8")
        positions = [content.index(f"RULE-SET,{category},") for category in ROUTING_CATEGORY_ORDER]
        self.assertEqual(positions, sorted(positions))

    def test_runtime_route_probes_cover_openai_and_reject_boundaries(self) -> None:
        ai = Source("ai", "filter", "quantumult-x", "ai", "AI", "https://ai.test", "quantumult-x")
        reject = Source("reject", "filter", "surge", "reject", "reject", "https://reject.test", "surge")
        direct = Source("direct", "filter", "surge", "china-direct", "direct", "https://direct.test", "surge")
        exception = Source(
            "exception",
            "filter",
            "surge",
            "direct-exception",
            "direct",
            "https://exception.test",
            "surge",
        )
        rules = tuple(
            rule
            for source, text in (
                (ai, "HOST-SUFFIX,openai.com\nHOST-SUFFIX,oaistatsig.com\n"),
                (reject, "HOST-SUFFIX,example.com\n"),
                (direct, "HOST-SUFFIX,example.net\n"),
                (exception, "HOST,allow.example.com\n"),
            )
            for rule in parse_resource(text, source).rules
        )

        self.assertEqual(simulate_first_match(rules, RouteProbe(domain="auth.openai.com")).policy, "AI")
        self.assertEqual(simulate_first_match(rules, RouteProbe(domain="api.oaistatsig.com")).policy, "AI")
        self.assertEqual(simulate_first_match(rules, RouteProbe(domain="ad.example.com")).policy, "reject")
        self.assertEqual(simulate_first_match(rules, RouteProbe(domain="www.example.net")).policy, "direct")
        self.assertEqual(simulate_first_match(rules, RouteProbe(domain="allow.example.com")).policy, "direct")

    def test_priority_preview_finds_a_live_cross_category_route_change(self) -> None:
        ai = Source(
            "rulego-ai-supplement",
            "filter",
            "surge",
            "ai",
            "AI",
            "https://ai.test",
            "surge",
        )
        apple = Source(
            "blackmatrix-apple",
            "filter",
            "quantumult-x",
            "apple",
            "苹果服务",
            "https://apple.test",
            "quantumult-x",
        )
        broad = parse_resource("HOST-SUFFIX,smoot.apple.com\n", ai).rules[0]
        exact = parse_resource("HOST,api.smoot.apple.com\n", apple).rules[0]

        preview = build_priority_preview(
            resolve_conflicts(audit_rules((broad, exact))),
            target="quantumult-x",
        )

        self.assertEqual(preview.live_cross_category_count, 1)
        self.assertEqual(preview.status_counts["preview-candidate"], 2)
        self.assertEqual(len(preview.candidate_rules), 1)
        self.assertEqual(preview.candidate_rules[0].rule_type, "HOST-SUFFIX")
        self.assertEqual(preview.candidate_rules[0].value, "smoot.apple.com")
        self.assertEqual(preview.candidate_rules[0].policy, "苹果服务")
        item = preview.items[0]
        self.assertEqual(item.probe.domain, "api.smoot.apple.com")
        self.assertEqual(item.expected_rule.policy, "苹果服务")
        self.assertEqual(item.actual_rule.policy, "AI")
        self.assertEqual(item.method, "apple-service-contract")
        self.assertEqual(item.confidence, "high")

    def test_priority_preview_ignores_constraints_for_rejected_rules(self) -> None:
        ai = Source(
            "rulego-ai-supplement",
            "filter",
            "surge",
            "ai",
            "AI",
            "https://ai.test",
            "surge",
        )
        apple = Source(
            "blackmatrix-apple",
            "filter",
            "quantumult-x",
            "apple",
            "苹果服务",
            "https://apple.test",
            "quantumult-x",
        )
        google = Source(
            "blackmatrix-google",
            "filter",
            "quantumult-x",
            "google",
            "谷歌服务",
            "https://google.test",
            "quantumult-x",
        )
        rules = (
            parse_resource("HOST-SUFFIX,smoot.apple.com\n", ai).rules[0],
            parse_resource("HOST,api.smoot.apple.com\n", apple).rules[0],
            parse_resource("HOST,api.smoot.apple.com\n", google).rules[0],
        )

        preview = build_priority_preview(
            resolve_conflicts(audit_rules(rules)),
            target="quantumult-x",
        )

        self.assertGreaterEqual(preview.discarded_overlap_count, 1)
        self.assertTrue(
            all(rule.source_id != "blackmatrix-apple" for rule in preview.candidate_rules)
        )

    def test_priority_preview_does_not_treat_a_third_rule_as_authorized(self) -> None:
        ai = Source(
            "rulego-ai-supplement",
            "filter",
            "surge",
            "ai",
            "AI",
            "https://ai.test",
            "surge",
        )
        apple = Source(
            "blackmatrix-apple",
            "filter",
            "quantumult-x",
            "apple",
            "苹果服务",
            "https://apple.test",
            "quantumult-x",
        )
        direct = Source(
            "blackmatrix-direct",
            "filter",
            "quantumult-x",
            "china-direct",
            "direct",
            "https://direct.test",
            "quantumult-x",
        )
        broad_ai = parse_resource("HOST-SUFFIX,gateway.icloud.com\n", ai).rules[0]
        exact_apple = parse_resource("HOST,gateway.icloud.com\n", apple).rules[0]
        keyword_direct = parse_resource("HOST-KEYWORD,icloud.com\n", direct).rules[0]

        preview = build_priority_preview(
            resolve_conflicts(audit_rules((broad_ai, exact_apple, keyword_direct))),
            target="quantumult-x",
        )

        self.assertEqual(len(preview.candidate_rules), 1)
        self.assertEqual(preview.candidate_rules[0].rule_type, "HOST-SUFFIX")
        self.assertEqual(preview.candidate_rules[0].value, "icloud.com")
        evidence = [item for item in preview.items if item.expected_rule == exact_apple]
        self.assertEqual({item.status for item in evidence}, {"preview-candidate", "review-required"})
        self.assertIn(
            "third-rule-interference",
            {item.disposition_reason for item in evidence},
        )
        candidate = preview.to_dict()["override_candidates"][0]
        self.assertEqual(candidate["confidence"], "high")

    def test_priority_preview_builds_a_cidr_witness(self) -> None:
        social = Source(
            "blackmatrix-social",
            "filter",
            "clash",
            "social",
            "全球加速",
            "https://social.test",
            "clash-classical",
        )
        netflix = Source(
            "blackmatrix-netflix",
            "filter",
            "clash",
            "netflix",
            "Netflix",
            "https://netflix.test",
            "clash-classical",
        )
        broad = parse_resource("IP-CIDR,34.224.0.0/12\n", social).rules[0]
        narrow = parse_resource("IP-CIDR,34.226.14.0/24\n", netflix).rules[0]
        conflict = audit_rules((broad, narrow)).conflicts[0]

        probe = conflict_probe(conflict)

        self.assertIsNotNone(probe)
        self.assertEqual(probe.ip, "34.226.14.0")
        self.assertTrue(all(rule_matches(rule, probe) for rule in (broad, narrow)))

    def test_priority_preview_keeps_active_apple_policy_over_global_media(self) -> None:
        apple = Source(
            "blackmatrix-apple",
            "filter",
            "quantumult-x",
            "apple",
            "苹果服务",
            "https://apple.test",
            "quantumult-x",
        )
        media = Source(
            "rulego-global-media",
            "filter",
            "surge",
            "global-media",
            "国际媒体",
            "https://media.test",
            "surge",
        )
        apple_rule = parse_resource("HOST-SUFFIX,tv.apple.com\n", apple).rules[0]
        media_rule = parse_resource("HOST,linear.tv.apple.com\n", media).rules[0]

        preview = build_priority_preview(
            resolve_conflicts(audit_rules((media_rule, apple_rule))),
            target="quantumult-x",
        )

        self.assertEqual(preview.candidate_rules, ())
        self.assertEqual(preview.status_counts["equivalent-policy"], 1)

    def test_priority_preview_flags_missing_apple_policy_instead_of_proxy_candidate(self) -> None:
        ai = Source(
            "rulego-ai",
            "filter",
            "surge",
            "ai",
            "AI",
            "https://ai.test",
            "surge",
        )
        proxy = Source(
            "rulego-proxy",
            "filter",
            "surge",
            "proxy",
            "全球加速",
            "https://proxy.test",
            "surge",
        )
        ai_rule = parse_resource("HOST-SUFFIX,gateway.icloud.com\n", ai).rules[0]
        proxy_rule = parse_resource("HOST,gateway.icloud.com\n", proxy).rules[0]

        preview = build_priority_preview(
            resolve_conflicts(audit_rules((ai_rule, proxy_rule))),
            target="quantumult-x",
        )

        self.assertEqual(len(preview.candidate_rules), 1)
        self.assertEqual(preview.candidate_rules[0].rule_type, "HOST-SUFFIX")
        self.assertEqual(preview.candidate_rules[0].value, "gateway.icloud.com")
        review = [item for item in preview.items if item.status == "review-required"]
        self.assertEqual(review[0].disposition_reason, "apple-policy-missing")
        self.assertEqual(review[0].method, "apple-service-contract")

    def test_priority_preview_keeps_reject_ahead_of_apple_service_contract(self) -> None:
        reject = Source(
            "rulego-reject",
            "filter",
            "surge",
            "reject",
            "reject",
            "https://reject.test",
            "surge",
        )
        apple = Source(
            "blackmatrix-apple",
            "filter",
            "quantumult-x",
            "apple",
            "苹果服务",
            "https://apple.test",
            "quantumult-x",
        )
        reject_rule = parse_resource("HOST,iadsdk.apple.com\n", reject).rules[0]
        apple_rule = parse_resource("HOST-SUFFIX,apple.com\n", apple).rules[0]

        preview = build_priority_preview(
            resolve_conflicts(audit_rules((reject_rule, apple_rule))),
            target="quantumult-x",
        )

        self.assertEqual(preview.candidate_rules, ())
        self.assertEqual(preview.status_counts["enforced"], 1)

    def test_generated_quantumultx_routes_pass_openai_probes(self) -> None:
        import json

        build = json.loads((ROOT / "outputs" / "quantumult-x" / "build.json").read_text(encoding="utf-8"))
        rules = []
        for entry in build["safe_categories"]:
            source = Source(
                f"generated-{entry['category']}",
                "filter",
                "quantumult-x",
                entry["category"],
                entry["policy"],
                "inline:generated",
                "quantumult-x",
            )
            rules.extend(
                parse_resource((ROOT / entry["file"]).read_text(encoding="utf-8"), source).rules
            )

        for domain in ("auth.openai.com", "chatgpt.com", "persistent.oaistatic.com", "api.oaistatsig.com"):
            result = simulate_first_match(rules, RouteProbe(domain=domain))
            self.assertIsNotNone(result)
            self.assertEqual(result.policy, "AI")

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
        alipay = Source("alipay", "filter", "surge", "alipay", "direct", "https://p.test", "surge")
        rules = (
            parse_resource("DOMAIN,ai.example\n", ai).rules[0],
            parse_resource("DOMAIN-SUFFIX,ads.example\n", reject).rules[0],
            parse_resource("DOMAIN,pay.example\n", alipay).rules[0],
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            entries = render_mihomo_category_filters(
                rules, root / "safe", relative_prefix="outputs/mihomo/categories/safe"
            )
            self.assertEqual([entry["category"] for entry in entries], ["reject", "ai", "alipay"])
            self.assertIn("DOMAIN,ai.example\n", (root / "safe" / "ai.list").read_text(encoding="utf-8"))
            self.assertNotIn(",AI\n", (root / "safe" / "ai.list").read_text(encoding="utf-8"))
            render_mihomo_rule_providers(entries, root / "providers.yaml", repository_base_url="https://raw.test")
            render_mihomo_rules(entries, root / "rules.yaml")
            providers = (root / "providers.yaml").read_text(encoding="utf-8")
            route_rules = (root / "rules.yaml").read_text(encoding="utf-8")
            self.assertIn("behavior: classical", providers)
            self.assertIn("format: text", providers)
            self.assertIn("interval: 86400", providers)
            self.assertLess(route_rules.index("RULE-SET,reject,REJECT"), route_rules.index("RULE-SET,ai,AI"))
            self.assertLess(route_rules.index("RULE-SET,ai,AI"), route_rules.index("GEOSITE,openai,AI"))
            self.assertLess(route_rules.index("GEOSITE,openai,AI"), route_rules.index("RULE-SET,alipay,DIRECT"))
            self.assertIn("GEOSITE,cn,DIRECT", route_rules)
            self.assertGreater(route_rules.index("GEOSITE,cn,DIRECT"), route_rules.index("RULE-SET,ai,AI"))

    def test_quantumultx_remote_renderer_uses_daily_refresh_interval(self) -> None:
        from ruleforge.render import render_filter_remote_conf

        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "filter_remote.conf"
            render_filter_remote_conf(
                [{"category": "ai", "file": "categories/ai.list", "policy": "AI"}],
                path,
                repository_base_url="https://raw.test",
                title="test",
            )
            content = path.read_text(encoding="utf-8")
            self.assertIn("update-interval=86400", content)
            self.assertNotIn("update-interval=172800", content)

    def test_quantumultx_complete_profile_uses_prior_shape_without_private_material(self) -> None:
        profile = (ROOT / "profiles" / "quantumult-x" / "config.example.conf").read_text(encoding="utf-8")
        generated = (ROOT / "outputs" / "quantumult-x" / "filter_remote.safe.conf").read_text(encoding="utf-8")

        for section in (
            "general",
            "dns",
            "policy",
            "server_remote",
            "filter_remote",
            "rewrite_remote",
            "server_local",
            "filter_local",
            "rewrite_local",
            "task_local",
            "http_backend",
            "mitm",
        ):
            self.assertIn(f"[{section}]", profile)

        server_remote = profile.split("[server_remote]", 1)[1].split("[filter_remote]", 1)[0]
        self.assertNotRegex(server_remote, r"(?m)^\s*https?://")

        mitm = profile.split("[mitm]", 1)[1]
        self.assertNotRegex(mitm, r"(?mi)^\s*(passphrase|p12|hostname|skip_validating_cert)\s*=")
        self.assertNotIn("gravatar", profile.lower())
        self.assertIn("fallback_udp_policy = reject", profile)
        self.assertNotIn("update-interval=172800", profile)

        generated_filter_lines = [
            line for line in generated.splitlines() if line == "[filter_remote]" or line.startswith("https://")
        ]
        profile_filter = profile.split("[filter_remote]", 1)[1].split("[rewrite_remote]", 1)[0]
        for line in generated_filter_lines:
            if line != "[filter_remote]":
                self.assertIn(line, profile_filter)
        self.assertIn("static=AI, 香港节点, 台湾节点, 日本节点, 韩国节点, 狮城节点, 美国节点", profile)
        self.assertIn("event-interaction https://raw.githubusercontent.com/KOP-XIAO/QuantumultX", profile)

    def test_category_renderers_remove_stale_files_and_keep_empty_declared_categories(self) -> None:
        from ruleforge.render import render_category_filters, render_mihomo_category_filters

        source = Source("test", "filter", "surge", "ai", "AI", "https://example.test", "surge")
        rule = parse_resource("DOMAIN,example.com\n", source).rules[0]
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            for renderer in (render_category_filters, render_mihomo_category_filters):
                output = root / renderer.__name__
                output.mkdir()
                stale = output / "stale.list"
                stale.write_text("old\n", encoding="utf-8")
                entries = renderer(
                    (rule,),
                    output,
                    category_policies={"ai": "AI", "reject": "reject"},
                )
                self.assertFalse(stale.exists())
                self.assertEqual([entry["category"] for entry in entries], ["reject", "ai"])
                self.assertIn("# Policy: reject", (output / "reject.list").read_text(encoding="utf-8"))

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

    def test_priority_preview_is_not_referenced_by_active_profiles(self) -> None:
        active_files = (
            ROOT / "profiles" / "quantumult-x" / "config.example.conf",
            ROOT / "profiles" / "mihomo" / "config.example.yaml",
            ROOT / "outputs" / "quantumult-x" / "filter_remote.safe.conf",
            ROOT / "outputs" / "mihomo" / "rules.safe.yaml",
            ROOT / "outputs" / "mihomo" / "rule-providers.safe.yaml",
        )
        for path in active_files:
            with self.subTest(path=path):
                self.assertNotIn("priority-preview", path.read_text(encoding="utf-8"))

    def test_mihomo_profile_shows_business_groups_before_regions_with_icons(self) -> None:
        content = (ROOT / "profiles" / "mihomo" / "config.example.yaml").read_text(encoding="utf-8")
        self.assertLess(content.index("  - name: 全球加速"), content.index("  - name: 香港节点"))
        self.assertLess(content.index("  - name: 兜底策略"), content.index("  - name: 香港节点"))
        self.assertEqual(content.count("raw.githubusercontent.com/Orz-3/mini/master/Color/"), 20)

    def test_mihomo_profile_keeps_provider_nodes_unique_and_proxy_groups_closed(self) -> None:
        content = (ROOT / "profiles" / "mihomo" / "config.example.yaml").read_text(encoding="utf-8")
        self.assertNotIn("additional-prefix:", content)
        self.assertEqual(content.count("include-all: true"), 6)
        self.assertEqual(content.count("expected-status: 204"), 8)
        self.assertNotIn("empty-fallback: DIRECT", content)
        self.assertIn("tolerance: 10", content)
        self.assertEqual(content.count("interval: 86400"), 28)
        self.assertNotIn("interval: 172800", content)

    def test_mihomo_profile_declares_udp_disabled_by_default(self) -> None:
        content = (ROOT / "profiles" / "mihomo" / "config.example.yaml").read_text(encoding="utf-8")
        self.assertEqual(content.count("override:"), 2)
        self.assertEqual(content.count("udp: false"), 2)
        self.assertIn("Proxy Provider 的节点 UDP 默认显式关闭", (ROOT / "profiles" / "mihomo" / "README.md").read_text(encoding="utf-8"))

    def test_quantumultx_readme_documents_all_remote_policies(self) -> None:
        content = (ROOT / "profiles" / "quantumult-x" / "README.md").read_text(encoding="utf-8")
        self.assertIn("- 美国节点", content)
        self.assertIn("- proxy", content)
        self.assertIn("没有 Mihomo 的 `GEOSITE,cn` 域名兜底", content)

    def test_quantumultx_has_openai_statsig_fallback(self) -> None:
        _, sources = load_manifest(ROOT / "sources" / "quantumultx.yaml")
        self.assertTrue(any(source.id == "local-openai-oaistatsig" for source in sources))
        content = (ROOT / "outputs" / "quantumult-x" / "categories" / "safe" / "ai.list").read_text(
            encoding="utf-8"
        )
        self.assertIn("host-suffix,oaistatsig.com,AI", content)

    def test_generated_china_media_filter_is_not_empty(self) -> None:
        content = (ROOT / "outputs" / "quantumult-x" / "categories" / "safe" / "china-media.list").read_text(
            encoding="utf-8"
        )
        rules = [line for line in content.splitlines() if line.strip() and not line.startswith("#")]
        self.assertGreater(len(rules), 0)
        self.assertIn("host,api.bilibili.com,港台番剧", rules)

    def test_generated_priority_previews_are_inactive_and_summarized(self) -> None:
        import json

        for target in ("quantumult-x", "mihomo"):
            with self.subTest(target=target):
                root = ROOT / "outputs" / target
                preview = json.loads((root / "priority-preview.json").read_text(encoding="utf-8"))
                build = json.loads((root / "build.json").read_text(encoding="utf-8"))
                markdown = (root / "priority-preview.md").read_text(encoding="utf-8")

                self.assertEqual(preview["mode"], "preview-only")
                self.assertFalse(preview["active"])
                self.assertEqual(preview["target"], target)
                self.assertEqual(
                    preview["actual_policy_mismatch_count"],
                    preview["preview_candidate_decision_count"]
                    + preview["review_required_count"],
                )
                self.assertEqual(build["priority_preview"], {
                    key: value
                    for key, value in preview.items()
                    if key not in {"override_candidates", "items"}
                })
                self.assertIn("仅供审阅", markdown)

    def test_mihomo_profile_places_geosite_cn_before_geoip_and_match(self) -> None:
        content = (ROOT / "profiles" / "mihomo" / "config.example.yaml").read_text(encoding="utf-8")
        self.assertIn("geosite-matcher: succinct", content)
        self.assertIn(
            'geosite: "https://github.com/MetaCubeX/meta-rules-dat/releases/download/latest/geosite.dat"',
            content,
        )
        self.assertIn("geo-update-interval: 24", content)
        self.assertNotIn("geo-update-interval: 48", content)
        self.assertLess(content.index("RULE-SET,ai,AI"), content.index("GEOSITE,openai,AI"))
        self.assertLess(content.index("GEOSITE,openai,AI"), content.index("RULE-SET,alipay,DIRECT"))
        self.assertLess(content.index("RULE-SET,proxy,全球加速"), content.index("GEOSITE,cn,DIRECT"))
        self.assertLess(content.index("GEOSITE,cn,DIRECT"), content.index("GEOIP,CN,DIRECT,no-resolve"))


if __name__ == "__main__":
    unittest.main()
