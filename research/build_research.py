from __future__ import annotations

import csv
import hashlib
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "model-dos-and-donts"
FAC = ROOT / "deslopify" / "fac" / "_template" / "models"
NE_FAC = ROOT / "deslopify" / "ne-fac" / "_template" / "models"
LOCAL_SKILL = Path("/Users/eric/.agents/skills/deslopify/SKILL.md")

# These are legacy/deprecated placements for the proposal scaffold. They are
# intentionally conservative: a model stays active when the provider's current
# status was not clear from the reviewed catalog.
DEPRECATED = {
    "ai21": {"jamba-1.6"},
    "alibaba": {"qwen2.5", "qwen2.5-coder", "qwq-32b"},
    "allenai": {"olmo-2"},
    "amazon": {"nova-premier", "nova-pro", "nova-lite", "nova-micro"},
    "anthropic": {
        "claude-opus-4", "claude-opus-4.1", "claude-opus-4.5", "claude-opus-4.6",
        "claude-opus-4.7", "claude-opus-4.8", "claude-opus-5", "claude-sonnet-3",
        "claude-sonnet-3.5", "claude-sonnet-3.7", "claude-sonnet-4",
        "claude-sonnet-4.5", "claude-sonnet-4.6", "claude-sonnet-5",
        "claude-haiku-3", "claude-haiku-3.5", "claude-haiku-4.5", "claude-fable-5",
    },
    "bytedance": {"seed-2.0-pro", "seed-2.0-lite", "seed-2.0-mini", "seed-2.0-code"},
    "cohere": {"command-r", "command-r-plus", "command-r7b"},
    "deepseek": {
        "deepseek-v3", "deepseek-v3.1", "deepseek-v3.1-terminus", "deepseek-v3.2",
        "deepseek-v3.2-speciale", "deepseek-r1", "deepseek-r1-0528", "deepseek-coder-v2",
    },
    "google": {
        "gemini-1.5-pro", "gemini-1.5-flash", "gemini-2.0-flash", "gemini-2.0-flash-lite",
    },
    "ibm": {"granite-4.0"},
    "meta": {"llama-3", "llama-3.1", "llama-3.2", "llama-3.2-vision", "llama-3.3"},
    "microsoft": set(),
    "minimax": {"minimax-m1", "minimax-m2", "minimax-m2.1", "minimax-m2.5"},
    "mistral": {
        "mistral-medium-3.1", "mistral-large-2.1", "mistral-small-3.2",
        "devstral-2", "devstral-small-2", "magistral-medium-1.2", "magistral-small-1.2",
        "mistral-small-creative",
    },
    "moonshot": {"kimi-k2", "kimi-k2.5", "kimi-k2.6"},
    "nvidia": set(),
    "openai": {
        "gpt-4-turbo", "gpt-4.5-preview", "gpt-3.5-turbo", "gpt-5.3-chat",
        "gpt-5.2-chat", "gpt-5.2-codex", "gpt-5.1-chat", "gpt-5.1-codex",
        "gpt-5.1-codex-max", "gpt-5.1-codex-mini", "gpt-5-codex",
    },
    "perplexity": {"sonar", "sonar-pro", "sonar-reasoning", "sonar-reasoning-pro", "sonar-deep-research"},
    "writer": {"palmyra-x4"},
    "xai": {"grok-3", "grok-3-mini", "grok-4", "grok-4.1-fast", "grok-4-fast", "grok-code-fast-1"},
    "z-ai": {"glm-4.5", "glm-4.5-air", "glm-4.6", "glm-4.7", "glm-5", "glm-5.1", "glm-5.2"},
}

