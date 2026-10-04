---
name: deslopify
description: Apply reviewed dos and don'ts to remove filler and generic phrasing from writing, with provider and model-specific guidance.
---

Read [fac — dos](fac/_template/general.md) and [ne fac — don'ts](ne-fac/_template/general.md).

For a known provider, also read its `general.md` under [fac models](fac/_template/models/) and [ne fac models](ne-fac/_template/models/). Read the matching model file in `new/`, `available/` or `deprecated/` when the model is known. Empty files have no rules.

Apply each rule only to its stated writing context and any named harness or setting. Do not infer a provider or model from the draft's style.

## Public-facing frontend copy

Never add technical terms or implementation details to a public-facing frontend unless they help the visitor understand, choose, or use the product. Preserve useful customer-facing specs, compatibility, limits, accessibility text, and required disclosures.

Remove the provider/catalog count and render accounting from the storefront, or move them to internal diagnostics. If a design selector works, keep its label in ordinary language, for example `Choose a design`. Omit an unusable control; do not imply it works.

Let photos, content, layout, and working interactions carry their meaning. Do not add titles, labels, or marketing copy merely to fill space or explain what they already communicate. Remove decorative headings and redundant UI narration.

Keep copy that supplies needed context or navigation, accessible names and alt text, instructions, errors, product facts, and legal disclosures. A useful heading or label earns its place; minimalism is not a reason to remove it. See the before/after examples in [website copy](examples/website-copy.md).
