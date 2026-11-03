#!/usr/bin/env python3
"""Fixes the two mechanical faults a machine translation leaves behind.

The first is the percentage. The English source writes "7 percent", and the
model keeps the word "percent" because the context tells it to keep every
number and unit as it is. In a language that writes a percentage with the
symbol, the word is not a unit but an untranslated English word.

The second is the missing space. A model that switches between two scripts
sometimes joins them: "有时" in Arabic, "заcompound" in Ukrainian. The words
are right and only the space is missing.

Usage:
    python3 scripts/fix_translation_spacing.py zh ko vi ar tl uk
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

# The languages that write a percentage with the symbol.
SYMBOL_PERCENT = {"zh", "ko", "vi", "ar", "tl", "uk"}

PERCENT = re.compile(r"(\d(?:[\d.,]*\d)?)\s+percent\b")

# A word of one script right after a word of another, with no space between.
SCRIPT_GAP = re.compile(
    r"(?<=[Ѐ-ӿ一-鿿぀-ヿ])"
    r"(?=[A-Za-z])"
    r"|"
    r"(?<=[A-Za-z])"
    r"(?=[Ѐ-ӿ一-鿿぀-ヿ])"
)

# Korean writes the particle right after the Latin word it belongs to: "PMI는",
# "P는". A space there breaks the grammar, so the rule leaves Korean alone.
NO_SCRIPT_GAP = {"ko"}


def fix(text: str, locale: str) -> tuple[str, int, int]:
    percent = 0
    spacing = 0
    if locale in SYMBOL_PERCENT:
        percent = len(PERCENT.findall(text))
        text = PERCENT.sub(r"\1%", text)
    if locale not in NO_SCRIPT_GAP:
        spacing = len(SCRIPT_GAP.findall(text))
        text = SCRIPT_GAP.sub(" ", text)
    return text, percent, spacing


def main() -> int:
    locales = sys.argv[1:] or ["zh", "ko", "vi", "pt", "ar", "tl", "uk"]

    for locale in locales:
        path = I18N / f"{locale}.json"
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        percent = 0
        spacing = 0
        changed = False
        for key, value in list(data.items()):
            if not isinstance(value, str):
                continue
            fixed, p, s = fix(value, locale)
            percent += p
            spacing += s
            if fixed != value:
                data[key] = fixed
                changed = True
        if changed:
            path.write_text(
                json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
            )
        print(f"{locale}: {percent} percentages, {spacing} missing spaces")

    return 0


if __name__ == "__main__":
    sys.exit(main())
