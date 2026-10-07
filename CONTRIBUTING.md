# Contributing a do or don't

[Open the rule form](https://github.com/EricSpencer00/deslopify/issues/new?template=rule.yml). You don't need to clone the repo or write code. Submit one rule per issue.

1. Choose **Add a rule** or **Change a rule**. For a change, copy the existing ID from the [rule index](deslopify/references/rule-index.md).
2. Choose a category, direction, and scope.
3. State when the rule applies and what someone should do.
4. Include **one example that follows the rule** and **one counterexample that breaks it**.
5. Explain why it helps. Add public evidence if you have it; identify invented examples as illustrative.

The form also works for screenshots and layout descriptions. An example always shows the desired outcome, even when the rule is a don't.

## Category and scope

| Category | Use it for | Example suggestion |
| --- | --- | --- |
| Writing | Wording, structure, clarity, and preserving meaning | Replace unsupported praise with a concrete benefit. |
| Taste | A stated stylistic or aesthetic preference | Prefer a restrained palette for this brand. |
| Design | Layout, typography, visuals, and interactions | Keep the primary action visually distinguishable. |

Choose the category that best describes the change. Split a proposal if it contains independent rules.

| Scope | Company | Model |
| --- | --- | --- |
| All models | Leave blank | Leave blank |
| One company | Its folder name, e.g. `openai`, `anthropic`, or `google` | Leave blank |
| One model | Its company folder name | Exact model ID, e.g. `gpt-6.1-sol` |

Choose the narrowest scope your observation supports. Include the app, harness, quantization, personality, or other setting in the context when it matters. A problem seen in one configuration does not establish a company-wide behavior. [Browse company and model folder names](MODEL-CATALOG.md); new names are allowed as lowercase slugs. Model state is resolved from existing slots, or defaults to `new` for an unlisted model.

## A complete suggestion

| Form field | Answer |
| --- | --- |
| Change | Add a rule |
| Rule ID | `avoid-empty-superlatives` |
| Rule title | Replace empty praise with a concrete benefit |
| Category | Writing |
| Direction | Do |
| Applies to | All models |
| Company / Model | Leave blank |
| When does this apply? | Product descriptions. Preserve useful specifications and required disclosures. |
| The rule | Replace unsupported praise with a specific benefit the product actually offers. |
| Example that follows the rule | Export all invoices as a CSV file. |
| Counterexample that breaks the rule | Unlock an incredible, seamless invoice experience. |
| Why is this useful? | Readers can decide whether the product solves their problem. |
| Evidence or links | Illustrative example, not a recorded model output. |

For a don't, “Don't add unsupported praise” would use the same example and counterexample. Avoid turning preferences into blanket bans or treating punctuation alone as proof of AI authorship.

## Maintainer: turn an issue into a change

1. Review the rule, its scope, and the example pair. Ask for edits in the issue if needed.
2. Open [Actions → Rule proposal](https://github.com/EricSpencer00/deslopify/actions/workflows/rule-proposal.yml), choose **Run workflow** on the default branch, and enter the issue number.
3. The workflow validates the answers, adds or updates the record, regenerates reading files and indexes, runs the checks, and opens a PR on `rule-proposal/issue-<number>`.
4. Review the diff and merge the PR to apply the rule. It closes the issue. GitHub may show **Approve workflows to run** on a bot-created PR; approve those runs and wait for checks before merging. [GitHub's workflow-trigger behavior](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow).

To revise an open proposal, edit the issue and run the workflow again with the same issue number. It updates the same branch and PR without force-pushing. Keep its Rule ID stable. If the rule's category or scope changes, old generated guidance is cleared. Conflicts in generated files are rebuilt from merged records; conflicts in authored files or unrelated branch changes stop for manual review. After a PR is closed or merged, use a new change issue.

The issue-form validator also runs when a `[Rule]` issue is opened or edited. It checks structure and conditional company/model fields; it does not approve the advice. Proposals require a maintainer's manual Actions run. No model API key is needed.

If PR creation is blocked, check **Settings → Actions → General → Workflow permissions → Allow GitHub Actions to create and approve pull requests**. This setting permits creation; the workflow does not approve or merge PRs. The generated branch and a seven-day patch artifact remain available when generation succeeded. Enable the setting or create the PR from that branch, then rerun if needed. [GitHub's repository Actions settings](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository).

## Agent or direct PR contribution

Canonical records are in `deslopify/rules/<category>/<id>.json`. Stable IDs let agents update a rule instead of appending a duplicate. Each record contains:

```json
{
  "id": "avoid-empty-superlatives",
  "title": "Replace empty praise with a concrete benefit",
  "category": "writing",
  "direction": "do",
  "scope": "all",
  "company": null,
  "model": null,
  "model_state": null,
  "context": "Product descriptions. Preserve useful specifications and required disclosures.",
  "rule": "Replace unsupported praise with a specific benefit the product actually offers.",
  "example": "Export all invoices as a CSV file.",
  "counterexample": "Unlock an incredible, seamless invoice experience.",
  "rationale": "Readers can decide whether the product solves their problem.",
  "evidence": "Illustrative example, not a recorded model output."
}
```

All fields are required; `evidence` may be empty. Company scope uses a company string with null model/state. Model scope uses company and model strings plus `new`, `available`, or `deprecated` for `model_state`. IDs use lowercase letters, numbers, and hyphens (at most 64 characters). Titles are one line (at most 120 characters); other text fields are at most 8,000 characters. The validator rejects missing fields, duplicate IDs, invalid scopes, and identical example pairs.

Edit the record, then run these lightweight checks:

```sh
python3 deslopify/scripts/rules.py render
python3 scripts/sync_model_harnesses.py --check
python3 scripts/validate_content.py
python3 -m unittest discover -s tests -v
python3 scripts/update_readme_tree.py
python3 deslopify/scripts/rules.py render --check
```

Commit the record and generated files together. `fac/` contains dos; `ne-fac/` contains don'ts. Their all-model/company/model Markdown files and `deslopify/references/rule-index.*` are generated. Do not edit those reading files directly. CI checks PRs and regenerates them on the default branch.

For an offline preview of a form response, save the issue JSON and run:

```sh
python3 scripts/propose_rule.py --issue-json issue.json --dry-run
```

Without `--dry-run`, this adds or updates the canonical record and generated guidance locally. Use an issue JSON object with a `body` field, or a GitHub event object containing `issue`. The installed skill's `scripts/rules.py select` can return only the relevant category and scopes, as Markdown or JSON.
