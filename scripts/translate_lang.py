#!/usr/bin/env python3
"""Translates a language of the PlainMoney Calculators site.

The site translates itself by hash: build.py writes `i18n/todo-{lang}.html`,
a file that holds every English chunk it still needs, and the translation goes
back into `i18n/{lang}.json` under the same hash.

The chunk is an HTML fragment, so it is cut into pieces first: `i18n/units.py`
splits it into sentence-sized units and hides the inline tags behind [[n]]
markers, which is what gets translated. This script does the middle step:
it translates the units, hands them back to `units.py apply`, and merges the
result into the language file with `i18n/import.py`.

The calculator scripts also show strings with a count in them — "12 months",
"30 years" — and a language picks a different word for each count. Those forms
are written to `i18n/{lang}-plurals.json` under the CLDR categories the
browser's `Intl.PluralRules` asks for.

Usage:
    python3 scripts/translate_lang.py zh
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "tools"))

from gemini_translate import Translator  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
I18N_DIR = ROOT / "i18n"

CONTEXT = (
    "User-visible text from a US personal-finance calculator website: "
    "mortgage, auto loan, take-home pay, 401(k), compound interest and debt "
    "payoff calculators, plus worked examples and FAQs. Write plain, direct "
    "financial prose. Keep every number, currency amount, percentage, state "
    "name and placeholder exactly as it is. The site shows the arithmetic "
    "behind a number and never tells the reader what to do."
)

# The CLDR plural categories each language uses, and the question that gets
# the right word form for each one.
CATEGORIES = {
    "zh": ["other"],
    "ko": ["other"],
    "vi": ["other"],
    "pt": ["one", "other"],
    "tl": ["one", "other"],
    "uk": ["one", "few", "many", "other"],
    "ar": ["zero", "one", "two", "few", "many", "other"],
}

CATEGORY_QUESTION = {
    "zero": "the count is 0",
    "one": "the count is 1",
    "two": "the count is 2",
    "few": "the count ends in 3 to 10",
    "many": "the count ends in 11 to 99",
    "other": "every other count, such as a fractional count or a large round number",
}

# The strings the calculator scripts show that carry a count.
PLURAL_STRINGS = [
    "{n} yr",
    "{n} mo",
    "{n} months",
    "Payment to finish in {n} months",
    "PMI applies because your down payment is under 20%. It drops off after about {years} years, when your loan reaches 80% of the home price.",
]

# What each plural string counts.
PLURAL_NOUN = {
    "{n} yr": "year",
    "{n} mo": "month",
    "{n} months": "month",
    "Payment to finish in {n} months": "month",
    "PMI applies because your down payment is under 20%. It drops off after about {years} years, when your loan reaches 80% of the home price.": "year",
}


def purge_unchanged(translator: Translator, units: list[str], lang: str, context: str) -> None:
    """Drops the cached translations that came back wrong.

    Four kinds are dropped: a unit the model handed back in English, a unit
    the model mixed another language into, a unit that came back empty, and a
    unit the model wrapped in quotation marks. All are cached like any other
    result, so without this they would never be tried again.
    """
    from gemini_translate import bad_cached, looks_like_prose

    removed = 0
    for unit in units:
        if not looks_like_prose(unit):
            continue
        path = translator._cache_path(lang, unit, context)
        if not path.exists():
            continue
        cached = path.read_text(encoding="utf-8")
        if bad_cached(unit, cached, lang):
            path.unlink()
            removed += 1
    if removed:
        print(f"  dropped {removed} wrong units from the cache")


def run(command: list[str]) -> str:
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    if result.returncode != 0:
        raise SystemExit(f"{' '.join(command)}\n{result.stderr.strip()}")
    return result.stdout.strip()


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: python3 scripts/translate_lang.py <lang> [...]", file=sys.stderr)
        return 1

    translator = Translator(batch_size=15, backend=os.environ.get("TRANSLATE_BACKEND", "minimax"))
    languages = sys.argv[1:]

    for lang in languages:
        print(f"=== {lang} ===")

        # 1. The units to translate.
        run([sys.executable, "i18n/units.py", "extract", lang])
        units = json.loads((I18N_DIR / f"units-{lang}.json").read_text())
        print(f"  {len(units)} units")

        # 2. The translation of each unit, in the same order. A unit the
        # model handed back in English is dropped from the cache first, so it
        # is translated properly this time.
        purge_unchanged(translator, units, lang, CONTEXT)
        translated = translator.translate_list(units, lang, context=CONTEXT)
        translated_path = I18N_DIR / f"translated-{lang}.json"
        translated_path.write_text(json.dumps(translated, ensure_ascii=False, indent=1))

        # 3. Put the translation back into the HTML.
        print(" ", run([sys.executable, "i18n/units.py", "apply", lang, str(translated_path)]))

        # 4. Merge it into the language file.
        print(" ", run([sys.executable, "i18n/import.py", lang, f"i18n/done-{lang}.html"]))

        # 5. The plural forms.
        write_plurals(lang, translator)

    print("stats:", translator.stats)
    return 0


def write_plurals(lang: str, translator: Translator) -> None:
    """Writes the CLDR plural forms for the strings that carry a count."""
    categories = CATEGORIES[lang]
    forms: dict[str, dict[str, str]] = {}

    for template in PLURAL_STRINGS:
        noun = PLURAL_NOUN[template]
        question = (
            f"Give the word form of \"{noun}\" in {LANG_NAMES[lang]}, as it follows a "
            f"count, for each of these categories: "
            + "; ".join(f"\"{c}\" is {CATEGORY_QUESTION[c]}" for c in categories)
            + ". Reply with a JSON object and nothing else. Its keys are exactly "
            + ", ".join(f"\"{c}\"" for c in categories)
            + ". Its values are the full phrase including the {n} or {years} "
            "placeholder. Keep the placeholder exactly as it is."
        )
        parsed = ask_for_json(translator, question, lang)
        if not parsed:
            raise SystemExit(f"could not read the plural forms for {lang}")
        forms[template] = {c: parsed.get(c, parsed.get("other", "")) for c in categories}

    path = I18N_DIR / f"{lang}-plurals.json"
    path.write_text(json.dumps(forms, ensure_ascii=False, indent=1) + "\n")
    print(f"  wrote {path.name}: {len(forms)} plural strings")


def ask_for_json(translator: Translator, question: str, lang: str) -> dict:
    """Asks for a JSON object, and asks again when the answer is not one.

    The model sometimes answers a request for JSON with prose. The second
    attempt says so plainly, and the answer is then read out of the prose if
    the JSON still does not arrive.
    """
    raw = translator.ask(question, context=CONTEXT)
    parsed = parse_json_object(raw)
    if parsed:
        return parsed

    stricter = question + " Your last answer was not JSON. Output only the JSON object, starting with { and ending with }."
    raw = translator.ask(stricter, context=CONTEXT)
    return parse_json_object(raw)


LANG_NAMES = {
    "zh": "Simplified Chinese",
    "ko": "Korean",
    "vi": "Vietnamese",
    "pt": "Brazilian Portuguese",
    "ar": "Modern Standard Arabic",
    "tl": "Tagalog",
    "uk": "Ukrainian",
}


def parse_json_object(raw: str) -> dict:
    text = raw.strip()
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.lstrip().lower().startswith("json"):
            text = text.lstrip()[4:]
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1:
        return {}
    try:
        data = json.loads(text[start : end + 1])
    except json.JSONDecodeError:
        return {}
    return data if isinstance(data, dict) else {}


if __name__ == "__main__":
    sys.exit(main())
