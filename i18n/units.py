#!/usr/bin/env python3
"""Splits i18n/source.html into translatable text units and puts translations back.

  python3 i18n/units.py extract            -> i18n/units.json  (list of English strings)
  python3 i18n/units.py apply units.es.json -> i18n/source.es.html (same order as units.json)

Inline tags inside a unit become [[n]]...[[/n]] markers so the translator sees whole sentences.
"""
import html, json, re, sys
from html.parser import HTMLParser
from pathlib import Path

HERE = Path(__file__).parent
INLINE = {"strong", "b", "em", "i", "a", "code", "sup", "sub"}


class Tok(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.toks = []

    def handle_starttag(self, tag, attrs):
        self.toks.append(("start", tag, self.get_starttag_text()))

    def handle_startendtag(self, tag, attrs):
        self.toks.append(("void", tag, self.get_starttag_text()))

    def handle_endtag(self, tag):
        self.toks.append(("end", tag, f"</{tag}>"))

    def handle_data(self, d):
        self.toks.append(("text", None, d))

    def handle_entityref(self, name):
        self.toks.append(("text", None, f"&{name};"))

    def handle_charref(self, name):
        self.toks.append(("text", None, f"&#{name};"))

    def handle_decl(self, d):
        self.toks.append(("raw", None, f"<!{d}>"))


def runs(src):
    """Yields ('raw', html) and ('unit', html_run) pieces covering src in order."""
    p = Tok(); p.feed(src); p.close()
    run = []
    def flush():
        # Inline tags whose partner falls outside this run (e.g. an <a> wrapping block content) stay raw.
        matched, stack = set(), []
        for i, (kind, tag, _) in enumerate(run):
            if kind == "start":
                stack.append(i)
            elif kind == "end":
                if stack and run[stack[-1]][1] == tag:
                    matched.update((stack.pop(), i))
        cur = []
        for i, t in enumerate(run):
            if t[0] != "text" and i not in matched:
                if cur:
                    yield ("unit", "".join(x[2] for x in cur)); cur = []
                yield ("raw", t[2])
            else:
                cur.append(t)
        if cur:
            yield ("unit", "".join(x[2] for x in cur))
        run.clear()
    for kind, tag, raw in p.toks:
        if kind == "text" or (kind in ("start", "end") and tag in INLINE):
            run.append((kind, tag, raw))
        else:
            yield from flush()
            yield ("raw", raw)
    yield from flush()


def has_words(s):
    return bool(re.search(r"[A-Za-z]{2,}", re.sub(r"<[^>]+>", "", s)))


def to_marked(unit_html):
    """Inline tags -> [[n]] markers; entities decoded. Returns (text, tags, lead, trail)."""
    lead = re.match(r"\s*", unit_html).group(0)
    trail = re.search(r"\s*$", unit_html).group(0)
    core = unit_html[len(lead):len(unit_html) - len(trail)] if trail else unit_html[len(lead):]
    tags, stack, out = [], [], []
    for m in re.finditer(r"<(/?)(\w+)[^>]*>|[^<]+", core):
        if m.group(2):
            if m.group(1):
                n = stack.pop(); out.append(f"[[/{n}]]")
            else:
                tags.append(m.group(0)); n = len(tags); stack.append(n); out.append(f"[[{n}]]")
        else:
            out.append(html.unescape(m.group(0)))
    return "".join(out), tags, lead, trail


def from_marked(text, tags, lead, trail):
    def esc(s):
        return html.escape(s, quote=False)
    parts = re.split(r"(\[\[/?\d+\]\])", text)
    out = []
    for part in parts:
        m = re.fullmatch(r"\[\[(/?)(\d+)\]\]", part)
        if m:
            tag = tags[int(m.group(2)) - 1]
            name = re.match(r"<(\w+)", tag).group(1)
            out.append(f"</{name}>" if m.group(1) else tag)
        else:
            out.append(esc(part))
    return lead + "".join(out) + trail


def main():
    src = (HERE / "source.html").read_text()
    pieces = list(runs(src))
    if sys.argv[1] == "extract":
        units = list(dict.fromkeys(to_marked(h)[0] for k, h in pieces if k == "unit" and has_words(h)))
        (HERE / "units.json").write_text(json.dumps(units, ensure_ascii=False, indent=1))
        print(len(units), "units,", sum(len(u) for u in units), "chars")
    else:
        en = json.loads((HERE / "units.json").read_text())
        es = dict(zip(en, json.loads(Path(sys.argv[2]).read_text())))
        out, bad = [], 0
        for k, h in pieces:
            if k == "unit" and has_words(h):
                text, tags, lead, trail = to_marked(h)
                tr = es[text]
                if sorted(re.findall(r"\[\[/?\d+\]\]", tr)) != sorted(re.findall(r"\[\[/?\d+\]\]", text)):
                    bad += 1
                    print("marker mismatch:", text[:60], "->", tr[:60])
                    tr = re.sub(r"\[\[/?\d+\]\]", "", tr)
                    tags = []
                out.append(from_marked(tr, tags, lead, trail) if tags else lead + html.escape(tr, quote=False) + trail)
            else:
                out.append(h)
        (HERE / "source.es.html").write_text("".join(out))
        print("applied;", bad, "marker mismatches")


main()
