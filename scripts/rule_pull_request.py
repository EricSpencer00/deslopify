#!/usr/bin/env python3
"""GitHub Actions entry point: one reviewed issue, one reusable proposal PR."""

from __future__ import annotations

import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

from propose_rule import ROOT, apply_proposal, rule_from_issue, rules


def command(*args: str) -> str:
    result = subprocess.run(args, cwd=ROOT, text=True, capture_output=True, check=True)
    return result.stdout.strip()


def allowed_path(path: str, rule_id: str) -> bool:
    if path == "MODEL-CATALOG.md" or path in ("deslopify/references/rule-index.md", "deslopify/references/rule-index.json"):
        return True
    if path in {f"deslopify/rules/{category}/{rule_id}.json" for category in rules.CATEGORIES}:
        return True
    return bool(re.fullmatch(r"deslopify/(fac|ne-fac)/_template/(general\.md|models/[a-z0-9.-]+/(general\.md|(new|available|deprecated)/[a-z0-9.-]+\.md))", path))


def merge_default(base: str) -> None:
    try:
        command("git", "merge", "--no-edit", f"origin/{base}")
    except subprocess.CalledProcessError:
        conflicts = command("git", "diff", "--name-only", "--diff-filter=U").splitlines()
        if not conflicts or any(path.startswith("deslopify/rules/") or not allowed_path(path, "") for path in conflicts):
            raise ValueError("proposal has an authored-file merge conflict; resolve it manually before rerunning")
        # Source records have merged cleanly. Rebuild conflicting derived files
        # from those records instead of asking a person to merge rendered text.
        command("git", "checkout", "--theirs", "--", *conflicts)
        rules.sync(ROOT / "deslopify")
        command(sys.executable, "scripts/update_readme_tree.py")
        command("git", "add", "--", *conflicts, "deslopify/fac", "deslopify/ne-fac", "deslopify/references", "MODEL-CATALOG.md")
        command("git", "commit", "-m", "Merge accepted rules and regenerate guidance")


def check_branch_paths(branch: str, base: str, rule_id: str) -> None:
    # Only data/generated files may differ. Never run scripts or tests supplied
    # by a proposal branch with a write token.
    paths = command("git", "diff", "--name-only", f"origin/{base}...origin/{branch}").splitlines()
    if any(not allowed_path(path, rule_id) for path in paths):
        raise ValueError("proposal branch contains unrelated changes; review it manually before rerunning")
    for path in paths:
        entry = command("git", "ls-tree", f"origin/{branch}", "--", path)
        if entry and not entry.startswith("100644 blob "):
            raise ValueError("proposal branch contains a non-regular data file")


def main() -> int:
    number = os.environ.get("ISSUE_NUMBER", "")
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    base = os.environ.get("DEFAULT_BRANCH", "main")
    if not re.fullmatch(r"[1-9][0-9]*", number) or not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
        raise ValueError("provide a positive issue number and GITHUB_REPOSITORY")
    command("git", "check-ref-format", "--branch", base)
    issue = json.loads(command("gh", "api", f"repos/{repo}/issues/{number}"))
    if issue.get("pull_request") or issue.get("state") != "open":
        raise ValueError("choose an open rule issue, not a pull request")
    change, rule = rule_from_issue(issue, ROOT / "deslopify")
    branch = f"rule-proposal/issue-{number}"
    prs = json.loads(command("gh", "pr", "list", "--repo", repo, "--head", branch,
                             "--state", "all", "--json", "number,state,body,url"))
    if any(pr["state"] != "OPEN" for pr in prs):
        raise ValueError("this issue already has a closed or merged proposal; open a new change issue")
    if len(prs) > 1:
        raise ValueError("multiple proposal PRs found; resolve them before rerunning")
    marker = f"<!-- deslopify-rule-id: {rule['id']} -->"
    if prs and marker not in prs[0]["body"]:
        raise ValueError("keep the proposal's Rule ID stable; open a new issue to propose a different rule")
    command("git", "config", "user.name", "github-actions[bot]")
    command("git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
    command("git", "fetch", "origin", base)
    exists = bool(command("git", "ls-remote", "--heads", "origin", f"refs/heads/{branch}"))
    if exists:
        command("git", "fetch", "origin", f"{branch}:refs/remotes/origin/{branch}")
        check_branch_paths(branch, base, rule["id"])
        command("git", "switch", "--create", branch, f"origin/{branch}")
        merge_default(base)
    else:
        if prs:
            raise ValueError("proposal PR is missing its branch; restore it before rerunning")
        command("git", "switch", "--create", branch, f"origin/{base}")
    current = next((item for item in rules.load_rules(ROOT / "deslopify") if item["id"] == rule["id"]), None)
    # The default-branch validation above decides whether this is an add/change.
    # An earlier successful run may already have added the rule to this branch.
    apply_proposal(ROOT / "deslopify", "update" if current else "add", rule)
    command(sys.executable, "scripts/validate_content.py")
    command(sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v")
    command(sys.executable, "scripts/update_readme_tree.py")
    paths = command("git", "diff", "--name-only").splitlines()
    untracked = command("git", "ls-files", "--others", "--exclude-standard").splitlines()
    if any(not allowed_path(path, rule["id"]) for path in paths + untracked):
        raise ValueError("generation changed an unexpected path")
    command("git", "add", "--", "deslopify/rules", "deslopify/references", "deslopify/fac", "deslopify/ne-fac", "MODEL-CATALOG.md")
    if command("git", "diff", "--cached", "--name-only"):
        command("git", "commit", "-m", f"{change.title()} rule {rule['id']} from issue #{number}")
    elif not prs and not exists:
        raise ValueError("the proposal makes no change to the current catalog")
    artifact = Path(os.environ.get("RUNNER_TEMP", tempfile.gettempdir())) / "rule-proposal.patch"
    artifact.write_text(command("git", "diff", "--binary", f"origin/{base}...HEAD") + "\n", encoding="utf-8")
    command("git", "push", "origin", f"HEAD:refs/heads/{branch}")
    body = (f"{marker}\n{change.title()} `{rule['id']}` from the structured issue form.\n\n"
            f"Category: **{rule['category']}**. Direction: **{rule['direction']}**. Scope: **{rules.scope_label(rule)}**.\n\n"
            "Includes one example and one counterexample. Generated guidance and the rule index are refreshed.\n\n"
            "Validation: rule records, installed-skill references, preservation fixtures, and the test suite passed. "
            "These checks validate structure and existing regressions; the rule's usefulness still needs review.\n\n"
            f"Closes #{number}.\n")
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", suffix=".md") as file:
        file.write(body)
        file.flush()
        if prs:
            command("gh", "pr", "edit", str(prs[0]["number"]), "--repo", repo, "--body-file", file.name)
            url = prs[0]["url"]
        else:
            url = command("gh", "pr", "create", "--repo", repo, "--base", base, "--head", branch,
                          "--title", f"{change.title()} rule: {rule['title']}", "--body-file", file.name)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as file:
            file.write(f"Proposal ready: {url}\n\nReview the example pair and scope, then merge the PR to apply the rule.\n")
    print(url)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        # Do not echo token-bearing command environment or full API responses.
        detail = f"command exited {error.returncode}: {error.cmd[0]}" if isinstance(error, subprocess.CalledProcessError) else str(error)
        print(f"Proposal failed: {detail}. See CONTRIBUTING.md for rerun and permissions guidance.", file=sys.stderr)
        raise SystemExit(1)
