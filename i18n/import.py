#!/usr/bin/env python3
"""Merges a translated copy of i18n/todo-{lang}.html into i18n/{lang}.json.

Usage: python3 i18n/import.py ru i18n/done-ru.html
"""
import json, re, sys
from pathlib import Path

here = Path(__file__).parent
lang, src = sys.argv[1], sys.argv[2]
path = here / f"{lang}.json"
data = json.loads(path.read_text()) if path.exists() else {}
html = Path(src).read_text()
added = 0
for k, body in re.findall(r'<article id="k([0-9a-f]+)"[^>]*>\n?(.*?)\n?</article>', html, re.S):
    data[k] = body.strip()
    added += 1
path.write_text(json.dumps(data, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
print(f"Imported {added} translations; {lang}.json has {len(data)}")
