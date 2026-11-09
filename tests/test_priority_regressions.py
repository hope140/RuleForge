from __future__ import annotations

import sys
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ruleforge.audit import audit_rules, resolve_conflicts
from ruleforge.model import Rule
from ruleforge.render import MIHOMO_RULES_BEGIN, MIHOMO_RULES_END, render_mihomo_rules, sync_mihomo_profile, sync_quantumultx_profile
from ruleforge.runtime import RouteProbe, simulate_route
from route_helpers import active_routes, policy_name


class PriorityRegressionTests(unittest.TestCase):
    def test_routed_ip_options_follow_policy(self) -> None:
        for kind, value in (("IP-CIDR", "91.108.4.0/22"), ("IP6-CIDR", "2001:b28:f23c::/48")):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as temp:
                path = Path(temp) / "rules.yaml"
                rule = Rule("test", "clash", "proxy", "proxy", kind, value, ("no-resolve",))
                for entries in ([], [{"category": "privacy", "policy": "reject"}]):
                    render_mihomo_rules(entries, path, priority_rules=[rule])
                    native_type = "IP-CIDR6" if kind == "IP6-CIDR" else kind
                    self.assertIn(
                        f"{native_type},{value},全球加速,no-resolve",
                        path.read_text(encoding="utf-8"),
                    )

    def test_exact_conflict_loser_cannot_return_as_priority_override(self) -> None:
        winner = Rule("google", "surge", "google", "谷歌服务", "HOST", "mtalk.google.com")
        loser = Rule("direct", "surge", "china-direct", "direct", "HOST", "mtalk.google.com")
        broad = Rule("google", "surge", "google", "谷歌服务", "HOST-SUFFIX", "google.com")
        result = resolve_conflicts(audit_rules([winner, loser, broad]))
        self.assertIn(winner, result.rules)
        self.assertNotIn(loser, result.rules)
        self.assertNotIn(loser, result.priority_override_rules)
        self.assertTrue(set(result.priority_override_rules).issubset(result.rules))

    def test_profile_sync_preserves_unmanaged_settings_and_line_endings(self) -> None:
        generated = "# generated\nrules:\n  - RULE-SET,ai,AI\n"
        for newline in ("\n", "\r\n"):
            with self.subTest(newline=repr(newline)):
                prefix = newline.join(("mixed-port: 7890", "rules:", "  - IP-CIDR,10.0.0.0/8,DIRECT", MIHOMO_RULES_BEGIN))
                suffix = newline.join((MIHOMO_RULES_END, "  - MATCH,兜底策略", ""))
                original = prefix + newline + "  - DOMAIN,stale.test,DIRECT" + newline + suffix
                updated = sync_mihomo_profile(original, generated)
                self.assertEqual(updated, prefix + newline + "  - RULE-SET,ai,AI" + newline + suffix)
                self.assertEqual(sync_mihomo_profile(updated, generated), updated)

    def test_profile_sync_rejects_missing_duplicate_or_reversed_markers(self) -> None:
        for content in ("rules:\n", MIHOMO_RULES_BEGIN * 2 + MIHOMO_RULES_END, MIHOMO_RULES_END + MIHOMO_RULES_BEGIN):
            with self.subTest(content=content), self.assertRaises(ValueError):
                sync_mihomo_profile(content, "rules:\n  - RULE-SET,ai,AI\n")

    def test_profile_sync_check_fails_without_writing_and_output_is_isolated(self) -> None:
        from ruleforge.cli import main

        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            profile, rules, output = (root / name for name in ("profile.yaml", "rules.yaml", "assembled.yaml"))
            original = f"rules:\n{MIHOMO_RULES_BEGIN}\n  - DOMAIN,old.test,DIRECT\n{MIHOMO_RULES_END}\n"
            profile.write_text(original, encoding="utf-8")
            rules.write_text("rules:\n  - RULE-SET,ai,AI\n", encoding="utf-8")
            args = ["sync-mihomo-profile", "--profile", str(profile), "--rules", str(rules)]
            self.assertEqual(main([*args, "--check"]), 1)
            self.assertEqual(profile.read_text(encoding="utf-8"), original)
            self.assertEqual(main([*args, "--output", str(output)]), 0)
            self.assertEqual(profile.read_text(encoding="utf-8"), original)
            self.assertIn("RULE-SET,ai,AI", output.read_text(encoding="utf-8"))
            self.assertEqual(main(args), 0)
            self.assertEqual(main([*args, "--check"]), 0)

    def test_committed_profile_matches_generated_routing_block(self) -> None:
        profile = (ROOT / "profiles/mihomo/config.example.yaml").read_text(encoding="utf-8")
        generated = (ROOT / "outputs/mihomo/rules.safe.yaml").read_text(encoding="utf-8")
        self.assertEqual(profile, sync_mihomo_profile(profile, generated))

    def test_emitted_priorities_only_contain_surviving_rules(self) -> None:
        for target in ("quantumult-x", "mihomo"):
            with self.subTest(target=target):
                root = ROOT / "outputs" / target
                build = json.loads((root / "build.json").read_text(encoding="utf-8"))
                safe = set()
                for entry in build["safe_categories"]:
                    for row in (ROOT / entry["file"]).read_text(encoding="utf-8").splitlines():
                        if row and not row.startswith("#"):
                            kind, value, *_ = row.split(",")
                            safe.add((kind, value, policy_name(entry["policy"])))
                name = "priority-overrides.safe.list" if target == "quantumult-x" else "rules.safe.yaml"
                count = 0
                for row in (root / name).read_text(encoding="utf-8").splitlines():
                    row = row.strip().removeprefix("- ")
                    if not row or row.startswith(("#", "rules:", "RULE-SET,", "GEOSITE,")):
                        continue
                    kind, value, policy, *_ = row.split(",")
                    self.assertIn((kind, value, policy_name(policy)), safe, row)
                    count += 1
                self.assertEqual(count, build["priority_override_rule_count"])

    def test_qx_sync_repairs_order_and_preserves_other_sections(self) -> None:
        original = "[policy]\r\nstatic=games, direct\r\n\r\n[filter_remote]\r\n"
        tail = "\r\n[rewrite_remote]\r\n# Local rewrite settings\r\n"
        first, second = "https://example.com/first", "https://example.com/second"
        generated = f"[filter_remote]\n{first}\n{second}\n"
        reversed_profile = original + f"{second}\r\n{first}\r\n" + tail
        expected = original + f"{first}\r\n{second}\r\n" + tail
        self.assertEqual(sync_quantumultx_profile(reversed_profile, generated), expected)
        self.assertEqual(sync_quantumultx_profile(expected, generated), expected)

    def test_emitted_routes_enforce_priority_and_exact_conflict_decisions(self) -> None:
        expected = {
            "c.mi.com": "全球加速",
            "apple-relay.cloudflare.com": "苹果服务",
            "cp4.cloudflare.com": "苹果服务",
            "store.steampowered.com": "游戏商店",
            "steamcommunity.com": "游戏商店",
            "cmp1-hkg1.steamserver.net": "游戏商店",
            "cmp2-dfw2.steamserver.net": "游戏商店",
            "ext1-maa2.steamserver.net": "游戏商店",
            "ext2-maa2.steamserver.net": "游戏商店",
            "cdn.steamusercontent.com": "游戏商店",
            "store.epicgames.com": "游戏商店",
            "account-public-service-prod03.ol.epicgames.com": "游戏商店",
            "launcherwaitingroom-public-service-prod06.ol.epicgames.com": "游戏商店",
            "launcher-website-prod07.ol.epicgames.com": "游戏商店",
            "accounts.launcher-website-prod07.ol.epicgames.com": "游戏商店",
            "accountportal-website-prod07.ol.epicgames.com": "游戏商店",
            "static-assets-prod.epicgames.com": "游戏商店",
            "store-site-backend-static.ak.epicgames.com": "游戏商店",
            "store-content.ak.epicgames.com": "游戏商店",
            "library-service.live.use1a.on.epicgames.com": "游戏商店",
            "datastorage-public-service-liveegs.live.use1a.on.epicgames.com": "游戏商店",
            "cache14-dfw2.steamcontent.com": "游戏下载",
            "steampipe.akamaized.net": "游戏下载",
            "client-update.steamstatic.com": "游戏下载",
            "client-update.fastly.steamstatic.com": "游戏下载",
            "client-update.akamai.steamstatic.com": "游戏下载",
            "download2.epicgames.com": "游戏下载",
            "epicgames-download1.akamaized.net": "游戏下载",
            "api-glb-sea.smoot.apple.com": "苹果服务",
            "tvbtracking.azurewebsites.net": "国际媒体",
            "beacons.gvt2.com": "谷歌服务",
            "ctldl.windowsupdate.com": "direct",
            "azuremigrate.download.prss.microsoft.com": "direct",
        }
        for target in ("quantumult-x", "mihomo"):
            for profile in (False, True):
                with self.subTest(target=target, profile=profile):
                    rules = active_routes(ROOT, target, profile=profile)
                    for domain, policy in expected.items():
                        result = simulate_route(rules, RouteProbe(domain=domain))
                        self.assertIsNotNone(result, domain)
                        self.assertEqual(result.policy, policy, domain)
                    for domain in ("ipv6check-http.steamserver.net", "ye1.c.lencr.org", "other.akamaized.net"):
                        result = simulate_route(rules, RouteProbe(domain=domain))
                        if result is not None:
                            self.assertNotIn(result.policy, {"游戏商店", "游戏下载"}, domain)
                    if target == "mihomo":
                        for executable in ("qbittorrent.exe", "aria2c.exe"):
                            result = simulate_route(rules, RouteProbe(process=executable))
                            self.assertIsNotNone(result, executable)
                            self.assertEqual(result.policy, "direct")
                    result = simulate_route(rules, RouteProbe(ip="23.211.15.99"))
                    self.assertIsNotNone(result)
                    self.assertEqual(result.policy, "国际媒体")
                    mtalk = simulate_route(rules, RouteProbe(domain="mtalk.google.com"))
                    self.assertIsNotNone(mtalk)
                    self.assertEqual(mtalk.policy, "谷歌服务" if target == "quantumult-x" else "direct")


if __name__ == "__main__":
    unittest.main()
