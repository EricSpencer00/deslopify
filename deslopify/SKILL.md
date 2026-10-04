---
name: deslopify
description: Apply reviewed dos and don'ts to remove filler and generic phrasing from writing, with provider and model-specific guidance.
---

Read [fac — dos](fac/_template/general.md) and [ne fac — don'ts](ne-fac/_template/general.md).

For a known provider, also read its `general.md` under [fac models](fac/_template/models/) and [ne fac models](ne-fac/_template/models/). Read the matching model file in `new/`, `available/` or `deprecated/` when the model is known. Empty files have no rules.

Apply each rule only to its stated writing context and any named harness or setting. Do not infer a provider or model from the draft's style.

## Public-facing frontend copy

Never add technical terms or implementation details to a public-facing frontend unless they help the visitor understand, choose, or use the product. Preserve useful customer-facing specs, compatibility, limits, accessibility text, and required disclosures.

FamousMoji shop regression: `Swap album / Get That Yam Off Your Face / 2,554 Printify items · 53,634 / 53,634 rendered`.

Remove the provider/catalog count and render accounting from the storefront, or move them to internal diagnostics. If album/artwork selection works, keep it in ordinary language, for example `Choose an album / Get That Yam Off Your Face`. Omit an unusable control; do not imply it works.
