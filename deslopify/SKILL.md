---
name: deslopify
description: Apply reviewed writing, taste, and design dos and don'ts, with company and model-specific guidance, to reader-facing prose and interfaces.
---

## Pick the relevant rules

Read [fac — dos](fac/_template/general.md) and [ne fac — don'ts](ne-fac/_template/general.md).

Use **writing** rules for wording, structure, and meaning; **taste** rules for stated aesthetic preferences; **design** rules for layout, visuals, and interactions. Apply only the categories and contexts needed for the user's task. A taste preference is not a universal correctness test.

For a known company, also read its `general.md` under [fac models](fac/_template/models/) and [ne fac models](ne-fac/_template/models/). For a known model, read its matching file in `new/`, `available/`, or `deprecated/`. Empty files are unused slots, not guidance. Catalog states organize files; they do not establish current model availability.

Apply all-model rules plus matching company and model rules. Respect the task, audience, and any named harness or setting. Do not infer a company or model from a draft's style or extend a model observation to every model.

Each rule has an ID, scope, context, and illustrative example pair. **The example follows the rule; the counterexample breaks it**, including for don'ts. Preserve the author's meaning, useful facts, qualifications, and voice. Keep useful UI labels, accessible names, instructions, errors, product facts, and required disclosures.

## Find or maintain a rule

Use the [rule index](references/rule-index.md) to locate an ID. For a compact selection, run the installed helper:

```sh
python3 <skill-directory>/scripts/rules.py select --category writing --company openai --model gpt-6.1-sol
```

Omit company/model for all-model rules only. `--format json` returns structured records. The [machine index](references/rule-index.json) includes source and reading-file paths; the canonical records live in `rules/<category>/<id>.json`. Edit records, then run `scripts/rules.py render`; generated reading files will be rebuilt. Repository maintainers can also use the rule issue form and GitHub Actions to propose changes.

For public-facing copy, see the before/after [website-copy examples](examples/website-copy.md).
