#!/usr/bin/env python3
"""Keep the repository tree in README.md in sync with the files on disk."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
START = "<!-- README TREE START -->"
END = "<!-- README TREE END -->"
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
    if path == Path("README.md"):
        return "repository map"
    if path == Path("LICENSE"):
        return "license"
    if path == Path("deslopify/SKILL.md"):
        return "skill entrypoint"
    if path == Path("scripts/update_readme_tree.py"):
        return "README tree generator"
    if path == Path("scripts/sync_model_harnesses.py"):
        return "provider-native model slot sync"
    if path == Path(".github/workflows/readme-tree.yml"):
        return "CI update job"
    if path.name == "general.md":
        return "general guidance slot"
    if path.name == ".gitkeep":
        return "keeps an empty directory tracked"
    if path.suffix == ".md" and len(path.parts) >= 2 and path.parts[-2] in MODEL_STATES:
        return ""
    return "repository file"


def directory_note(path: Path) -> str:
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
        "- `general.md` is the company guidance slot.",
        "- Model `.md` files are empty slots for model-specific guidance.",
        "- `.gitkeep` files keep empty model-state directories in Git.",
        END,
    ]
    return "\n".join(lines)


def update_readme() -> None:
    original = README.read_text()
    section = generated_section(repository_files())
    if START in original and END in original:
        before = original.split(START, 1)[0].rstrip()
        after = original.split(END, 1)[1].lstrip()
        updated = f"{before}\n\n{section}"
        if after:
            updated += f"\n\n{after}"
    else:
        updated = f"{original.rstrip()}\n\n{section}\n"
    README.write_text(updated)


if __name__ == "__main__":
    update_readme()
