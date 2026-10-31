from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class MihomoRegionFilterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        profile = (ROOT / "profiles/mihomo/config.example.yaml").read_text(encoding="utf-8")
        cls.filters = {}
        for block in profile.split("  - name: ")[1:]:
            name = block.splitlines()[0]
            if "    type: url-test\n" not in block:
                continue
            include = re.search(r"^    filter: (.+)$", block, re.MULTILINE)
            exclude = re.search(r"^    exclude-filter: (.+)$", block, re.MULTILINE)
            assert include is not None and exclude is not None
            cls.filters[name] = (
                re.compile(json.loads(include.group(1))),
                re.compile(json.loads(exclude.group(1))),
            )

    def matching_regions(self, node: str) -> list[str]:
        return [
            name
            for name, (include, exclude) in self.filters.items()
            if include.search(node) and not exclude.search(node)
        ]

    def test_region_names_and_numbered_codes_keep_their_region(self) -> None:
        cases = {
            "香港节点": ("香港 01", "港01", "HK01", "Hong Kong 01", "HongKong 01"),
            "台湾节点": ("台湾 01", "台01", "TW01", "Taiwan 01"),
            "日本节点": ("日本 01", "JP01", "Japan 01"),
            "韩国节点": ("韩国 01", "韩01", "KR01", "Korea 01", "🇰🇷 01"),
            "狮城节点": ("新加坡 01", "狮城 01", "狮01", "坡01", "SG01", "Singapore 01"),
            "美国节点": ("美国 01", "美01", "US01", "United States 01", "America 01"),
        }
        self.assertEqual(set(self.filters), set(cases))
        for region, nodes in cases.items():
            for node in nodes:
                with self.subTest(node=node):
                    self.assertEqual(self.matching_regions(node), [region])

    def test_short_codes_do_not_match_inside_unrelated_words(self) -> None:
        for node in (
            "Australia 01", "Austria 01", "Russia 01", "Business 01",
            "Ukraine 01", "ASGARD 01", "Network 01", "myJPClient 01",
        ):
            with self.subTest(node=node):
                self.assertEqual(self.matching_regions(node), [])

    def test_descriptive_words_do_not_exclude_correct_region(self) -> None:
        for node in ("Hong Kong Business 01", "香港 HK 每日专线", "香港 Network 01"):
            with self.subTest(node=node):
                self.assertEqual(self.matching_regions(node), ["香港节点"])

    def test_multi_region_names_remain_outside_region_groups(self) -> None:
        for node in ("HK-SG 01", "香港 狮01", "日本 US01", "KR-TW 01", "Hong Kong United States 01"):
            with self.subTest(node=node):
                self.assertEqual(self.matching_regions(node), [])


if __name__ == "__main__":
    unittest.main()
