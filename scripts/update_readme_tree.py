#!/usr/bin/env python3
"""Keep MODEL-CATALOG.md in sync with the repository files on disk."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "MODEL-CATALOG.md"
START = "<!-- CATALOG TREE START -->"
END = "<!-- CATALOG TREE END -->"
IGNORED = {".git", ".agents", "__pycache__"}
MODEL_STATES = {"new", "available", "deprecated"}
NEW_MODEL_NOTES = {
    "alibaba": "Qwen Code model slots",
    "bytedance": "Trae model slots",
    "google": "Gemini CLI/Jules model slots",
    "minimax": "MiniMax Code model slots",
    "mistral": "Mistral Vibe model slots",
    "moonshot": "Kimi Code model slots",
    "openai": "Codex model slots",
    "anthropic": "Claude Code model slots",
    "xai": "Grok Build model slots",
    "z-ai": "ZCode model slots",
}


def repository_files() -> list[Path]:
    files = []
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if path.is_file() and not any(part in IGNORED for part in relative.parts):
            files.append(relative)
    return sorted(files, key=lambda path: tuple(part.lower() for part in path.parts))


def file_note(path: Path) -> str:
    notes = {
        Path("AGENTS.md"): "agent maintenance guide",
        Path("CONTRIBUTING.md"): "rule form, example pair, and Actions workflow",
        Path("deslopify/scripts/rules.py"): "validate, generate, and select rules",
        Path("scripts/propose_rule.py"): "issue-form parser and add/change helper",
        Path("scripts/rule_pull_request.py"): "issue-to-PR Actions entrypoint",
        Path("deslopify/references/rule-index.md"): "browsable rule index",
        Path("deslopify/references/rule-index.json"): "machine-readable rule index",
        Path(".github/ISSUE_TEMPLATE/rule.yml"): "do/don't contribution form",
        Path(".github/ISSUE_TEMPLATE/bug.yml"): "tooling bug and question form",
        Path(".github/ISSUE_TEMPLATE/config.yml"): "issue chooser configuration",
        Path(".github/workflows/rule-proposal.yml"): "validate issues and propose add/change PRs",
    }
    if path in notes:
        return notes[path]
    if path.parts[:2] == ("deslopify", "rules") and path.suffix == ".json":
        return "canonical rule record"
    if path == Path("README.md"):
        return "purpose, installation, and usage"
    if path == Path("MODEL-CATALOG.md"):
        return "model catalog and repository map"
    if path == Path("LICENSE"):
        return "license"
    if path == Path("deslopify/SKILL.md"):
        return "skill entrypoint"
    if path == Path("scripts/update_readme_tree.py"):
        return "catalog generator"
    if path == Path("scripts/sync_model_harnesses.py"):
        return "provider-native model slot sync"
    if path == Path(".github/workflows/readme-tree.yml"):
        return "CI update job"
    if path.name == "general.md":
        return "all-model guidance" if path.parent.name == "_template" else "company guidance"
    if path.name == ".gitkeep":
        return "keeps an empty directory tracked"
    if path.suffix == ".md" and len(path.parts) >= 2 and path.parts[-2] in MODEL_STATES:
        return "model guidance" if (ROOT / path).stat().st_size else ""
    return "repository file"


def directory_note(path: Path) -> str:
    if path == Path("deslopify/rules"):
        return "canonical writing, taste, and design records"
    if path.name == "new":
        return NEW_MODEL_NOTES.get(path.parent.name, "provider-native model slots")
    if path.name == "available":
        return "provider/API model slots"
    if path.name == "deprecated":
        return "legacy model slots"
    if path.name == "models":
        return "company model slots"
    return ""


def tree_lines(files: list[Path]) -> list[str]:
    directories: set[Path] = {Path()}
    children: dict[Path, set[str]] = {}
    for path in files:
        parent = path.parent
        children.setdefault(parent, set()).add(path.name)
        for index in range(1, len(path.parts)):
            directory = Path(*path.parts[:index])
            directories.add(directory)
            children.setdefault(directory.parent, set()).add(directory.name)

    def render(directory: Path, prefix: str = "") -> list[str]:
        entries = []
        for name in children.get(directory, set()):
            child = directory / name
            entries.append((child, child in directories))
        entries.sort(key=lambda item: (not item[1], item[0].name.lower()))

        lines: list[str] = []
        for index, (child, is_directory) in enumerate(entries):
            last = index == len(entries) - 1
            branch = "└── " if last else "├── "
            if is_directory:
                note = directory_note(child)
                suffix = f" — {note}" if note else ""
                lines.append(f"{prefix}{branch}{child.name}/{suffix}")
                extension = "    " if last else "│   "
                lines.extend(render(child, prefix + extension))
            else:
                note = file_note(child)
                suffix = f" — {note}" if note else ""
                lines.append(f"{prefix}{branch}{child.name}{suffix}")
        return lines

    return [".", *render(Path())]


def generated_section(files: list[Path]) -> str:
    lines = [
        START,
        "## File tree",
        "",
        "```text",
        *tree_lines(files),
        "```",
        "",
        "### File notes",
        "",
        "- `_template/general.md` applies to all models; company `general.md` files apply to that company.",
        "- Populated model files name the model, any harness or setting, and the writing context. Empty files are unused slots.",
        "- `.gitkeep` files keep empty model-state directories in Git.",
        END,
    ]
    return "\n".join(lines)


def update_catalog() -> None:
    original = CATALOG.read_text()
    section = generated_section(repository_files())
    if START in original and END in original:
        before = original.split(START, 1)[0].rstrip()
        after = original.split(END, 1)[1].lstrip()
        updated = f"{before}\n\n{section}"
        if after:
            updated += f"\n\n{after}"
    else:
        updated = f"{original.rstrip()}\n\n{section}"
    CATALOG.write_text(updated.rstrip() + "\n")


if __name__ == "__main__":
    update_catalog()
