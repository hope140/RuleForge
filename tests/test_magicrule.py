from __future__ import annotations

import dataclasses
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ruleforge.curation import curate_rules
from ruleforge.fetch import FetchError, fetch_source
from ruleforge.manifest import ManifestError, load_manifest
from ruleforge.model import Rule, Source
from ruleforge.audit import audit_rules, resolve_conflicts
from ruleforge.runtime import RouteProbe, simulate_route
from route_helpers import active_routes


class MagicRuleTests(unittest.TestCase):
    def source(self, name="OpenAI", client="QuantumultX"):
        return Source("magicrule-" + name.lower(), "filter",
                      "quantumult-x" if client == "QuantumultX" else "clash", "ai", "AI",
                      f"https://magicrule.pages.dev/data/index/{client}.json#{name}",
                      "quantumult-x" if client == "QuantumultX" else "clash-classical",
                      resolver="magicrule")

    def documents(self, source, payload=b"HOST,chatgpt.com,OpenAI\n", version="one"):
        client = "QuantumultX" if source.format == "quantumult-x" else "Mihomo"
        name = source.url.split("#")[1]
        manifest_url = f"https://magicrule.pages.dev/data/rules/{client}/{name}/manifest.json"
        artifact_url = f"https://rule-26r.pages.dev/data/_shared/artifacts/{name}_{version}.list"
        manifest = {"client": client, "rule": name, "artifacts": [{
            "key": "rules" if client == "QuantumultX" else "classical",
            "url": artifact_url, "binary": False, "empty": False,
            "dedupe": {"bytes_sha256": hashlib.sha256(payload).hexdigest()},
        }]}
        index = {"client": client, "rules": [{"name": name, "manifest": manifest_url}]}
        return index, manifest, {
            source.url.split("#")[0]: json.dumps(index).encode(),
            manifest_url: json.dumps(manifest).encode(), artifact_url: payload,
        }

    def test_refresh_follows_new_hash_and_offline_reuses_resolved_resource(self):
        source = self.source()
        with tempfile.TemporaryDirectory() as cache:
            for version in ("one", "two"):
                payload = f"HOST,{version}.example.com,OpenAI\n".encode()
                _, _, documents = self.documents(source, payload, version)
                with patch("ruleforge.fetch._download", side_effect=lambda url, *args: documents[url]):
                    resource = fetch_source(source, cache, refresh=True)
                self.assertEqual(resource.text, payload.decode())
                self.assertIn(version, resource.resolved_url)
            with patch("ruleforge.fetch._download", side_effect=AssertionError("offline network")):
                cached = fetch_source(source, cache, offline=True)
            self.assertTrue(cached.from_cache)
            self.assertEqual(cached.resolved_url, resource.resolved_url)
            self.assertEqual(cached.sha256, resource.sha256)

    def test_failed_refresh_keeps_previous_cached_rules(self):
        source = self.source()
        _, _, documents = self.documents(source)
        with tempfile.TemporaryDirectory() as cache:
            with patch("ruleforge.fetch._download", side_effect=lambda url, *args: documents[url]):
                previous = fetch_source(source, cache, refresh=True)
            url = previous.resolved_url
            documents[url] = b"HOST,wrong.example.com\n"
            with patch("ruleforge.fetch._download", side_effect=lambda url, *args: documents[url]):
                with self.assertRaisesRegex(FetchError, "SHA256"):
                    fetch_source(source, cache, refresh=True)
            self.assertEqual(fetch_source(source, cache, offline=True).text, previous.text)

    def test_metadata_is_shared_only_within_one_build(self):
        first, second = self.source(), self.source("Anthropic")
        i1, _, docs1 = self.documents(first)
        i2, _, docs2 = self.documents(second)
        index_url = first.url.split("#")[0]
        documents = {**docs1, **docs2, index_url: json.dumps({
            "client": "QuantumultX", "rules": i1["rules"] + i2["rules"],
        }).encode()}
        with tempfile.TemporaryDirectory() as cache:
            metadata_cache = {}
            with patch("ruleforge.fetch._download", side_effect=lambda url, *args: documents[url]) as get:
                for source in (first, second):
                    fetch_source(source, cache, refresh=True, metadata_cache=metadata_cache)
            self.assertEqual(sum(call.args[0] == index_url for call in get.call_args_list), 1)

    def test_rejects_missing_duplicate_or_wrong_client_categories(self):
        source = self.source()
        index, _, documents = self.documents(source)
        for data in ({**index, "rules": []}, {**index, "rules": index["rules"] * 2},
                     {**index, "client": "Surge"}):
            with self.subTest(data=data), tempfile.TemporaryDirectory() as cache:
                documents[source.url.split("#")[0]] = json.dumps(data).encode()
                with patch("ruleforge.fetch._download", side_effect=lambda url, *args: documents[url]):
                    with self.assertRaises(FetchError):
                        fetch_source(source, cache, refresh=True)

    def test_rejects_invalid_manifest_and_unsafe_downloads(self):
        source = self.source()
        index, manifest, documents = self.documents(source)
        url = index["rules"][0]["manifest"]
        for change in ({"rule": "Other"}, {"client": "Mihomo"},
                       {"artifacts": [{**manifest["artifacts"][0], "binary": True}]},
                       {"artifacts": [{**manifest["artifacts"][0], "url": "file:///secret"}]},
                       {"artifacts": [{**manifest["artifacts"][0], "url": "https://localhost/secret"}]}):
            with self.subTest(change=change), tempfile.TemporaryDirectory() as cache:
                documents[url] = json.dumps({**manifest, **change}).encode()
                with patch("ruleforge.fetch._download", side_effect=lambda url, *args: documents[url]):
                    with self.assertRaises(FetchError):
                        fetch_source(source, cache, refresh=True)

    def test_mihomo_selects_full_classical_artifact(self):
        source = self.source(client="Mihomo")
        _, _, documents = self.documents(source, b"payload:\n  - DOMAIN-SUFFIX,openai.com\n")
        with tempfile.TemporaryDirectory() as cache:
            with patch("ruleforge.fetch._download", side_effect=lambda url, *args: documents[url]):
                resource = fetch_source(source, cache, refresh=True)
        self.assertIn("payload:", resource.text)

    def test_shared_artifact_header_changes_require_matching_body_digest(self):
        source = self.source(client="Mihomo")
        body = b"payload:\n- 'DOMAIN-SUFFIX,openai.com'\n"
        original = b"# NAME: OpenAI\n# AUTHOR: MagicRule\n# REPO: https://magicrule.pages.dev\n# UPDATED: old\n" + body
        shared = original.replace(b"UPDATED: old", b"UPDATED: new")
        index, manifest, documents = self.documents(source, original)
        artifact = manifest["artifacts"][0]
        artifact["dedupe"].update(mode="standard_header_normalized", normalized_header_lines=4,
                                 semantic_sha256=hashlib.sha256(body).hexdigest())
        documents[index["rules"][0]["manifest"]] = json.dumps(manifest).encode()
        documents[artifact["url"]] = shared
        with tempfile.TemporaryDirectory() as cache:
            with patch("ruleforge.fetch._download", side_effect=lambda url, *args: documents[url]):
                self.assertEqual(fetch_source(source, cache, refresh=True).text, shared.decode())
                documents[artifact["url"]] = shared.replace(b"openai.com", b"other.com")
                with self.assertRaisesRegex(FetchError, "SHA256"):
                    fetch_source(source, cache, refresh=True)

    def test_manifests_replace_old_dependencies_and_validate_resolver(self):
        for filename in ("quantumultx.yaml", "mihomo.yaml"):
            text = (ROOT / "sources" / filename).read_text(encoding="utf-8")
            self.assertNotIn("blackmatrix7/ios_rule_script", text)
            _, sources = load_manifest(ROOT / "sources" / filename)
            self.assertEqual(sum(s.resolver == "magicrule" for s in sources), 77)
            self.assertTrue(any(s.url.endswith("#NPM") for s in sources))
            for before, after in (("resolver: magicrule", "resolver: unknown"),
                                  (".json#OpenAI", ".json"),
                                  ("https://magicrule.pages.dev", "http://magicrule.pages.dev")):
                with self.subTest(filename=filename, after=after), tempfile.TemporaryDirectory() as temp:
                    path = Path(temp) / filename
                    path.write_text(text.replace(before, after, 1), encoding="utf-8")
                    with self.assertRaises(ManifestError):
                        load_manifest(path)

    def test_copilot_curation_preserves_service_boundary_and_reports_drops(self):
        values = ("copilot-proxy.githubusercontent.com", "copilot.microsoft.com", "qwen.ai", "auth0.com")
        rules = [Rule("magicrule-copilot", "quantumult-x", "ai", "AI", "HOST-SUFFIX", v) for v in values]
        # The identical value in another dedicated source is not filtered by the Copilot boundary.
        other = dataclasses.replace(rules[2], source_id="local-ai")
        result = curate_rules([*rules, other])
        self.assertIn(rules[0], result.rules)
        self.assertIn(rules[1], result.rules)
        self.assertNotIn(rules[2], result.rules)
        self.assertIn(other, result.rules)
        self.assertTrue(any(d.rule == rules[2] and d.reason == "copilot-source-business-boundary" for d in result.dropped))

    def test_primary_source_priority_cannot_choose_a_business_category(self):
        primary = Rule("magicrule-demo", "clash", "demo", "AI", "HOST", "example.com")
        other = dataclasses.replace(primary, source_id="other", policy="direct")
        same = resolve_conflicts(audit_rules([other, primary]))
        self.assertEqual(same.rules, (primary,))
        self.assertEqual(len(same.source_decisions), 1)
        self.assertEqual(same.decisions[0].decision, "prefer-source")
        cross = resolve_conflicts(audit_rules([primary, dataclasses.replace(other, category="different")]))
        self.assertEqual(len(cross.unresolved_decisions), 1)
        self.assertEqual(len(cross.source_decisions), 0)

    def test_registry_owner_survives_same_policy_deduplication(self):
        rules = [Rule("magicrule-" + category, "clash", category, policy, "HOST-SUFFIX", "npmjs.com")
                 for category, policy in (("microsoft", "全球加速"), ("github", "GitHub"), ("developer", "全球加速"))]
        result = resolve_conflicts(audit_rules(curate_rules(rules).rules))
        self.assertEqual(len(result.rules), 1)
        self.assertEqual(result.rules[0].category, "developer")
        self.assertEqual(result.rules[0].policy, "全球加速")

    def test_fcm_direct_compatibility_preserves_both_client_contracts(self):
        for kind in ("quantumult-x", "clash"):
            push = Rule("magicrule-google", kind, "google", "谷歌服务", "HOST", "alt8-mtalk.google.com")
            ordinary = dataclasses.replace(push, value="mail.google.com")
            result = curate_rules([push, ordinary])
            self.assertEqual(result.rules[0].policy, "direct")
            self.assertEqual(result.rules[1].policy, "谷歌服务")
            main = dataclasses.replace(push, value="mtalk.google.com")
            self.assertEqual(curate_rules([main]).rules[0].policy, "direct" if kind == "clash" else "谷歌服务")

    def test_service_lists_cannot_claim_country_tlds(self):
        rules = [Rule("magicrule-google", "clash", "google", "谷歌服务", "HOST-SUFFIX", value)
                 for value in ("hk", "tw", "co", "google", "google.com.hk")]
        direct = dataclasses.replace(rules[0], category="china-direct", policy="direct", value="cn")
        result = curate_rules([*rules, direct])
        self.assertEqual({r.value for r in result.rules}, {"google", "google.com.hk", "cn"})
        self.assertEqual(len(result.dropped), 3)
        self.assertTrue(all(d.reason == "country-tld-business-overreach" for d in result.dropped))

    def test_shared_ai_infrastructure_is_not_claimed_by_a_single_product(self):
        rules = [Rule("magicrule-openai", "clash", "ai", "AI", kind, value) for kind, value in (
            ("HOST", "storage.googleapis.com"), ("HOST-SUFFIX", "statsigapi.net"),
            ("HOST-KEYWORD", "datadog"), ("HOST-KEYWORD", "sentry"),
            ("HOST-KEYWORD", "colab"), ("HOST-KEYWORD", "codex"),
            ("HOST-SUFFIX", "events.statsigapi.net"), ("HOST-SUFFIX", "chatgpt.com"),
        )]
        result = curate_rules(rules)
        self.assertEqual({r.value for r in result.rules}, {"events.statsigapi.net", "chatgpt.com"})

    def test_overseas_media_stays_out_of_domestic_corporate_direct_lists(self):
        rules = [Rule("magicrule-tencent", "clash", "china-services", "direct", "HOST-SUFFIX", value)
                 for value in ("wetv.vip", "wetvinfo.com", "joox.com", "qq.com")]
        result = curate_rules(rules)
        self.assertTrue(all(r.category == "global-media" and r.policy == "国际媒体" for r in result.rules[:3]))
        self.assertEqual(result.rules[3].policy, "direct")

    def test_netflix_does_not_claim_shared_aws_pools(self):
        values = ("34.208.0.0/12", "52.71.40.0/16", "3.228.182.10/32", "198.38.96.0/19")
        rules = [Rule("magicrule-netflix", "clash", "netflix", "Netflix", "IP-CIDR", value) for value in values]
        result = curate_rules(rules)
        self.assertEqual({r.value for r in result.rules}, set(values[2:]))
        self.assertTrue(all(d.reason == "shared-cloud-network" for d in result.dropped))
        self.assertIn(dataclasses.replace(rules[0], category="cloud", policy="全球加速"),
                      curate_rules([dataclasses.replace(rules[0], category="cloud", policy="全球加速")]).rules)

    def test_generated_routes_preserve_migrated_service_coverage(self):
        expected = {
            "claude.ai": "AI", "civitai.com": "AI",
            "appleid.apple.com": "苹果服务", "appleid.cdn-apple.com": "苹果服务",
            "mail.icloud.com.cn": "苹果服务", "mail.me.com": "苹果服务",
            "drive.google.com": "谷歌服务", "npmjs.com": "全球加速",
            "registry.npmjs.org": "全球加速", "npm.community": "全球加速",
            "bilibili.tv": "国际媒体", "paramountplus.com": "国际媒体",
            "peacocktv.com": "国际媒体", "qwen.ai": "direct",
            "xiaoaiassist.com": "direct", "copilot-proxy.githubusercontent.com": "AI",
            "copilot-telemetry.githubusercontent.com": "GitHub",
            "copilot-workspace.githubnext.com": "GitHub", "tenor.com": "全球加速",
            "linetv.tw": "国际媒体",
        }
        for target in ("quantumult-x", "mihomo"):
            for profile in (False, True):
                rules = active_routes(ROOT, target, profile=profile)
                for domain, policy in expected.items():
                    with self.subTest(target=target, profile=profile, domain=domain):
                        result = simulate_route(rules, RouteProbe(domain=domain))
                        self.assertIsNotNone(result, domain)
                        self.assertEqual(result.policy, policy)

    def test_generated_routes_keep_media_aliases_and_shared_services_scoped(self):
        expected = {
            "wetv.vip": "国际媒体", "htrace.wetvinfo.com": "国际媒体", "joox.com": "国际媒体",
            "i-joox.com": "国际媒体", "sanook.com": "国际媒体",
            "api.imem.app": "电报代理", "api.swiftgram.app": "电报代理", "mbrx.app": "电报代理",
            "e13252.dscg.akamaiedge.net": "Netflix", "h-netflix.online-metrix.net": "Netflix",
            "apple-events.akamaized.net": "苹果服务", "cdn-apple-mapkit.com": "苹果服务",
            "gsp4-cn.ls.apple.com.edgekey.net": "苹果服务", "ls.apple.com.edgesuite.net": "苹果服务",
            "storage.googleapis.com": "谷歌服务", "events.statsigapi.net": "AI",
            "discord-attachments-uploads-prd.storage.googleapis.com": "全球加速",
            "alt1-mtalk.google.com": "direct", "alt8-mtalk.google.com": "direct",
            "officecdn.microsoft.com": "direct", "ctldl.windowsupdate.com": "direct",
            "cdn.jsdelivr.net": "全球加速",
        }
        for target in ("quantumult-x", "mihomo"):
            for profile in (False, True):
                rules = active_routes(ROOT, target, profile=profile)
                for domain, policy in expected.items():
                    with self.subTest(target=target, profile=profile, domain=domain):
                        result = simulate_route(rules, RouteProbe(domain=domain))
                        self.assertIsNotNone(result, domain)
                        self.assertEqual(result.policy, policy)
                for domain in ("customer.statsigapi.net", "customer.sentry.io", "www.ecolab.com", "codexalimentarius.org"):
                    result = simulate_route(rules, RouteProbe(domain=domain))
                    self.assertTrue(result is None or result.policy != "AI", domain)
                for domain in ("unrelated-example.hk", "unrelated-example.tw", "unrelated-example.co"):
                    result = simulate_route(rules, RouteProbe(domain=domain))
                    self.assertTrue(result is None or result.policy != "谷歌服务", domain)
                shared = simulate_route(rules, RouteProbe(ip="34.208.10.1"))
                self.assertTrue(shared is None or shared.policy != "Netflix")
                netflix = simulate_route(rules, RouteProbe(ip="198.38.96.1"))
                self.assertIsNotNone(netflix)
                self.assertEqual(netflix.policy, "Netflix")


if __name__ == "__main__":
    unittest.main()