GENERAL = [
    ("G01", "Lead with the subject", "Put the concrete subject, situation, or decision first.", "Do not open with generic importance, excitement, or significance claims."),
    ("G02", "Use supported specificity", "Use names, mechanisms, examples, and numbers supplied by the source.", "Do not invent details to make thin material sound finished."),
    ("G03", "Give each paragraph one job", "Let each paragraph establish a fact, explain a choice, show a consequence, or make a judgment.", "Do not restate one claim in several polished forms."),
    ("G04", "Keep interpretation near evidence", "Name a consequence only when the facts support it.", "Do not turn a list into a personality, mission, or generic promise."),
    ("G05", "Keep the author's voice", "Preserve supported preferences, idioms, pacing, humor, and first-person experience.", "Do not manufacture intimacy, anecdotes, feelings, or a founder story."),
    ("G06", "Use precise verbs", "Keep actors visible and choose the ordinary word that says exactly what happened.", "Do not replace an action with abstract nouns or inflated adjectives."),
    ("G07", "Keep useful limits", "Retain uncertainty, conditions, failed attempts, and necessary disclosures.", "Do not trade a true qualification for a smoother universal claim."),
    ("G08", "Stop when the thought is complete", "End on the last sentence that adds information, judgment, or a qualification.", "Do not append a recap, moral, or future-looking conclusion by reflex."),
    ("G09", "Judge surface patterns in context", "Keep a list, colon, dash, passive voice, or first person when it does useful work.", "Do not replace one set of AI mannerisms with another blacklist."),
    ("G10", "Verify claims about work", "Report what was inspected, changed, or verified and state limits plainly.", "Do not announce successful tests or completed work without evidence."),
    ("G11", "Respect the requested scope", "Use the existing structure and complete the requested artifact.", "Do not add files, abstractions, features, or redesigns without a concrete need."),
    ("G12", "Make interfaces answer the content", "Choose hierarchy, typography, and layout for the actual audience and material.", "Do not use a repeated hero/card/gradient template as a substitute for design judgment."),
]


def category(provider: str, model: str) -> tuple[str, str, str]:
    """Return proposed do, proposed dont, and evidence note."""
    if provider == "anthropic" and model in {"claude-opus-4.5", "claude-opus-4.6"}:
        return (
            "Make the smallest solution that solves the requested problem.",
            "Do not add speculative abstractions, helper layers, or generic frontend patterns.",
            "Anthropic explicitly describes overengineering and generic frontend defaults for Opus 4.5/4.6.",
        )
    if provider == "anthropic" and model in {"claude-opus-5", "claude-opus-5.5"}:
        return (
            "Set visible length, scope, and stopping criteria explicitly.",
            "Do not assume lower reasoning effort will automatically shorten the visible prose or justify extra work.",
            "Anthropic documents visible verbosity and effort/scope controls for Opus 5/5.5.",
        )
    if provider == "anthropic" and model in {"claude-fable-5", "claude-fable-5.1"}:
        return (
            "Use compact paragraphs, surgical edits, and evidence-backed progress claims.",
            "Do not pack prose densely, rewrite whole files for small edits, or report unverified progress.",
            "Anthropic documents density, file-edit, and progress-report behaviors for Fable 5/5.1.",
        )
    if provider == "anthropic" and model.startswith("claude-sonnet"):
        return (
            "Give a positive style example and a concrete stopping point; match effort to task difficulty.",
            "Do not rely on a large negative blacklist, stop midway, or add work outside the requested scope.",
            "Anthropic documents effort, scope, and positive-example controls for Sonnet 5/5.5.",
        )
    if provider == "openai" and model == "gpt-6-astra":
        return (
            "Specify the response shape and keep verification proportional to the change.",
            "Do not let detailed formatting, recurring phrases, or broad verification become the deliverable.",
            "OpenAI documents Astra's detailed/formatted tendencies and possible over-verification.",
        )
    if provider == "openai" and model == "gpt-5.5":
        return (
            "State the target outcome, success criteria, constraints, and stopping point.",
            "Do not replace a clear outcome with an open-ended improvement ritual or unsupported polish.",
            "OpenAI recommends outcome-first prompts and deliberate stopping criteria for GPT-5.5.",
        )
    if provider == "google" and model.startswith("gemini-3"):
        return (
            "Use a short, direct prompt and specify only the output detail the reader needs.",
            "Do not carry elaborate legacy chain-of-thought prompting into a model that can over-analyze it.",
            "Google documents direct prompts and concise defaults for Gemini 3.",
        )
    if provider == "deepseek" and model.startswith("deepseek-r1"):
        return (
            "Use a bounded user-turn instruction, appropriate sampling, and a clean final answer.",
            "Do not use greedy decoding or publish repetitive reasoning as the finished copy.",
            "DeepSeek documents repetition risks and user-prompt/sampling recommendations for R1.",
        )
    if provider == "alibaba" and model.startswith("qwen3"):
        return (
            "Choose thinking or non-thinking mode deliberately and keep the final artifact separate from think markup.",
            "Do not use greedy decoding in thinking mode or expose <think> content as public prose.",
            "The Qwen3 model card documents mode separation and repetition risk from greedy decoding.",
        )
    if provider == "moonshot" and model.startswith("kimi-k2"):
        return (
            "Break a large software or editing task into an agentic sequence with clear tools and checkpoints.",
            "Do not force a whole project into one completion or leave tool purposes ambiguous.",
            "Moonshot reports token growth, incomplete calls, and one-shot degradation for Kimi K2.",
        )
    if provider == "google" and model.startswith("gemma"):
        return (
            "Use the role and control-token format supported by the exact Gemma checkpoint.",
            "Do not copy an older Gemma system-role assumption into a newer deployment.",
            "Google documents different instruction-role formats across Gemma generations.",
        )
    if provider == "mistral":
        return (
            "Keep the role, task, examples, and output requirements clear and mutually consistent.",
            "Do not stack contradictory standing instructions or add ceremony around a simple task.",
            "Mistral recommends concise, consistent prompt structure; exact model behavior remains untested.",
        )
    if "coder" in model or "code" in model or provider in {"bytedance", "nvidia"}:
        return (
            "Reuse the existing structure, make the smallest complete change, and verify the result.",
            "Do not turn a scoped task into a framework rewrite, speculative abstraction, or generic demo.",
            "Task-specific proposal based on the local skill; no exact prose tendency was established.",
        )
    if any(token in model for token in ("mini", "nano", "lite", "haiku")):
        return (
            "Keep the request narrow while preserving the facts and qualifications the reader needs.",
            "Do not achieve brevity by deleting the conditions that make the claim true.",
            "Task-specific proposal for efficient variants; exact model behavior remains untested.",
        )
    return (
        "Lead with supported facts, use concrete language, and stop when the requested artifact is complete.",
        "Do not add generic significance, decorative warmth, invented specificity, or a self-congratulatory close.",
        "Local deslopify baseline; exact model behavior remains untested.",
    )


