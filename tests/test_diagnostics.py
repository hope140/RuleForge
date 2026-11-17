from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from ruleforge.cli import main


class DiagnosticsTests(unittest.TestCase):
    def test_conflict_diagnostics_preserve_published_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            output = root / 'output'
            output.mkdir()
            sentinel = output / 'existing.list'
            sentinel.write_bytes(b'existing published rules\n')
            manifest = root / 'manifest.yaml'
            lines = ['schema_version: 1', 'target: quantumult-x', 'sources:']
            for category, policy in [('ai', 'AI'), ('social', 'Social')]:
                lines.extend([
                    f'  - id: {category}', '    kind: inline', '    format: quantumult-x',
                    f'    category: {category}', f'    policy: {policy}',
                    f'    url: "inline:HOST,same.example,{policy}"', '    parser: quantumult-x', '    enabled: true',
                ])
            manifest.write_text('\n'.join(lines) + '\n')
            args = ['build', '--manifest', str(manifest), '--output-dir', str(output),
                    '--cache-dir', str(root / 'cache'), '--fail-on-conflict']
            self.assertEqual(main(args + ['--diagnostics-dir', str(root / 'diagnostics')]), 2)
            report = json.loads((root / 'diagnostics/conflicts.json').read_text())
            self.assertEqual(report['summary']['unresolved_conflict_count'], 1)
            self.assertEqual(report['unresolved_groups'], [
                {'kind': 'exact-policy', 'categories': ['ai', 'social'], 'count': 1}])
            self.assertEqual(report['unresolved'][0]['conflict']['left']['value'], 'same.example')
            self.assertEqual(len(report['sources']), 2)
            self.assertEqual(sentinel.read_bytes(), b'existing published rules\n')
            self.assertEqual(list(output.iterdir()), [sentinel])
            for path in [output, output / 'nested', root]:
                self.assertEqual(main(args + ['--diagnostics-dir', str(path)]), 1)
                self.assertEqual(sentinel.read_bytes(), b'existing published rules\n')

    def test_graph_api_stays_social_without_reclassifying_meta_ai(self):
        from ruleforge.audit import audit_rules, resolve_conflicts
        from ruleforge.model import Rule
        rules = [Rule(source, "quantumult-x", category, policy, "HOST", "graph.facebook.com")
                 for source, category, policy in [('rulego-ai-supplement', 'ai', 'AI'),
                                                  ('magicrule-social-whatsapp', 'social', '全球加速')]]
        result = resolve_conflicts(audit_rules(rules))
        self.assertEqual(result.rules, (rules[1],))
        self.assertEqual(result.unresolved_decisions, ())
        ai = Rule('test', 'quantumult-x', 'ai', 'AI', 'HOST-SUFFIX', 'meta.ai')
        self.assertIn(ai, resolve_conflicts(audit_rules([*rules, ai])).rules)
        reject = Rule('reject', 'quantumult-x', 'reject', 'reject', 'HOST', 'graph.facebook.com')
        self.assertEqual(resolve_conflicts(audit_rules([*rules, reject])).rules, (reject,))

    def test_quarantine_uses_immutable_same_target_snapshots(self):
        from ruleforge.manifest import load_manifest
        for name, target in [('quantumultx', 'quantumult-x'), ('mihomo', 'mihomo')]:
            _, sources = load_manifest(ROOT / 'sources' / (name + '.yaml'))
            snapshots = [s for s in sources if s.id.startswith('snapshot-reviewed-')]
            self.assertEqual({s.category for s in snapshots}, {'apple', 'telegram', 'china-direct'})
            for source in snapshots:
                self.assertIn('/893b4f3cb68f415c9025ce82fade7011fd5333a3/outputs/' + target + '/', source.url)
                self.assertEqual(source.resolver, '')
                self.assertTrue(source.enabled)
            self.assertFalse(next(s for s in sources if s.id == 'magicrule-apple-proxy').enabled)


if __name__ == '__main__':
    unittest.main()
