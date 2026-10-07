import importlib.util
from pathlib import Path
import re
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('build_site', ROOT / 'scripts/build_site.py')
build_site = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build_site)


class SiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        out = Path(cls.tmp.name) / 'site'
        build_site.build(out)
        cls.out = out
        cls.page = (out / 'index.html').read_text()

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_every_rule_has_an_anchor(self):
        for rule in build_site.rulebook.load_rules(build_site.SKILL):
            with self.subTest(rule=rule['id']):
                self.assertIn(f'id="{rule["id"]}"', self.page)

    def test_every_example_is_rendered(self):
        examples = build_site.parse_examples(build_site.SKILL / 'examples/website-copy.md')
        self.assertGreater(len(examples), 0)
        self.assertEqual(self.page.count('class="example"'), len(examples))
        for example in examples:
            self.assertTrue(example['before'])

    def test_redline_marks_only_changes(self):
        self.assertEqual(build_site.diff('a b c', 'a c'), 'a <del>b</del> c')
        self.assertEqual(build_site.diff('Swap design', 'Choose a design'), '<del>Swap</del> <ins>Choose a</ins> design')

    def test_page_is_complete(self):
        self.assertNotRegex(self.page, r'\{\{[A-Z_]+\}\}')
        for href in re.findall(r'(?:href|src)="([^":#?]+)"', self.page):
            with self.subTest(asset=href):
                self.assertTrue((self.out / href).exists())


if __name__ == '__main__':
    unittest.main()
