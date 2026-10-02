#!/usr/bin/env python3
"""Keep provider-native model slots present in both skill templates."""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODEL_ROOTS = (
    ROOT / "deslopify/fac/_template/models",
    ROOT / "deslopify/ne-fac/_template/models",
)

# These are the current defaults or default routes of provider-owned coding
# harnesses. The files are intentionally empty: they are authoring slots.
HARNESS_DEFAULTS = {
    "alibaba": ("qwen3.5-plus",),
    "bytedance": ("seed-code",),
    "google": ("gemini-auto", "gemini-3-flash", "gemini-3.1-pro"),
    "minimax": ("minimax-m3.1-flash-preview",),
    "mistral": ("mistral-medium-latest",),
    "moonshot": ("kimi-k3", "kimi-for-coding", "kimi-for-coding-highspeed"),
    "z-ai": ("glm-5.3", "glm-5.3-flash"),
}


def expected_paths() -> list[Path]:
    return [
        root / provider / "new" / f"{model}.md"
        for root in MODEL_ROOTS
        for provider, models in HARNESS_DEFAULTS.items()
        for model in models
    ]


def sync(check: bool) -> int:
    missing = [path for path in expected_paths() if not path.is_file()]
    if check:
        if missing:
            for path in missing:
                print(f"missing: {path.relative_to(ROOT)}")
            return 1
        return 0

    for path in missing:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch()
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail when a required provider-native model slot is missing",
    )
    args = parser.parse_args()
    return sync(args.check)


if __name__ == "__main__":
    raise SystemExit(main())
