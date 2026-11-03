# Translations

The site is published in ten languages: en, ru, es, zh, ko, vi, pt, ar, tl, uk.
Translated pages live under `public/<lang>/` and are built from `i18n/<lang>.json`,
keyed by a hash of each English chunk. After changing English text, `python3 build.py` lists what is
missing and writes it to `todo-{lang}.html`.

## How a language is translated

The whole pipeline runs in one command:

    python3 scripts/translate_lang.py zh ko vi pt ar tl uk

It does the middle step of the old manual flow, using an LLM instead of DeepL:
1. `i18n/units.py extract <lang>` writes `units-<lang>.json`, one sentence-sized string per entry,
   with inline tags as `[[n]]` markers.
2. The strings are translated in batches, checked, and written to `translated-<lang>.json`.
   A unit that comes back in English, or in the wrong script, is translated again on its own.
3. `i18n/units.py apply <lang> translated-<lang>.json` writes `done-<lang>.html`,
   then `i18n/import.py <lang> i18n/done-<lang>.html` merges it into `<lang>.json`.
4. The CLDR plural forms are written to `<lang>-plurals.json`.
5. Run `python3 build.py` again. The todo file disappears once nothing is missing.

Results are cached under `../tools/.cache`, so a re-run only pays for what changed.

`I18N_FORCE_TODO=zh,pt python3 build.py` regenerates the todo files for the languages named,
which is how an English edit is pushed back into the translations.

## Manual fallback

If the model is unavailable, the old manual flow still works:
1. `python3 i18n/units.py extract ru` writes `units-ru.json`, one sentence-sized string per entry,
   with inline tags as `[[n]]` markers.
2. Translate that list in the same order and save it as a JSON list.
   Short labels sometimes come back wrong; re-translate those with a fuller English phrase.
   Keep `{placeholders}` in English.
3. `python3 i18n/units.py apply ru <that file>` writes `done-ru.html`,
   then `python3 i18n/import.py ru i18n/done-ru.html` merges it into `ru.json`.
4. Run `python3 build.py` again. The todo file disappears once nothing is missing.

Strings shown by the calculator scripts are listed in `js-strings.json` and use `{placeholders}`.
Worked examples and FAQs come from `content.py`.
