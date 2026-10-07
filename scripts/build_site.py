#!/usr/bin/env python3
"""Build the static website from the skill's own files (stdlib only).

The rule cards come from deslopify/rules/*.json and the before/after panels
from deslopify/examples/website-copy.md, so the site changes when the skill
does. Output goes to _site/ (or --out).
"""
from __future__ import annotations

import argparse
import difflib
import html
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
SKILL = ROOT / "deslopify"
REPO = "https://github.com/EricSpencer00/deslopify"
sys.path.insert(0, str(SKILL / "scripts"))
import rules as rulebook  # noqa: E402

STATIC = ("style.css", "app.js", "favicon.svg", "og.png")
COMPANIES = {
    "ai21": "AI21", "alibaba": "Alibaba", "allenai": "Ai2", "amazon": "Amazon",
    "anthropic": "Anthropic", "bytedance": "ByteDance", "cohere": "Cohere",
    "deepseek": "DeepSeek", "google": "Google", "ibm": "IBM", "meta": "Meta",
    "microsoft": "Microsoft", "minimax": "MiniMax", "mistral": "Mistral",
    "moonshot": "Moonshot", "nvidia": "NVIDIA", "openai": "OpenAI",
    "perplexity": "Perplexity", "writer": "Writer", "xai": "xAI", "z-ai": "Z.ai",
}


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def inline(text: str) -> str:
    """Escape text, then apply the small Markdown subset the records use."""
    out = esc(text)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    return re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', out)


def paragraphs(text: str) -> str:
    return "".join(f"<p>{inline(p.strip())}</p>" for p in re.split(r"\n\s*\n", text) if p.strip())


def words(text: str) -> list[str]:
    return re.findall(r"\s+|[^\s]+", text)


def show(tokens: list[str]) -> str:
    """Escape tokens. UI copy in the examples uses ' / ' between elements; draw it quietly."""
    return "".join('<span class="sep">/</span>' if t == "/" else esc(t) for t in tokens)


def diff(before: str, after: str) -> str:
    """Word-level redline of before -> after."""
    a, b = words(before), words(after)
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == "equal":
            out.append(show(a[i1:i2]))
            continue
        for tag, tokens in (("del", a[i1:i2]), ("ins", b[j1:j2])):
            text = "".join(tokens)
            if text.strip():
                lead, trail = text[: len(text) - len(text.lstrip())], text[len(text.rstrip()):]
                out.append(f"{lead}<{tag}>{show(words(text.strip()))}</{tag}>{trail or ' '}")
    return re.sub(r"\s{2,}", " ", "".join(out)).strip()


def parse_examples(path: Path) -> list[dict]:
    sections = re.split(r"^#{1,2} ", path.read_text(encoding="utf-8"), flags=re.M)[1:]
    examples = []
    for section in sections:
        title, _, body = section.partition("\n")
        quoted = r"(?:\n\n> (?P<{0}q>.+)|\s*`(?P<{0}c>[^`]+)`)"
        before = re.search(r"^Before:" + quoted.format("b"), body, re.M)
        after = re.search(r"^After(?P<cond>[^:\n]*):" + quoted.format("a"), body, re.M)
        context, notes = [], []
        for para in re.split(r"\n\s*\n", body.strip()):
            para = para.strip()
            if not para or para.startswith(("Before:", "After", ">")):
                continue
            (context if para.endswith(":") and not notes else notes).append(para.rstrip(":"))
        before_text = before.group("bq") or before.group("bc")
        after_text = (after.group("aq") or after.group("ac")) if after else ""
        examples.append({
            "title": title.strip(), "context": context, "notes": notes,
            "condition": after.group("cond").strip(", ") if after else "",
            "before": before_text, "after": after_text,
        })
    return examples


def render_example(ex: dict, index: int) -> str:
    context = "".join(f'<p class="ex-context">{inline(c)}.</p>' for c in ex["context"])
    if ex["condition"]:
        context += f'<p class="ex-context">Assumes {inline(ex["condition"].removeprefix("when "))}.</p>'
    notes = "".join(f"<p>{inline(n)}</p>" for n in ex["notes"])
    redline = diff(ex["before"], ex["after"])
    after = show(words(ex["after"])) if ex["after"] else '<span class="omitted">(omitted)</span>'
    title = ex["title"].split(": ", 1)[-1]
    return f"""
      <figure class="example" id="example-{index}">
        <figcaption><span class="ex-num">{index:02d}</span> {inline(title[:1].upper() + title[1:])}</figcaption>
        {context}
        <blockquote class="redline">{redline}</blockquote>
        <details class="clean"><summary>Show the edited text only</summary><blockquote>{after}</blockquote></details>
        <div class="ex-notes">{notes}</div>
      </figure>"""


