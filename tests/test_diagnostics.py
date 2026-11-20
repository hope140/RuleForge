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
        from ruleforge.audit import _value_category_rule
        for kind, value in [('HOST-SUFFIX', 'facebook.com'),
                            ('HOST-SUFFIX', 'graph.facebook.com'),
                            ('HOST-KEYWORD', 'facebook')]:
            broad = Rule('social', 'quantumult-x', 'social', '全球加速', kind, value)
            audit = audit_rules([rules[0], broad])
            self.assertTrue(audit.conflicts)
            for conflict in audit.conflicts:
                self.assertIsNone(_value_category_rule(conflict))

    def test_restored_magicrule_sources_use_live_client_indexes(self):
        from ruleforge.manifest import load_manifest
        categories = {
            'magicrule-apple': 'Apple',
            'magicrule-apple-proxy': 'AppleProxy',
            'magicrule-telegram': 'Telegram',
            'magicrule-direct': 'Direct',
        }
        for name, client in [('quantumultx', 'QuantumultX'), ('mihomo', 'Mihomo')]:
            with self.subTest(client=client):
                _, sources = load_manifest(ROOT / 'sources' / (name + '.yaml'))
                by_id = {source.id: source for source in sources}
                self.assertFalse(any(key.startswith('snapshot-reviewed-') for key in by_id))
                for key, category in categories.items():
                    source = by_id[key]
                    self.assertTrue(source.enabled)
                    self.assertEqual(source.resolver, 'magicrule')
                    self.assertEqual(source.url, f'https://magicrule.pages.dev/data/index/{client}.json#{category}')

    def test_shared_facebook_cdn_is_not_pinned_to_ai(self):
        from ruleforge.curation import curate_rules
        from ruleforge.model import Rule
        wildcard = Rule('rulego-ai-supplement', 'surge', 'ai', 'AI',
                        'HOST-WILDCARD', 'scontent-*.xx.fbcdn.net')
        social = Rule('social', 'quantumult-x', 'social', '全球加速', 'HOST-SUFFIX', 'fbcdn.net')
        precise = Rule('ai', 'quantumult-x', 'ai', 'AI', 'HOST', 'specific.xx.fbcdn.net')
        meta = Rule('ai', 'quantumult-x', 'ai', 'AI', 'HOST-SUFFIX', 'meta.ai')
        result = curate_rules([wildcard, social, precise, meta])
        self.assertEqual(result.rules, (social, precise, meta))
        self.assertEqual(len(result.dropped), 1)
        self.assertEqual(result.dropped[0].reason, 'business-category-correction')

    def test_anthropic_telemetry_respects_shared_service_boundary(self):
        from ruleforge.curation import curate_rules
        from ruleforge.model import Rule
        shared = Rule('magicrule-anthropic', 'quantumult-x', 'ai', 'AI',
                      'HOST', 'http-intake.logs.us5.datadoghq.com')
        scoped = Rule('magicrule-anthropic', 'quantumult-x', 'ai', 'AI',
                      'HOST', 'o1158394.ingest.us.sentry.io')
        core = Rule('magicrule-anthropic', 'quantumult-x', 'ai', 'AI',
                    'HOST-SUFFIX', 'anthropic.com')
        reject = Rule('privacy', 'surge', 'privacy', 'reject',
                      'HOST', 'http-intake.logs.us5.datadoghq.com')
        result = curate_rules([shared, scoped, core, reject])
        self.assertEqual(result.rules, (scoped, core, reject))
        self.assertEqual(len(result.dropped), 1)
        self.assertEqual(result.dropped[0].reason, 'business-category-correction')


if __name__ == '__main__':
    unittest.main()