def move_deprecated() -> list[tuple[str, str, str]]:
    moved: list[tuple[str, str, str]] = []
    for tree in (FAC, NE_FAC):
        for provider, models in DEPRECATED.items():
            destination = tree / provider / "deprecated"
            destination.mkdir(parents=True, exist_ok=True)
            for model in sorted(models):
                source = tree / provider / f"{model}.md"
                if not source.exists():
                    continue
                target = destination / source.name
                if target.exists():
                    raise RuntimeError(f"duplicate deprecated target: {target}")
                shutil.move(source, target)
                moved.append((tree.parent.parent.name, provider, model))
    return moved


def write_outputs() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    skill = LOCAL_SKILL.read_bytes()
    (OUT / "local-deslopify-skill.md").write_bytes(skill)

    lines = [
        "# Proposed deslopify research",
        "",
        "This is a review draft in a separate worktree. It does not change the main `deslopify/` checkout.",
        "",
        "Every model row below is an untested proposal. The local skill is the baseline; model-specific notes add a hypothesis or a provider-documented control. A model being in `deprecated/` means it is a legacy placement in this scaffold, not that every endpoint has shut down.",
        "",
        "- [Local deslopify skill](local-deslopify-skill.md)",
        "- [General proposals](general-proposals.md)",
        "- [Model index](model-index.csv)",
        "- [Deprecated model placements](deprecated-models.md)",
        "- [Sources and limits](sources.md)",
        "",
    ]
    (OUT / "README.md").write_text("\n".join(lines))

    general = [
        "# Proposed general dos and donts",
        "",
        "These proposals are derived from the local deslopify skill. They are intended to apply to every model when the task is relevant.",
        "",
        "| ID | Do | Dont |",
        "| --- | --- | --- |",
    ]
    general.extend(f"| {gid} | {do} | {dont} |" for gid, _, do, dont in GENERAL)
    general.extend(["", "The local skill remains the source of truth for the fuller rationale and editing passes.", ""])
    (OUT / "general-proposals.md").write_text("\n".join(general))

    sources = [
        "# Sources and limits",
        "",
        "Reviewed 2026-10-01 (America/Chicago). No model-generation evals were run. These links support prompting controls, reported tendencies, or model lifecycle context; they do not prove that a proposed rule improves this repository's outputs.",
        "",
        f"Local skill SHA-256: `{hashlib.sha256(skill).hexdigest()}`.",
        "",
        "Primary sources reviewed:",
        "",
        "- [OpenAI GPT-5.5 and GPT-6 guidance](https://developers.openai.com/api/docs/guides/latest-model)",
        "- [OpenAI prompt guidance for GPT-5.5](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.5)",
        "- [OpenAI all-model catalog](https://developers.openai.com/api/docs/models/all)",
        "- [Anthropic prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)",
        "- [Anthropic Opus 5.5 guidance](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)",
        "- [Anthropic Fable 5.1 guidance](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1)",
        "- [Google Gemini 3 guide](https://ai.google.dev/gemini-api/docs/gemini-3)",
        "- [Google Gemma role formatting](https://ai.google.dev/gemma/docs/core/prompt-structure)",
        "- [Google Gemma 4 formatting](https://ai.google.dev/gemma/docs/core/prompt-formatting-gemma4)",
        "- [Qwen3 model card](https://huggingface.co/Qwen/Qwen3-32B)",
        "- [DeepSeek-R1 README](https://github.com/deepseek-ai/DeepSeek-R1/blob/main/README.md)",
        "- [Kimi K2 report](https://www.kimi.com/en/blog/kimi-k2)",
        "- [Mistral prompting](https://docs.mistral.ai/inference/prompting)",
        "- [Z.AI thinking mode](https://docs.z.ai/guides/capabilities/thinking-mode)",
        "- [Cohere model catalog](https://docs.cohere.com/docs/models)",
        "- [Amazon Nova model guide](https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html)",
        "- [xAI model retirement notice](https://docs.x.ai/developers/migration/may-15-retirement)",
        "- [Perplexity Sonar migration](https://docs.perplexity.ai/docs/agent-api/migrate-from-sonar/overview.md)",
        "",
    ]
    (OUT / "sources.md").write_text("\n".join(sources))

    model_files = sorted(FAC.rglob("*.md"))
    model_files += sorted((FAC.parent / "models").rglob("deprecated/*.md"))
    # Deduplicate after the active/deprecated union above.
    model_files = sorted(set(model_files))
    rows = []
    for path in model_files:
        relative = path.relative_to(FAC)
        provider = relative.parts[0]
        model = path.stem
        status = "deprecated-or-legacy" if "deprecated" in relative.parts else "current-or-review"
        do, dont, evidence = category(provider, model)
        rows.append({
            "provider": provider,
            "model": model,
            "status": status,
            "scaffold_path": f"deslopify/fac/_template/models/{relative.as_posix()}",
            "ne_fac_scaffold_path": f"deslopify/ne-fac/_template/models/{relative.as_posix()}",
            "proposed_do": do,
            "proposed_dont": dont,
            "evidence_note": evidence,
            "baseline": "G01-G12",
            "tested": "no",
        })

    with (OUT / "model-index.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    deprecated = [
        "# Deprecated or legacy model placements",
        "",
        "These placeholders were moved in both `fac/_template/models/` and `ne-fac/_template/models/` under the provider's `deprecated/` folder. The classification is conservative and based on a named successor, an official retirement/deprecation list, or a provider migration path. It is a scaffold classification, not a claim that every provider endpoint is unavailable.",
        "",
        "| Provider | Models moved | Basis |",
        "| --- | --- | --- |",
    ]
    for provider in sorted(DEPRECATED):
        models = sorted(DEPRECATED[provider])
        if not models:
            continue
        deprecated.append(f"| `{provider}` | {', '.join(f'`{m}`' for m in models)} | Legacy family or provider migration path; review endpoint status before publishing. |")
    deprecated += ["", f"Moved placeholder count per tree: {sum(len(models) for models in DEPRECATED.values())}.", ""]
    (OUT / "deprecated-models.md").write_text("\n".join(deprecated))


if __name__ == "__main__":
    moved = move_deprecated()
    write_outputs()
    print(f"moved={len(moved)}")
