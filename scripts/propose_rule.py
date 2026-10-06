#!/usr/bin/env python3
"""Convert a GitHub issue-form response into a validated add/update of one rule."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "deslopify/scripts"))
import rules

LABELS = {
    "Change": "change", "Rule ID": "id", "Rule title": "title",
    "Category": "category", "Direction": "direction", "Applies to": "scope",
    "Company": "company", "Model": "model", "When does this apply?": "context",
    "The rule": "rule", "Example that follows the rule": "example",
    "Counterexample that breaks the rule": "counterexample",
    "Why is this useful?": "rationale", "Evidence or links (optional)": "evidence",
}


def parse_form(body: str) -> dict[str, str]:
    if not isinstance(body, str) or len(body) > 100000:
        raise ValueError("issue body must be text of at most 100000 characters")
    sections: dict[str, list[str]] = {}
    current = None
    fence = None
    for line in body.splitlines():
        delimiter = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if delimiter:
            if fence is None:
                fence = delimiter[1]
            elif delimiter[1][0] == fence[0] and len(delimiter[1]) >= len(fence) and not delimiter[2].strip():
                fence = None
        heading = re.fullmatch(r"### (.+)", line) if fence is None and not delimiter else None
        if heading:
            label = heading[1]
            if label not in LABELS:
                raise ValueError(f"unexpected form field: {label}")
            current = LABELS[label]
            if current in sections:
                raise ValueError(f"duplicate form field: {label}")
            sections[current] = []
        elif current:
            sections[current].append(line)
    if fence:
        raise ValueError("unclosed code fence in issue response")
    missing = set(LABELS.values()) - sections.keys()
    if missing:
        raise ValueError(f"use the rule issue form; missing fields: {', '.join(sorted(missing))}")
    result = {}
    for key, lines in sections.items():
        value = "\n".join(lines).strip()
        # GitHub wraps textarea fields with render: text in a code fence.
        wrapped = re.fullmatch(r"(`{3,}|~{3,})[^\n]*\n(.*)\n\1", value, re.DOTALL)
        if wrapped:
            value = wrapped[2].strip()
        result[key] = "" if value == "_No response_" else value
    return result


def rule_from_issue(issue: dict, skill: Path) -> tuple[str, dict]:
    values = parse_form(issue.get("body"))
    change = {"Add a rule": "add", "Change a rule": "update"}.get(values.pop("change"))
    if not change:
        raise ValueError("Change must be Add a rule or Change a rule")
    directions = {"Do": "do", "Don't": "dont"}
    scopes = {"All models": "all", "One company": "company", "One model": "model"}
    if values["direction"] not in directions or values["scope"] not in scopes:
        raise ValueError("choose a direction and scope from the form dropdowns")
    values["direction"] = directions[values["direction"]]
    values["scope"] = scopes[values["scope"]]
    values["category"] = values["category"].lower()
    for field in ("company", "model"):
        values[field] = values[field] or None
    existing = next((rule for rule in rules.load_rules(skill) if rule["id"] == values["id"]), None)
    if change == "add" and existing:
        raise ValueError(f"{values['id']} already exists; choose Change a rule")
    if change == "update" and not existing:
        raise ValueError(f"{values['id']} does not exist; choose Add a rule")
    values["model_state"] = None
    if values["scope"] == "model":
        # Validate slugs before using them in any filesystem path.
        for field in ("company", "model"):
            if not values[field] or not rules.SLUG.fullmatch(values[field]) or len(values[field]) > 64:
                raise ValueError(f"model scope needs a lowercase {field} slug")
        if existing and existing["company"] == values["company"] and existing["model"] == values["model"]:
            values["model_state"] = existing["model_state"]
        if not values["model_state"]:
            states = {state for state in rules.STATES for direction in ("fac", "ne-fac")
                      if (skill / direction / "_template/models" / values["company"] / state / f"{values['model']}.md").is_file()}
            if len(states) > 1:
                raise ValueError("model appears in multiple catalog states; resolve its slots before proposing a rule")
            values["model_state"] = next(iter(states), "new")
    rules.validate_rule(values)
    return change, values


def apply_proposal(skill: Path, change: str, rule: dict) -> Path:
    rules.validate_rule(rule)
    existing = next((item for item in rules.load_rules(skill) if item["id"] == rule["id"]), None)
    if (change == "add" and existing) or (change == "update" and not existing):
        raise ValueError("proposal no longer matches the current rule catalog")
    path = skill / rules.source_path(rule)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(rule, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if existing and rules.source_path(existing) != rules.source_path(rule):
        (skill / rules.source_path(existing)).unlink()
    rules.sync(skill)
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--issue-json", type=Path, required=True, help="issue JSON, or a GitHub event JSON containing issue")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--dry-run", action="store_true", help="validate and print the record without writing files")
    args = parser.parse_args()
    try:
        payload = json.loads(args.issue_json.read_text(encoding="utf-8"))
        issue = payload.get("issue", payload)
        change, rule = rule_from_issue(issue, args.root / "deslopify")
        if args.dry_run:
            print(json.dumps({"change": change, "rule": rule}, ensure_ascii=False, indent=2))
        else:
            path = apply_proposal(args.root / "deslopify", change, rule)
            print(f"{change}: {path.relative_to(args.root)}")
    except (ValueError, OSError) as error:
        print(f"Proposal error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
