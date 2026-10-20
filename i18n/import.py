#!/usr/bin/env python3
"""Merges a translated copy of i18n/source.html into i18n/es.json.

Usage: python3 i18n/import.py path/to/source.es.html
"""
import json, re, sys
from pathlib import Path

here = Path(__file__).parent
es_path = here / "es.json"
es = json.loads(es_path.read_text()) if es_path.exists() else {}
html = Path(sys.argv[1]).read_text()
added = 0
for k, body in re.findall(r'<article id="k([0-9a-f]+)"[^>]*>\n?(.*?)\n?</article>', html, re.S):
    es[k] = body.strip()
    added += 1
es_path.write_text(json.dumps(es, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
print(f"Imported {added} translations; es.json has {len(es)}")
