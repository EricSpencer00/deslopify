<!-- Generated from rules/*.json. Edit the rule record, then regenerate. -->

## Do not use polish as proof of authorship (`dont-diagnose-authorship-by-polish`)

**Writing · Don’t · All models**

**When:** Any writing

Do not treat punctuation or polish as proof that writing is AI-generated. AI-generated language usually uses specific words or phrases.

**Example — follows the rule:**

Assess what a sentence says and whether its wording fits the context.

**Counterexample — breaks the rule:**

Declare a passage AI-generated solely because it uses an em dash.

**Why:** Punctuation and polish alone do not establish authorship.

**Evidence / source:** Migrated from existing repository guidance: `deslopify/ne-fac/_template/general.md`. Examples are illustrative.

## Do not manufacture human errors (`dont-fake-human-errors`)

**Writing · Don’t · All models**

**When:** Paper writing

Do not add typos, tangents or invented details to imitate a human.

**Example — follows the rule:**

Preserve the supported result and the writer’s actual qualification.

**Counterexample — breaks the rule:**

Add a deliberate typo and an invented personal story to sound human.

**Why:** Fabricated mistakes and details damage meaning and accuracy.

**Evidence / source:** Migrated from existing repository guidance: `deslopify/ne-fac/_template/general.md`. Examples are illustrative.

## Avoid automatic aphorism endings (`dont-repeat-aphorisms`)

**Writing · Don’t · All models**

**When:** Any writing

Do not end every paragraph by restating its point as an aphorism.

**Example — follows the rule:**

End the paragraph after the result and its needed limitation.

**Counterexample — breaks the rule:**

Append “Ultimately, progress is the art of possibility” after every paragraph.

**Why:** A repeated closing flourish adds little information.

**Evidence / source:** Migrated from existing repository guidance: `deslopify/ne-fac/_template/general.md`. Examples are illustrative.

## Omit unneeded version history (`omit-unneeded-version-history`)

**Writing · Don’t · All models**

**When:** Public-facing frontend copy

Omit history about old versions, retired pages, migrations, or redesigns when users can use the current experience without it, especially in prominent notices. Prefer the current action or a transparent redirect. Keep migration notices needed for user action, data loss, compatibility, or service impact.

**Example — follows the rule:**

Current navigation works, so omit the old-pages notice. Keep “Export your data by June 30 to avoid losing access” when action is required.

**Counterexample — breaks the rule:**

The older pages of this site now live on the home page. Start there.

**Why:** Keep notices when they communicate an actual consequence or required action.

**Evidence / source:** Migrated from existing SKILL.md guidance. Examples are illustrative; see deslopify/examples/website-copy.md.

## Keep internal accounting out of storefronts (`public-copy-without-diagnostics`)

**Writing · Don’t · All models**

**When:** Public-facing frontend copy

Remove the provider/catalog count and render accounting from the storefront, or move them to internal diagnostics. If a design selector works, keep its label in ordinary language, for example `Choose a design`. Omit an unusable control; do not imply it works.

**Example — follows the rule:**

Choose a design / Mountain print

**Counterexample — breaks the rule:**

Swap design / Mountain print / Provider catalog: 120 items · 240 / 240 rendered

**Why:** A shopper needs the working choice and product information.

**Evidence / source:** Migrated from existing SKILL.md guidance. Examples are illustrative; see deslopify/examples/website-copy.md.

## Let layout and content communicate (`remove-redundant-ui-copy`)

**Design · Don’t · All models**

**When:** Public-facing frontend copy

Let photos, content, layout, and working interactions carry their meaning. Do not add titles, labels, or marketing copy merely to fill space or explain what they already communicate. Remove decorative headings and redundant UI narration.

**Example — follows the rule:**

Mountain print — 12 × 18 in matte poster. / Choose a size before adding to cart. / Add to cart

**Counterexample — breaks the rule:**

Explore Our Stunning Collection / Artwork Preview / Mountain print — 12 × 18 in matte poster. / Choose a size before adding to cart. / Add to cart

**Why:** Redundant labels compete with the useful content and controls.

**Evidence / source:** Migrated from existing SKILL.md guidance. Examples are illustrative; see deslopify/examples/website-copy.md.