def company_name(slug: str | None) -> str:
    return COMPANIES.get(slug or "", (slug or "").replace("-", " ").title())


def render_rule(rule: dict) -> str:
    rid = rule["id"]
    direction = "Do" if rule["direction"] == "do" else "Don’t"
    scope = ""
    if rule["scope"] == "company":
        scope = f"All {company_name(rule['company'])} models"
    elif rule["scope"] == "model":
        scope = f'<code>{esc(rule["model"])}</code>'
    meta = " · ".join(filter(None, (rule["category"].title(), scope, inline(rule["context"]))))
    evidence = f'<p class="evidence">Source: {inline(rule["evidence"])}</p>' if "http" in rule["evidence"] else ""
    search = " ".join(rule[k] or "" for k in ("id", "title", "context", "rule", "example",
                                              "counterexample", "rationale", "company", "model"))
    return f"""
        <article class="rule" id="{esc(rid)}" data-category="{rule['category']}" data-direction="{rule['direction']}" data-company="{esc(rule['company'] or 'all')}" data-search="{esc(search.lower())}">
          <h4><span class="dir dir-{rule['direction']}">{direction}</span> <a href="#{esc(rid)}">{inline(rule['title'])}</a></h4>
          <p class="meta">{meta}</p>
          <div class="rule-text">{paragraphs(rule['rule'])}</div>
          <dl class="pair">
            <div class="follows"><dt>Follows the rule</dt><dd>{inline(rule['example'])}</dd></div>
            <div class="breaks"><dt>Breaks it</dt><dd>{inline(rule['counterexample'])}</dd></div>
          </dl>
          <p class="why">{inline(rule['rationale'])}</p>
          {evidence}
          <p class="rule-id"><code>{esc(rid)}</code> <a href="{REPO}/blob/main/deslopify/{rulebook.source_path(rule).as_posix()}">record</a></p>
        </article>"""


def render_rules(rules: list[dict]) -> tuple[str, str]:
    groups: dict[str, list[dict]] = {}
    for rule in rules:
        groups.setdefault(rule["company"] or "all", []).append(rule)
    companies = sorted(k for k in groups if k != "all")
    blocks, options = [], []
    for key in ["all"] + companies:
        items = groups[key]
        name = "Every model" if key == "all" else company_name(key)
        blocks.append(f"""
      <section class="rule-group" data-group="{esc(key)}" aria-labelledby="g-{esc(key)}">
        <h3 id="g-{esc(key)}">{esc(name)} <span class="count">{len(items)}</span></h3>
        {''.join(render_rule(r) for r in items)}
      </section>""")
        options.append(f'<option value="{esc(key)}">{esc(name)} ({len(items)})</option>')
    return "".join(blocks), "".join(options)


def build(out: Path) -> None:
    rules = rulebook.load_rules(SKILL)
    examples = parse_examples(SKILL / "examples" / "website-copy.md")
    rule_html, company_options = render_rules(rules)
    count = lambda **kw: sum(all(r[k] == v for k, v in kw.items()) for r in rules)
    values = {
        "EXAMPLES": "".join(render_example(ex, i) for i, ex in enumerate(examples, 1)),
        "RULES": rule_html,
        "COMPANY_OPTIONS": company_options,
        "RULE_COUNT": str(len(rules)),
        "ALL_COUNT": str(count(scope="all")),
        "SPECIFIC_COUNT": str(len(rules) - count(scope="all")),
        "REPO": REPO,
    }
    page = (SITE / "index.html").read_text(encoding="utf-8")
    for key, value in values.items():
        page = page.replace("{{" + key + "}}", value)
    if leftover := re.findall(r"\{\{[A-Z_]+\}\}", page):
        raise SystemExit(f"unfilled placeholders: {leftover}")
    out.mkdir(parents=True, exist_ok=True)
    for old in out.iterdir():  # empty it in place so a running preview server keeps its directory
        shutil.rmtree(old) if old.is_dir() else old.unlink()
    (out / "index.html").write_text(page, encoding="utf-8")
    for name in STATIC:
        if (SITE / name).exists():
            shutil.copy2(SITE / name, out / name)
    (out / ".nojekyll").write_text("")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=ROOT / "_site")
    build(parser.parse_args().out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
