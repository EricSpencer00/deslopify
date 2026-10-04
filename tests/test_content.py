import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('validation', ROOT / 'scripts/validate_content.py')
validation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validation)


class ContentTests(unittest.TestCase):
    def test_regression_fixtures_and_lossy_edits(self):
        for case in json.loads((ROOT / 'tests/fixtures/rewrites.json').read_text()):
            with self.subTest(case=case['id']):
                self.assertEqual(validation.preservation_errors(case, case['after']), [])
                if case['preserve']:
                    self.assertTrue(validation.preservation_errors(case, case['after'].replace(case['preserve'][0], '', 1)))
                else:
                    self.assertTrue(case['omit_entirely'])
                    self.assertTrue(validation.preservation_errors(case, case['before']))
                self.assertTrue(validation.preservation_errors(case, case['after'] + ' 999'))
                self.assertTrue(validation.preservation_errors(case, case['after'] + ' https://example.org/invented'))

    def test_intent_and_qualification_reversals(self):
        cases = {case['id']: case for case in json.loads((ROOT / 'tests/fixtures/rewrites.json').read_text())}
        reversals = (
            ('email', 'could you review', 'please do not review'),
            ('website', 'exports CSV reports', 'deletes CSV reports'),
            ('technical', 'reduced p95 latency', 'increased p95 latency'),
            ('technical', 'have not tested concurrent writes', 'tested concurrent writes'),
            ('qualification', 'did not measure peak RSS', 'measured peak RSS'),
        )
        for case_id, before, after in reversals:
            with self.subTest(case=case_id, mutation=after):
                case = cases[case_id]
                candidate = case['after'].replace(before, after)
                self.assertNotEqual(candidate, case['after'])
                self.assertTrue(validation.preservation_errors(case, candidate))

    def test_frontend_diagnostics_and_useful_specs(self):
        cases = {case['id']: case for case in json.loads((ROOT / 'tests/fixtures/rewrites.json').read_text())}
        case = cases['frontend-diagnostics']
        self.assertEqual(validation.preservation_errors(case, case['after']), [])
        for candidate in (
            case['before'],
            case['after'] + ' / 240 rendered',
            case['after'].replace('Choose a design', 'No designs available'),
        ):
            with self.subTest(candidate=candidate):
                self.assertTrue(validation.preservation_errors(case, candidate))
        unsupported = {**case, 'remove_internal_diagnostics': ['999 rendered']}
        self.assertIn('diagnostic fixture lacks unique source support',
                      validation.preservation_errors(unsupported, case['after']))
        useful = cases['website']
        for candidate in (
            useful['after'].replace('CSV', 'JSON'),
            useful['after'].replace('20 projects', '200 projects'),
        ):
            with self.subTest(useful_spec=candidate):
                self.assertTrue(validation.preservation_errors(useful, candidate))

    def test_every_preservation_anchor_is_enforced(self):
        for case in json.loads((ROOT / 'tests/fixtures/rewrites.json').read_text()):
            for token in case['preserve']:
                with self.subTest(case=case['id'], token=token):
                    self.assertIn(token, case['before'])
                    self.assertIn(token, case['after'])
                    self.assertTrue(validation.preservation_errors(case, case['after'].replace(token, '', 1)))
            if 'intent' in case:
                self.assertIn(case['intent']['source'], case['before'])
                self.assertIn(case['intent']['candidate'], case['after'])
                self.assertTrue(validation.preservation_errors(case, case['after'].replace(case['intent']['candidate'], '', 1)))

    def test_unneeded_notice_omitted_and_critical_warnings_kept(self):
        cases = {case['id']: case for case in json.loads((ROOT / 'tests/fixtures/rewrites.json').read_text())}
        notice = cases['obsolete-notice']
        self.assertEqual(validation.preservation_errors(notice, ''), [])
        self.assertIn('unneeded notice rewritten instead of omitted',
                      validation.preservation_errors(notice, 'The home page now contains every section. Start there.'))
        warning = cases['migration-warning']
        self.assertEqual(validation.preservation_errors(warning, warning['before']), [])
        self.assertTrue(validation.preservation_errors(warning, ''))
        for token in warning['preserve']:
            with self.subTest(required_warning=token):
                self.assertTrue(validation.preservation_errors(warning, warning['after'].replace(token, '', 1)))

    def test_audience_omissions_keep_needed_context(self):
        cases = {case['id']: case for case in json.loads((ROOT / 'tests/fixtures/rewrites.json').read_text())}
        for case_id in ('frontend-redundancy', 'about-overview', 'audience-letter'):
            case = cases[case_id]
            with self.subTest(case=case_id):
                self.assertEqual(validation.preservation_errors(case, case['after']), [])
                self.assertIn('redundant UI copy remains',
                              validation.preservation_errors(case, case['before']))
                for token in case['preserve']:
                    with self.subTest(needed_context=token):
                        self.assertTrue(validation.preservation_errors(case, case['after'].replace(token, '', 1)))
                unsupported = {**case, 'remove_redundant_copy': ['Missing heading']}
                self.assertIn('redundancy fixture lacks unique source support',
                              validation.preservation_errors(unsupported, case['after']))

    def test_installation_and_explicit_invocation_routing(self):
        # Offline package smoke: temporary project installation, $name lookup,
        # and all linked guidance resolution. Does not call a language model.
        with tempfile.TemporaryDirectory() as directory:
            installed = Path(directory) / '.agents/skills/deslopify'
            shutil.copytree(ROOT / 'deslopify', installed)
            prompt = '$deslopify Tighten this email while preserving its facts.'
            skill_name = prompt.split()[0][1:]
            resolved = installed.parent / skill_name
            visited = validation.validate_skill(resolved)
            self.assertEqual(len(visited), 4)
            self.assertIn((resolved / 'examples/website-copy.md').resolve(), visited)
            (resolved / 'examples/website-copy.md').write_text('')
            with self.assertRaises(ValueError):
                validation.validate_skill(resolved)

    def test_directory_reference_cannot_escape_installed_skill(self):
        with tempfile.TemporaryDirectory() as directory:
            installed = Path(directory) / '.agents/skills/deslopify'
            shutil.copytree(ROOT / 'deslopify', installed)
            (Path(directory) / 'outside').mkdir()
            entry = installed / 'SKILL.md'
            entry.write_text(entry.read_text() + '\n[outside](../../../outside)\n')
            with self.assertRaisesRegex(ValueError, 'reference escapes installed skill'):
                validation.validate_skill(installed)


if __name__ == '__main__':
    unittest.main()
