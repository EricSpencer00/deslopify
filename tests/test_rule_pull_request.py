import copy
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from test_rules import ROOT, form
import rule_pull_request as workflow


class ProposalWorkflowTests(unittest.TestCase):
    """Real local Git operations; GitHub requests are simulated without a token."""

    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        parent = Path(self.directory.name)
        self.root = parent / "checkout"
        self.remote = parent / "remote.git"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        self.git("init", "--initial-branch=main")
        # Fixture commits must not invoke the maintainer's signing key or hooks.
        self.git("config", "commit.gpgsign", "false")
        self.git("config", "core.hooksPath", str(parent / "no-hooks"))
        self.git("config", "user.name", "Test maintainer")
        self.git("config", "user.email", "test@example.org")
        self.git("add", ".")
        self.git("commit", "-m", "Initial test catalog")
        subprocess.run(["git", "init", "--bare", str(self.remote)], check=True, capture_output=True)
        self.git("remote", "add", "origin", str(self.remote))
        self.git("push", "origin", "main")
        self.git("fetch", "origin")
        self.issue = {"number": 7, "state": "open", "body": form()}
        self.prs = []
        self.requests = []
        self.fail_creation = False

    def git(self, *args):
        return subprocess.check_output(["git", *args], cwd=self.root, text=True, stderr=subprocess.DEVNULL).strip()

    def command(self, *args):
        if args[0] == "git":
            return self.git(*args[1:])
        if args[0] == sys.executable:
            # The parser/renderer run for real in main(). Their validators and
            # installation tests have their own tests; avoid recursively running
            # this workflow test suite in the fixture checkout.
            self.requests.append(args)
            return ""
        self.assertEqual(args[0], "gh")
        self.requests.append(args)
        if args[1] == "api":
            return json.dumps(self.issue)
        if args[2] == "list":
            return json.dumps(self.prs)
        if args[2] == "create":
            if self.fail_creation:
                raise subprocess.CalledProcessError(1, args)
            body = Path(args[args.index("--body-file") + 1]).read_text()
            self.prs = [{"number": 11, "state": "OPEN", "body": body,
                         "url": "https://github.com/example/repo/pull/11"}]
            return self.prs[0]["url"]
        if args[2] == "edit":
            self.prs[0]["body"] = Path(args[args.index("--body-file") + 1]).read_text()
            return ""
        self.fail(f"unexpected GitHub operation: {args[:3]}")

    def run_workflow(self):
        # Each Actions run begins on the trusted default branch.
        self.git("switch", "main")
        branch = "rule-proposal/issue-7"
        if branch in self.git("branch", "--format=%(refname:short)").splitlines():
            self.git("branch", "-D", branch)
        with patch.object(workflow, "ROOT", self.root), patch.object(workflow, "command", self.command), \
             patch.dict(os.environ, {"ISSUE_NUMBER": "7", "GITHUB_REPOSITORY": "example/repo",
                                     "DEFAULT_BRANCH": "main", "RUNNER_TEMP": self.directory.name,
                                     "GITHUB_STEP_SUMMARY": str(Path(self.directory.name) / "summary.md")}):
            return workflow.main()

    def test_add_rerun_and_revision_reuse_one_pr_without_force(self):
        self.assertEqual(self.run_workflow(), 0)
        first = self.git("rev-parse", "HEAD")
        self.assertEqual(self.run_workflow(), 0)
        self.assertEqual(self.git("rev-parse", "HEAD"), first)
        self.assertEqual(len([r for r in self.requests if r[:3] == ("gh", "pr", "create")]), 1)
        self.issue["body"] = form(category="Design", direction="Don't", rule="Keep the control understandable.")
        self.assertEqual(self.run_workflow(), 0)
        self.assertEqual(self.git("merge-base", first, "HEAD"), first)
        self.assertFalse((self.root / "deslopify/rules/writing/test-specific-benefit.json").exists())
        changed = self.root / "deslopify/rules/design/test-specific-benefit.json"
        self.assertEqual(json.loads(changed.read_text())["direction"], "dont")
        self.assertEqual(len(self.prs), 1)
        self.assertIn("Closes #7", self.prs[0]["body"])
        self.assertTrue((Path(self.directory.name) / "rule-proposal.patch").stat().st_size)

    def test_change_existing_rule(self):
        self.issue["body"] = form(change="Change a rule", id="openai-no-unfitting-creatures",
                                  scope="One company", company="openai", direction="Don't")
        self.assertEqual(self.run_workflow(), 0)
        records = workflow.rules.load_rules(self.root / "deslopify")
        record = next(r for r in records if r["id"] == "openai-no-unfitting-creatures")
        self.assertEqual(record["rule"], "Describe a supported capability.")
        self.assertEqual(len(records), 33)

    def test_rerun_merges_other_accepted_rules_and_rebuilds_conflicts(self):
        self.run_workflow()
        proposal_head = self.git("rev-parse", "HEAD")
        self.git("switch", "main")
        change, rule = workflow.rule_from_issue({"body": form(id="another-accepted-rule")}, self.root / "deslopify")
        workflow.apply_proposal(self.root / "deslopify", change, rule)
        self.git("add", "deslopify")
        self.git("commit", "-m", "Accept another rule")
        accepted_head = self.git("rev-parse", "HEAD")
        self.git("push", "origin", "main")
        self.assertEqual(self.run_workflow(), 0)
        ids = {r["id"] for r in workflow.rules.load_rules(self.root / "deslopify")}
        self.assertIn("another-accepted-rule", ids)
        self.assertIn("test-specific-benefit", ids)
        self.assertEqual(self.git("merge-base", proposal_head, "HEAD"), proposal_head)
        self.assertEqual(self.git("merge-base", accepted_head, "HEAD"), accepted_head)
        self.assertEqual(workflow.rules.sync(self.root / "deslopify", check=True), [])

    def test_conflicting_authored_rule_is_not_overwritten(self):
        self.issue["body"] = form(change="Change a rule", id="cut-repetition")
        self.run_workflow()
        self.git("switch", "main")
        change, rule = workflow.rule_from_issue({"body": form(change="Change a rule", id="cut-repetition", rule="A different accepted revision.")}, self.root / "deslopify")
        workflow.apply_proposal(self.root / "deslopify", change, rule)
        self.git("add", "deslopify")
        self.git("commit", "-m", "Accept a different revision")
        self.git("push", "origin", "main")
        with self.assertRaisesRegex(ValueError, "authored-file merge conflict"):
            self.run_workflow()

    def test_unrelated_branch_code_is_not_executed_on_rerun(self):
        self.run_workflow()
        (self.root / "scripts/validate_content.py").write_text("raise RuntimeError('untrusted')\n")
        self.git("add", "scripts/validate_content.py")
        self.git("commit", "-m", "Unrelated branch code")
        self.git("push", "origin", "HEAD:rule-proposal/issue-7")
        old_requests = len(self.requests)
        with self.assertRaisesRegex(ValueError, "unrelated changes"):
            self.run_workflow()
        self.assertFalse(any(r[0] == sys.executable for r in self.requests[old_requests:]))

    def test_closed_or_changed_identity_proposal_stops(self):
        self.run_workflow()
        original = copy.deepcopy(self.prs)
        self.prs[0]["state"] = "MERGED"
        with self.assertRaisesRegex(ValueError, "closed or merged"):
            self.run_workflow()
        self.prs = original
        self.issue["body"] = form(id="a-different-rule")
        with self.assertRaisesRegex(ValueError, "Rule ID stable"):
            self.run_workflow()

    def test_creation_failure_keeps_patch_and_retries_existing_branch(self):
        self.fail_creation = True
        with self.assertRaises(subprocess.CalledProcessError):
            self.run_workflow()
        self.assertTrue((Path(self.directory.name) / "rule-proposal.patch").stat().st_size)
        head = self.git("rev-parse", "HEAD")
        self.fail_creation = False
        self.assertEqual(self.run_workflow(), 0)
        self.assertEqual(self.git("rev-parse", "HEAD"), head)
        self.assertEqual(len(self.prs), 1)


if __name__ == "__main__":
    unittest.main()
