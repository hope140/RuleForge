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


if __name__ == '__main__':
    unittest.main()
