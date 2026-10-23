# Translations

Translated pages live under `public/es/` and `public/ru/` and are built from `es.json` and `ru.json`,
keyed by a hash of each English chunk. After changing English text, `python3 build.py` lists what is
missing and writes it to `todo-{lang}.html`.

To translate the missing chunks with DeepL's text API (which only takes plain text):
1. `python3 i18n/units.py extract ru` writes `units-ru.json`, one sentence-sized string per entry,
   with inline tags as `[[n]]` markers.
2. Translate that list (ES-419 for Spanish, RU for Russian) in the same order and save it as a JSON list.
   Short labels sometimes come back wrong; re-translate those with a fuller English phrase.
   Keep `{placeholders}` in English.
3. `python3 i18n/units.py apply ru <that file>` writes `done-ru.html`,
   then `python3 i18n/import.py ru i18n/done-ru.html` merges it into `ru.json`.
4. Run `python3 build.py` again. The todo file disappears once nothing is missing.

Strings shown by the calculator scripts are listed in `js-strings.json` and use `{placeholders}`.
Worked examples and FAQs come from `content.py`.
