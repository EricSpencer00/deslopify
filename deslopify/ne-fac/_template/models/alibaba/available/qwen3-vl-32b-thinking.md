<!-- Generated from rules/*.json. Edit the rule record, then regenerate. -->

## Avoid repeated closing taglines (`alibaba-dont-repeat-taglines`)

**Writing · Don’t · Model: alibaba / qwen3-vl-32b-thinking (available)**

**When:** Conversation — Qwen3 VL Thinking 32B · Open WebUI / llama.cpp

Do not let a repeated closing tagline become the whole response template.

**Example — follows the rule:**

Answer the follow-up with the requested detail and end there.

**Counterexample — breaks the rule:**

End every reply with the same unrelated “Let’s make magic happen!” tagline.

**Why:** A closing template can crowd out the actual answer.

**Evidence / source:** Migrated from existing repository guidance: `deslopify/ne-fac/_template/models/alibaba/available/qwen3-vl-32b-thinking.md`. Examples are illustrative.
