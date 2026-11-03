#!/usr/bin/env python3
"""Removes the quotation marks the model puts around a label.

A short label comes back from the model as "“Alabama”" rather than "Alabama":
the model quotes the word the way it would quote a term in a sentence. On the
page the quotes are noise, and a dropdown of fifty states each in quotes reads
as a mistake.

The English source is what decides. A block that holds quotation marks in
English — a question about "today's dollars", a quoted term — keeps them in
the translation, because there they belong to the text. A block without them
does not get them in the translation either.

Usage:
    python3 scripts/fix_translation_quotes.py zh ko vi pt ar tl uk
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

# The quotation marks a model reaches for. The straight double quote is not
# in the list: the HTML uses it for the attributes, and taking it away would
# take the attributes with it.
QUOTES = "“”„‟«»"

# The languages where the model quotes a label. A dropdown of fifty states
# each in quotation marks reads as a mistake, and the model puts them there
# every time it answers a short label.
QUOTED_LABELS = {"vi", "pt", "tl"}

ARTICLE = re.compile(r'<article id="k([a-f0-9]+)">(.*?)</article>', re.S)


def english_blocks(locale: str) -> dict[str, str]:
    """The English text of every block, keyed by its hash."""
    path = I18N / f"todo-{locale}.html"
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    return {key: body for key, body in ARTICLE.findall(text)}


def main() -> int:
    locales = sys.argv[1:] or ["zh", "ko", "vi", "pt", "ar", "tl", "uk"]

    for locale in locales:
        path = I18N / f"{locale}.json"
        if not path.exists():
            continue
        if locale not in QUOTED_LABELS:
            # In the other languages the quotation marks are the language's
            # own way of quoting a term, and they belong where they are.
            print(f"{locale}: quotation marks left alone")
            continue
        blocks = english_blocks(locale)
        data = json.loads(path.read_text(encoding="utf-8"))
        removed = 0
        for key, value in list(data.items()):
            if not isinstance(value, str) or not value:
                continue
            marks = sum(value.count(q) for q in QUOTES)
            if not marks:
                continue
            english = blocks.get(key, "")
            if any(q in english for q in QUOTES):
                # The English has quotation marks too, so they belong here.
                continue
            fixed = value
            for quote in QUOTES:
                fixed = fixed.replace(quote, "")
            if fixed != value:
                data[key] = fixed
                removed += marks
        if removed:
            path.write_text(
                json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
            )
        print(f"{locale}: {removed} quotation marks removed")

    return 0


if __name__ == "__main__":
    sys.exit(main())
