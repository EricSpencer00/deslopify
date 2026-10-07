#!/usr/bin/env python3
"""Validate, render, and select the skill's canonical rule records (stdlib only)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

SKILL = Path(__file__).resolve().parents[1]
CATEGORIES = ("writing", "taste", "design")
STATES = ("new", "available", "deprecated")
MARKER = "<!-- Generated from rules/*.json. Edit the rule record, then regenerate. -->"
SLUG = re.compile(r"[a-z0-9]+(?:[.-][a-z0-9]+)*")
FIELDS = {"id", "title", "category", "direction", "scope", "company", "model",
          "model_state", "context", "rule", "example", "counterexample", "rationale", "evidence"}


def validate_rule(rule: dict) -> None:
    if not isinstance(rule, dict) or set(rule) != FIELDS:
        raise ValueError(f"rule must contain exactly: {', '.join(sorted(FIELDS))}")
    for field in ("id", "title", "context", "rule", "example", "counterexample", "rationale"):
        value = rule[field]
        if not isinstance(value, str) or not value.strip() or len(value) > 8000:
            raise ValueError(f"{field} must be nonempty text of at most 8000 characters")
    if not isinstance(rule["evidence"], str) or len(rule["evidence"]) > 8000:
        raise ValueError("evidence must be text of at most 8000 characters")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", rule["id"]) or len(rule["id"]) > 64:
        raise ValueError("id must be a lowercase hyphenated slug of at most 64 characters")
    if len(rule["title"]) > 120 or "\n" in rule["title"] or "\r" in rule["title"]:
        raise ValueError("title must be one line of at most 120 characters")
    if rule["category"] not in CATEGORIES or rule["direction"] not in ("do", "dont"):
        raise ValueError("choose writing/taste/design and do/dont")
    if rule["scope"] not in ("all", "company", "model"):
        raise ValueError("scope must be all, company, or model")
    for field in ("company", "model"):
        value = rule[field]
        if value is not None and (not isinstance(value, str) or len(value) > 64 or not SLUG.fullmatch(value)):
            raise ValueError(f"{field} must be a lowercase slug or null")
    if rule["scope"] == "all":
        if any(rule[f] is not None for f in ("company", "model", "model_state")):
            raise ValueError("all-model rules must leave company, model, and model_state null")
    elif rule["scope"] == "company":
        if not rule["company"] or rule["model"] is not None or rule["model_state"] is not None:
            raise ValueError("company rules need a company and no model or model_state")
    elif not rule["company"] or not rule["model"] or rule["model_state"] not in STATES:
        raise ValueError("model rules need company, model, and new/available/deprecated model_state")
    if rule["example"].strip() == rule["counterexample"].strip():
        raise ValueError("example and counterexample must show different outcomes")


def source_path(rule: dict) -> Path:
    return Path("rules") / rule["category"] / f"{rule['id']}.json"


def load_rules(skill: Path = SKILL) -> list[dict]:
    rules = []
    seen = set()
    for path in sorted((skill / "rules").rglob("*.json")):
        rule = json.loads(path.read_text(encoding="utf-8"))
        validate_rule(rule)
        if path.relative_to(skill) != source_path(rule):
            raise ValueError(f"{path}: path must match the rule category and id")
        if rule["id"] in seen:
            raise ValueError(f"duplicate rule id: {rule['id']}")
        seen.add(rule["id"])
        rules.append(rule)
    if not rules:
        raise ValueError("no rule records found")
    return sorted(rules, key=lambda r: (("all", "company", "model").index(r["scope"]),
                                       r["company"] or "", r["model"] or "", r["id"]))


def guidance_path(rule: dict) -> Path:
    path = Path("fac" if rule["direction"] == "do" else "ne-fac") / "_template"
    if rule["scope"] == "all":
        return path / "general.md"
    path = path / "models" / rule["company"]
    if rule["scope"] == "company":
        return path / "general.md"
    return path / rule["model_state"] / f"{rule['model']}.md"


def scope_label(rule: dict) -> str:
    if rule["scope"] == "all":
        return "All models"
    if rule["scope"] == "company":
        return f"Company: {rule['company']}"
    return f"Model: {rule['company']} / {rule['model']} ({rule['model_state']})"


def render_rule(rule: dict) -> str:
    return "\n".join((
        f"## {rule['title']} (`{rule['id']}`)", "",
        f"**{rule['category'].title()} · {'Do' if rule['direction'] == 'do' else 'Don’t'} · {scope_label(rule)}**",
        "", f"**When:** {rule['context']}", "", rule["rule"], "",
        f"**Example — follows the rule:**\n\n{rule['example']}", "",
        f"**Counterexample — breaks the rule:**\n\n{rule['counterexample']}", "",
        f"**Why:** {rule['rationale']}",
        *( ("", f"**Evidence / source:** {rule['evidence']}") if rule["evidence"] else () ),
    ))


def generated_files(rules: list[dict]) -> dict[Path, str]:
    groups: dict[Path, list[dict]] = {}
    for rule in rules:
        groups.setdefault(guidance_path(rule), []).append(rule)
    outputs = {
        path: MARKER + "\n\n" + "\n\n".join(render_rule(rule) for rule in group) + "\n"
        for path, group in groups.items()
    }
    lines = [MARKER, "", "# Rule index", "",
             "Read all-model rules plus the matching company and model rules. Apply only the category and context needed for the task.", "",
             "Examples are illustrative; they are not model benchmark results.", "",
             "| ID | Category | Direction | Scope |", "| --- | --- | --- | --- |"]
    for rule in rules:
        lines.append(f"| [{rule['id']}](../{guidance_path(rule).as_posix()}) | {rule['category']} | {rule['direction']} | {scope_label(rule)} |")
    outputs[Path("references/rule-index.md")] = "\n".join(lines) + "\n"
    outputs[Path("references/rule-index.json")] = json.dumps(
        {"schema_version": 1, "rules": [{**rule, "source": source_path(rule).as_posix(),
                                         "guidance": guidance_path(rule).as_posix()} for rule in rules]},
        ensure_ascii=False, indent=2) + "\n"
    return outputs


def sync(skill: Path = SKILL, *, check: bool = False) -> list[Path]:
    outputs = generated_files(load_rules(skill))
    # A removed or moved rule must not leave old guidance active. Preserve empty
    # catalog slots; never delete unrelated authored Markdown.
    for directory in ("fac", "ne-fac"):
        for path in (skill / directory).rglob("*.md"):
            relative = path.relative_to(skill)
            if path.read_text(encoding="utf-8").startswith(MARKER) and relative not in outputs:
                outputs[relative] = ""
    changed = []
    for relative, content in outputs.items():
        path = skill / relative
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            changed.append(relative)
            if not check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
    return changed


def select(rules: list[dict], category: str | None, company: str | None, model: str | None) -> list[dict]:
    if model and not company:
        raise ValueError("a model needs its company to avoid ambiguous matches")
    return [rule for rule in rules
            if (category is None or rule["category"] == category)
            and (rule["scope"] == "all"
                 or (rule["company"] == company and (rule["scope"] == "company" or rule["model"] == model)))]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill", type=Path, default=SKILL)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("validate")
    render = commands.add_parser("render")
    render.add_argument("--check", action="store_true")
    query = commands.add_parser("select")
    query.add_argument("--category", choices=CATEGORIES)
    query.add_argument("--company")
    query.add_argument("--model")
    query.add_argument("--format", choices=("markdown", "json"), default="markdown")
    args = parser.parse_args()
    try:
        rules = load_rules(args.skill)
        if args.command == "validate":
            print(f"Validated {len(rules)} rule records.")
        elif args.command == "render":
            changed = sync(args.skill, check=args.check)
            for path in changed:
                print(f"{'stale' if args.check else 'updated'}: {path}")
            return int(args.check and bool(changed))
        else:
            selected = select(rules, args.category, args.company, args.model)
            print(json.dumps(selected, ensure_ascii=False, indent=2) if args.format == "json"
                  else "\n\n".join(render_rule(rule) for rule in selected))
    except (ValueError, OSError) as error:
        print(f"Rule error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
