import copy
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import propose_rule

rules = propose_rule.rules


def form(**overrides):
    answers = {
        "change": "Add a rule", "id": "test-specific-benefit", "title": "State a specific benefit",
        "category": "Writing", "direction": "Do", "scope": "All models",
        "company": "", "model": "", "context": "Product descriptions",
        "rule": "Describe a supported capability.", "example": "Export invoices as CSV.",
        "counterexample": "Unlock a magical invoice experience.", "rationale": "Help readers judge the product.",
        "evidence": "Illustrative example.",
    }
    answers.update(overrides)
    text_fields = {"context", "rule", "example", "counterexample", "rationale", "evidence"}
    return "\n\n".join(f"### {label}\n\n" + (f"```text\n{answers[key]}\n```" if key in text_fields and answers[key]
                                                  else answers[key] or "_No response_")
                          for label, key in propose_rule.LABELS.items())


class RuleTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.skill = Path(self.directory.name) / "deslopify"
        shutil.copytree(ROOT / "deslopify", self.skill)

    def test_add_change_and_rerender_are_deterministic(self):
        change, rule = propose_rule.rule_from_issue({"body": form()}, self.skill)
        path = propose_rule.apply_proposal(self.skill, change, rule)
        self.assertEqual(json.loads(path.read_text()), rule)
        self.assertIn(rule["rule"], (self.skill / rules.guidance_path(rule)).read_text())
        self.assertEqual(rules.sync(self.skill, check=True), [])
        with self.assertRaisesRegex(ValueError, "already exists"):
            propose_rule.rule_from_issue({"body": form()}, self.skill)
        change, updated = propose_rule.rule_from_issue({"body": form(change="Change a rule", rule="Name the capability and its limit.")}, self.skill)
        propose_rule.apply_proposal(self.skill, change, updated)
        self.assertEqual(len([item for item in rules.load_rules(self.skill) if item["id"] == rule["id"]]), 1)
        self.assertEqual(json.loads(path.read_text())["rule"], updated["rule"])
        self.assertEqual(rules.sync(self.skill), [])

    def test_category_direction_and_scope_move_clears_stale_guidance(self):
        change, rule = propose_rule.rule_from_issue({"body": form(scope="One model", company="exampleco", model="example-1")}, self.skill)
        path = propose_rule.apply_proposal(self.skill, change, rule)
        previous = self.skill / rules.guidance_path(rule)
        change, updated = propose_rule.rule_from_issue({"body": form(change="Change a rule", category="Design", direction="Don't")}, self.skill)
        new_path = propose_rule.apply_proposal(self.skill, change, updated)
        self.assertFalse(path.exists())
        self.assertTrue(new_path.exists())
        self.assertEqual(previous.read_text(), "")
        self.assertIn(updated["id"], (self.skill / rules.guidance_path(updated)).read_text())

    def test_selection_combines_only_applicable_scopes(self):
        source = rules.load_rules(self.skill)
        all_ids = {r["id"] for r in source if r["scope"] == "all" and r["category"] == "writing"}
        selected = rules.select(source, "writing", "openai", "gpt-5.4")
        self.assertEqual({r["id"] for r in selected}, all_ids | {"openai-no-unfitting-creatures", "openai-no-unrelated-creatures"})
        self.assertEqual({r["id"] for r in rules.select(source, "writing", None, None)}, all_ids)
        self.assertTrue(all(r["category"] == "design" and r["scope"] == "all" for r in rules.select(source, "design", "unknown", "unknown")))
        with self.assertRaisesRegex(ValueError, "needs its company"):
            rules.select(source, None, None, "gpt-5.4")

    def test_model_state_preserves_existing_slot_or_uses_new(self):
        for model, expected in (("gpt-5.4", "available"), ("gpt-6.1-sol", "new"), ("gpt-4-turbo", "deprecated"), ("unlisted-1", "new")):
            with self.subTest(model=model):
                _, rule = propose_rule.rule_from_issue({"body": form(scope="One model", company="openai", model=model)}, self.skill)
                self.assertEqual(rule["model_state"], expected)
        (self.skill / "fac/_template/models/openai/new/gpt-5.4.md").touch()
        with self.assertRaisesRegex(ValueError, "multiple catalog states"):
            propose_rule.rule_from_issue({"body": form(scope="One model", company="openai", model="gpt-5.4")}, self.skill)

    def test_invalid_scopes_and_path_inputs_are_rejected_without_writes(self):
        before = set(self.skill.rglob("*.json"))
        for overrides in (
            {"scope": "One model"}, {"scope": "One company"},
            {"company": "openai"}, {"model": "gpt-5.4"},
            {"id": "../../outside"}, {"id": "Mixed_Case"},
            {"scope": "One model", "company": "../outside", "model": "example-1"},
            {"scope": "One model", "company": "openai", "model": "$(touch bad)"},
            {"example": ""}, {"counterexample": "Export invoices as CSV."},
            {"change": "Change a rule"}, {"category": "Unclassified"},
        ):
            with self.subTest(overrides=overrides), self.assertRaises(ValueError):
                propose_rule.rule_from_issue({"body": form(**overrides)}, self.skill)
        self.assertEqual(before, set(self.skill.rglob("*.json")))

    def test_fenced_multiline_text_is_data(self):
        example = '### Category\n\nDesign\n$(touch /tmp/unwanted)\n"quoted"\n`literal`'
        _, rule = propose_rule.rule_from_issue({"body": form(example=example, evidence="")}, self.skill)
        self.assertEqual(rule["example"], example)
        self.assertEqual(rule["category"], "writing")
        self.assertEqual(rule["evidence"], "")
        self.assertEqual(propose_rule.parse_form(form())["rule"], "Describe a supported capability.")

    def test_ambiguous_or_incomplete_form_is_rejected(self):
        for body in (form() + "\n\n### Category\n\nDesign", form().replace("### Rule ID", "### Unknown"),
                     form().replace("### Rule ID\n\ntest-specific-benefit\n\n", ""), form() + "\n\n```text\nunterminated"):
            with self.subTest(body=body[-100:]), self.assertRaises(ValueError):
                propose_rule.parse_form(body)

    def test_stale_generated_output_and_duplicate_ids_are_detected(self):
        path = self.skill / "fac/_template/general.md"
        path.write_text(path.read_text() + "\nManual stale edit\n")
        self.assertIn(path.relative_to(self.skill), rules.sync(self.skill, check=True))
        rules.sync(self.skill)
        self.assertEqual(rules.sync(self.skill, check=True), [])
        record = copy.deepcopy(rules.load_rules(self.skill)[0])
        record["category"] = "design" if record["category"] != "design" else "writing"
        duplicate = self.skill / rules.source_path(record)
        duplicate.parent.mkdir(parents=True, exist_ok=True)
        duplicate.write_text(json.dumps(record))
        with self.assertRaisesRegex(ValueError, "duplicate rule id"):
            rules.load_rules(self.skill)

    def test_installed_helper_runs_without_repository_files(self):
        import subprocess
        output = subprocess.check_output([sys.executable, str(self.skill / "scripts/rules.py"), "select",
                                          "--category", "design", "--format", "json"], text=True)
        selected = json.loads(output)
        self.assertTrue(selected)
        self.assertTrue(all(r["category"] == "design" for r in selected))


if __name__ == "__main__":
    unittest.main()
