from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ruleforge.cli import main
from ruleforge.manifest import ManifestError, load_manifest
from ruleforge.model import Source
from ruleforge.parsers import parse_resource


class InputRegressionTests(unittest.TestCase):
    def manifest(self, *, category="demo", policy="direct", enabled="true") -> str:
        return (
            "schema_version: 1\ntarget: quantumult-x\nsources:\n"
            "  - id: local-demo\n    kind: inline\n    format: quantumult-x\n"
            f"    category: '{category}'\n    policy: '{policy}'\n"
            "    url: inline:HOST,example.com\n    parser: quantumult-x\n"
            f"    enabled: {enabled}\n"
        )

    def test_invalid_or_inactive_sources_cannot_replace_existing_output(self):
        cases = (
            "schema_version: 1\ntarget: quantumult-x\n",
            "schema_version: 1\ntarget: quantumult-x\nsources: invalid\n",
            "schema_version: 1\ntarget: quantumult-x\nsources:\n",
            self.manifest(enabled="false"),
        )
        for content in cases:
            with self.subTest(content=content), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                manifest = root / "manifest.yaml"
                manifest.write_text(content, encoding="utf-8")
                output = root / "output"
                category = output / "categories" / "safe" / "demo.list"
                category.parent.mkdir(parents=True)
                category.write_bytes(b"host,example.com,direct\n")
                before = {p.relative_to(output): p.read_bytes() for p in output.rglob("*") if p.is_file()}
                with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                    result = main(["build", "--manifest", str(manifest), "--output-dir", str(output)])
                self.assertEqual(result, 1)
                after = {p.relative_to(output): p.read_bytes() for p in output.rglob("*") if p.is_file()}
                self.assertEqual(after, before)
                self.assertEqual(list(root.glob(".ruleforge-staging-*")), [])

    def test_manifest_rejects_duplicate_keys_and_sources_sections(self):
        base = self.manifest()
        cases = (
            base.replace("target: quantumult-x", "target: mihomo\ntarget: quantumult-x"),
            base.replace("    policy: 'direct'", "    policy: AI\n    policy: 'direct'"),
            base + "sources:\n",
            base.replace("sources:\n", "sources: invalid\nsources:\n", 1),
        )
        for content in cases:
            with self.subTest(content=content), tempfile.TemporaryDirectory() as temp:
                path = Path(temp) / "manifest.yaml"
                path.write_text(content, encoding="utf-8")
                with self.assertRaisesRegex(ManifestError, "duplicate"):
                    load_manifest(path)

    def test_category_names_cannot_collapse_to_the_same_output_filename(self):
        for category in ("a.b", "a_b", "A-b", "a--b", "-demo", "demo-", "", " "):
            with self.subTest(category=category), tempfile.TemporaryDirectory() as temp:
                path = Path(temp) / "manifest.yaml"
                path.write_text(self.manifest(category=category), encoding="utf-8")
                with self.assertRaisesRegex(ManifestError, "category.*kebab-case"):
                    load_manifest(path)

    def test_policy_must_produce_one_nonempty_routing_field(self):
        for policy in ("", " ", "direct,other"):
            with self.subTest(policy=policy), tempfile.TemporaryDirectory() as temp:
                path = Path(temp) / "manifest.yaml"
                path.write_text(self.manifest(policy=policy), encoding="utf-8")
                with self.assertRaisesRegex(ManifestError, "policy"):
                    load_manifest(path)

    def test_lint_rejects_mixed_policies_in_one_enabled_category(self):
        first = self.manifest()
        second = self.manifest(policy="AI").split("sources:\n", 1)[1]
        second = second.replace("local-demo", "local-other").replace("example.com", "other.example")
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "manifest.yaml"
            path.write_text(first + second, encoding="utf-8")
            with self.assertRaisesRegex(ManifestError, "mixed policies"):
                load_manifest(path)
            with contextlib.redirect_stderr(io.StringIO()), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(main(["lint", "--manifest", str(path)]), 1)
            path.write_text(first + second.replace("enabled: true", "enabled: false"), encoding="utf-8")
            _, sources = load_manifest(path)
            self.assertEqual(len(sources), 2)

    def test_quantumultx_native_options_survive_parsing_and_rendering(self):
        source = Source("test", "filter", "quantumult-x", "demo", "AI", "https://example.test", "quantumult-x")
        options = ("force-cellular", "multi-interface", "multi-interface-balance", "via-interface=en0", "no-resolve")
        result = parse_resource("host,example.com,old-policy," + ",".join(options), source)
        self.assertEqual(result.issues, ())
        self.assertEqual(result.rules[0].options, options)
        self.assertEqual(result.rules[0].to_quantumultx(), "host,example.com,AI," + ",".join(options))

    def test_mihomo_native_destination_port_round_trips(self):
        source = Source("test", "filter", "clash", "demo", "AI", "https://example.test", "clash-classical")
        result = parse_resource("payload:\n  - DST-PORT,443\n", source)
        self.assertEqual(result.issues, ())
        self.assertEqual(result.rules[0].rule_type, "DEST-PORT")
        self.assertEqual(result.rules[0].to_mihomo(), "DST-PORT,443")


if __name__ == "__main__":
    unittest.main()
