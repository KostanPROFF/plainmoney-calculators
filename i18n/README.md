# Spanish translations

Spanish pages under `public/es/` are built from `es.json`, keyed by a hash of each English chunk.
After changing English text, `python3 build.py` lists what is missing and writes it to `source.html`.

To translate the missing chunks with DeepL's text API (which only takes plain text):
1. `python3 i18n/units.py extract` writes `units.json`, one sentence-sized string per entry,
   with inline tags as `[[n]]` markers.
2. Translate that list to ES-419 in the same order and save it as a JSON list.
3. `python3 i18n/units.py apply <that file>` writes `source.es.html`,
   then `python3 i18n/import.py i18n/source.es.html` merges it into `es.json`.
4. Run `python3 build.py` again.

Strings shown by the calculator scripts are listed in `js-strings.json` and use `{placeholders}`.
