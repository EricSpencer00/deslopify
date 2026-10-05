#!/usr/bin/env python3
"""Validate maintained guidance, local reference routing, and rewrite fixtures.

Fixture checks protect known facts, not arbitrary semantics or authorship.
"""
import json
from pathlib import Path
import re
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]


def preservation_errors(case, candidate):
    errors = [f'missing: {token}' for token in case['preserve'] if token not in candidate]
    if case.get('omit_entirely') and candidate.strip():
        errors.append('unneeded notice rewritten instead of omitted')
    if 'intent' in case:
        intent = case['intent']
        if intent['source'] not in case['before']:
            errors.append('intent fixture lacks source support')
        if intent['candidate'] not in candidate:
            errors.append('request intent changed')
    for redundant in case.get('remove_redundant_copy', []):
        if not redundant or case['before'].count(redundant) != 1:
            errors.append('redundancy fixture lacks unique source support')
        if redundant in candidate:
            errors.append('redundant UI copy remains')
    numbers = lambda s: Counter(re.findall(r'\d+(?:\.\d+)?', s))
    links = lambda s: Counter(re.findall(r'https?://[^\s]+', s))
    # Only explicitly reviewed internal diagnostics may lose their numbers.
    # This fixture allowance is not a classifier for arbitrary public copy.
    public_source = case['before']
    for diagnostic in case.get('remove_internal_diagnostics', []):
        if not diagnostic or public_source.count(diagnostic) != 1:
            errors.append('diagnostic fixture lacks unique source support')
            continue
        public_source = public_source.replace(diagnostic, '', 1)
        if diagnostic in candidate:
            errors.append('internal diagnostics remain in public copy')
    if numbers(public_source) != numbers(candidate):
        errors.append('numbers changed')
    if links(case['before']) != links(candidate):
        errors.append('links changed')
    if case['unchanged'] and candidate != case['before']:
        errors.append('deliberate or already-good prose changed')
    return errors


def validate_skill(root):
    entry = root / 'SKILL.md'
    text = entry.read_text()
    if not text.startswith('---\nname: deslopify\ndescription:'):
        raise ValueError('skill metadata missing')
    visited = set()

    def check(path):
        path = path.resolve()
        if path in visited:
            return
        if not path.is_relative_to(root.resolve()):
            raise ValueError(f'reference escapes installed skill: {path}')
        # Existing model-folder links are navigation, not prose documents.
        if path.is_dir():
            return
        visited.add(path)
        body = path.read_text()
        if not body.strip():
            raise ValueError(f'empty maintained guidance: {path}')
        for target in re.findall(r'\]\(([^)]+)\)', body):
            if '://' not in target and not target.startswith('#'):
                check(path.parent / target.split('#')[0])

    check(entry)
    return visited


def main():
    visited = validate_skill(ROOT / 'deslopify')
    cases = json.loads((ROOT / 'tests/fixtures/rewrites.json').read_text())
    for case in cases:
        errors = preservation_errors(case, case['after'])
        if errors:
            raise ValueError(f"{case['id']}: {errors}")
    print(f'Validated {len(visited)} linked guidance files and {len(cases)} preservation fixtures.')


if __name__ == '__main__':
    main()
