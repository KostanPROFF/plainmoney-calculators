#!/usr/bin/env python3
"""Generates the static HTML pages from the templates below.

Run `python3 build.py`; it writes the site into public/. Edit content here, not in the generated HTML.
"""
from pathlib import Path
import json
import re

from art import ART
from content import CONTENT

SITE_NAME = "Plain Money Calculators"
SITE_URL = "https://plainmoneycalc.com"
ADSENSE_CLIENT = "ca-pub-5321511632415174"
GA_ID = "G-NDSEJCQ08E"  # Google Analytics 4
GTM_ID = "GTM-K9KBMGKN"  # Google Tag Manager container
ROOT = Path(__file__).parent / "public"

NAV = [
    ("mortgage-calculator.html", "Mortgage"),
    ("auto-loan-calculator.html", "Auto Loan"),
    ("paycheck-calculator.html", "Paycheck"),
    ("401k-calculator.html", "401(k)"),
    ("compound-interest-calculator.html", "Compound Interest"),
    ("./#all", "All calculators"),
]


def ad(kind, label="Advertisement"):
    # Auto ads place units for now. Return an <ins class="adsbygoogle"> unit here once manual ad slots exist.
    return ""


def field(id, label, value, pre="", post="", hint="", full=False, step="any", type_="number"):
    cls = "input-wrap" + (" has-pre" if pre else "") + (" has-post" if post else "")
    pre_html = f'<span class="pre">{pre}</span>' if pre else ""
    post_html = f'<span class="post">{post}</span>' if post else ""
    hint_html = f'<span class="hint">{hint}</span>' if hint else ""
    return (
        f'<div class="field{" full" if full else ""}"><label for="{id}">{label}</label>'
        f'<div class="{cls}">{pre_html}<input id="{id}" type="{type_}" inputmode="decimal" step="{step}" value="{value}">{post_html}</div>{hint_html}</div>'
    )


def select(id, label, options, selected=None, full=False, hint=""):
    opts = "".join(
        f'<option value="{v}"{" selected" if v == selected else ""}>{t}</option>' for v, t in options
    )
    hint_html = f'<span class="hint">{hint}</span>' if hint else ""
    return f'<div class="field{" full" if full else ""}"><label for="{id}">{label}</label><select id="{id}">{opts}</select>{hint_html}</div>'


# Translated copies of every page live under /es/ and /ru/. Translations come from i18n/{lang}.json, keyed by
# a hash of the English text, so editing English copy marks that chunk as untranslated until the file is refreshed.
I18N_DIR = Path(__file__).parent / "i18n"
LANGS = {
    "en": {"prefix": "", "locale": "en_US", "name": "English"},
    "es": {"prefix": "es/", "locale": "es_US", "name": "Español"},
    "ru": {"prefix": "ru/", "locale": "ru_RU", "name": "Русский"},
}
UI = {
    "footer": "Estimates only, not financial, tax or medical advice.",
    "about": "About",
    "privacy": "Privacy Policy",
    "nav_label": "Calculators",
    "theme": "Switch between light and dark theme",
}
TR = {l: json.loads(f.read_text()) if (f := I18N_DIR / f"{l}.json").exists() else {} for l in LANGS if l != "en"}
SOURCE = {}  # key -> English text, everything that needs a translation
PAGES = []  # English page args, replayed for each language


def key(text):
    import hashlib
    return hashlib.sha1(text.encode()).hexdigest()[:12]


def tr(text, lang):
    """English text in `lang`; records it as needing translation. Returns None when missing."""
    if lang == "en":
        SOURCE[key(text)] = text
        return text
    return TR[lang].get(key(text))


def extras(filename, lang):
    """Worked examples and FAQ for a calculator page, plus FAQPage structured data. None if untranslated."""
    c = CONTENT.get(filename)
    if not c:
        return "", None
    parts = [tr(x, lang) for x in ("Worked examples", "Frequently asked questions", c["examples"].strip(),
                                   *(t for qa in c["faq"] for t in qa))]
    if any(x is None for x in parts):
        return None, None
    h_ex, h_faq, examples, *qa = parts
    faq = list(zip(qa[::2], qa[1::2]))
    items = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>\n" for q, a in faq)
    html_ = f'<section class="prose extras">\n<h2>{h_ex}</h2>\n{examples}\n<h2>{h_faq}</h2>\n<div class="faq">\n{items}</div>\n</section>'
    strip = lambda t: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t)).replace("&amp;", "&").strip()
    schema = {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": lang, "mainEntity": [
        {"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in faq]}
    return html_, schema


THEME_ICONS = (
    '<svg class="moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/></svg>'
    '<svg class="sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/>'
    '<path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
)


def page(filename, title, description, body, scripts=(), schema=None, lang="en"):
    if lang == "en":
        PAGES.append((filename, title, description, body, scripts, schema))
    parts = [tr(x, lang) for x in (title, description, body, *UI.values(), *(t for _, t in NAV))]
    if any(x is None for x in parts):
        return False
    title, description, body, footer, about, privacy, nav_label, theme_label, *nav_texts = parts
    extra, faq_schema = extras(filename, lang)
    if extra is None:
        return False
    body += "\n" + extra if extra else ""
    # Illustrations go in after translation so they never change the translated text.
    if filename in ART:
        body = re.sub(r'<h1>(.*?)</h1>\s*<p class="lede">(.*?)</p>',
                      lambda m: f'<header class="calc-hero"><div><h1>{m[1]}</h1><p class="lede">{m[2]}</p></div>{ART[filename]}</header>',
                      body, count=1, flags=re.S)
    body = re.sub(r'(<a class="calc-card" href="([^"]+)">)', lambda m: m[1] + ART.get(m[2], ""), body)
    up = "" if lang == "en" else "../"
    nav = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == filename else ""}>{text}</a>'
        for (href, _), text in zip(NAV, nav_texts)
    )
    switch = "".join(
        f'<a class="lang-switch" href="{up}{LANGS[l]["prefix"]}{"" if filename == "index.html" else filename}" hreflang="{l}" lang="{l}">{LANGS[l]["name"]}</a>'
        for l in LANGS if l != lang
    )
    adsense = (
        f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_CLIENT}" crossorigin="anonymous"></script>'
        f'\n<meta name="google-adsense-account" content="{ADSENSE_CLIENT}">'
        if ADSENSE_CLIENT else "<!-- AdSense script goes here once ADSENSE_CLIENT is set in build.py -->"
    )
    # GA4 and Tag Manager share one dataLayer, initialised at once so nothing is lost. Their scripts load on the
    # visitor's first scroll, tap or key press, or 4 seconds after the page loads, so they stay off the critical
    # path that PageSpeed measures. The AdSense script is left as is.
    tags = [u for u, on in ((f"https://www.googletagmanager.com/gtm.js?id={GTM_ID}", GTM_ID),
                            (f"https://www.googletagmanager.com/gtag/js?id={GA_ID}", GA_ID)) if on]
    analytics = (
        "<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());"
        + (f"gtag('config','{GA_ID}');" if GA_ID else "")
        + ("dataLayer.push({'gtm.start':Date.now(),event:'gtm.js'});" if GTM_ID else "")
        + f"(function(){{var done=0,ev=['scroll','pointerdown','keydown','touchstart'];function go(){{if(done)return;done=1;"
        + f"ev.forEach(function(e){{removeEventListener(e,go)}});{json.dumps(tags)}.forEach(function(u){{var s=document.createElement('script');s.async=1;s.src=u;document.head.appendChild(s)}})}}"
        + "ev.forEach(function(e){addEventListener(e,go,{passive:true,once:true})});addEventListener('load',function(){setTimeout(go,4000)})})();</script>"
    ) if tags else ""
    path = clean(filename)
    url = lambda l: f"{SITE_URL}/{LANGS[l]['prefix']}{path}"
    alternates = "".join(f'<link rel="alternate" hreflang="{l}" href="{url(l)}">' for l in LANGS)
    alternates += f'<link rel="alternate" hreflang="x-default" href="{url("en")}">'
    if schema:
        schema = {**schema, "name": title.split(":")[0].split("(")[0].strip() if lang != "en" else schema["name"],
                  "description": description, "url": url(lang), "inLanguage": lang}
    site_schema = {"@context": "https://schema.org", "@type": "WebSite", "name": SITE_NAME, "url": url(lang),
                   "inLanguage": lang, "description": description} if filename == "index.html" else None
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in (site_schema, schema, faq_schema) if s)
    js_files = ["common.js", *([f"i18n-{lang}.js"] if lang != "en" else []), *scripts]
    js = "".join(f'<script defer src="/assets/{s}?v={asset_version(s, lang)}"></script>' for s in js_files)
    html = f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<script>try{{var t=localStorage.getItem("theme");if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
{analytics}
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{url(lang)}">
{alternates}
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url(lang)}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:image" content="{SITE_URL}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{LANGS[lang]['locale']}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="/assets/fonts/PublicSans-5-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/Archivo-0-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#070b09" media="(prefers-color-scheme: dark)">
<meta name="theme-color" content="#f4f8f6" media="(prefers-color-scheme: light)">
<style>{CSS}</style>
{adsense}
{ld}
</head>
<body>
<header class="site-header"><div class="wrap">
<a class="logo" href="./">Plain<span>Money</span></a>
<nav class="site-nav" aria-label="{nav_label}">{nav}{switch}<button class="theme-toggle" type="button" aria-label="{theme_label}" title="{theme_label}">{THEME_ICONS}</button></nav>
</div></header>
<main class="wrap">
{body}
</main>
<footer class="site-footer"><div class="wrap">
<span>&copy; 2026 {SITE_NAME}. {footer}</span>
<nav><a href="about.html">{about}</a><a href="privacy.html">{privacy}</a></nav>
</div></footer>
{js}
</body>
</html>
"""
    out = ROOT / LANGS[lang]["prefix"] / filename
    out.parent.mkdir(parents=True, exist_ok=True)
    # Cloudflare serves foo.html at /foo (and redirects /foo.html there), so every link uses that form.
    html = re.sub(r'href="((?:\.\./)?(?:[a-z]{2}/)?)([a-z0-9-]+)\.html', lambda m: f'href="{m[1] or ""}{clean(m[2] + ".html")}' if m[2] != "index" else f'href="{m[1] or "./"}', html)
    out.write_text(html)
    return True


# Fonts are self-hosted and the stylesheet is inlined, so nothing blocks the first paint.
CSS = re.sub(r"\s*\n\s*", "", (ROOT / "assets" / "fonts.css").read_text() + (ROOT / "assets" / "style.css").read_text())


def asset_version(name, lang):
    """Short content hash for cache busting; /assets/* is cached for a year (see public/_headers)."""
    import hashlib
    if name.startswith("i18n-"):
        src = b"".join(f.read_bytes() for f in sorted(I18N_DIR.glob(f"{lang}*.json")) + [I18N_DIR / "js-strings.json"])
    else:
        src = (ROOT / "assets" / name).read_bytes()
    return hashlib.sha1(src).hexdigest()[:8]


def clean(filename):
    """Public path of a page: Cloudflare serves foo.html as /foo and index.html as the folder."""
    return "" if filename == "index.html" else filename.removesuffix(".html")


def calc_schema(name, description, filename, category="FinanceApplication"):
    return {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": name,
        "description": description,
        "url": f"{SITE_URL}/{clean(filename)}",
        "applicationCategory": category,
        "operatingSystem": "Any",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
    }


# ---------------------------------------------------------------- Home
GROUPS = [
    ("Home &amp; loans", [
        ("mortgage-calculator.html", "Mortgage Calculator", "Monthly payment with taxes, insurance, PMI and HOA, plus a full amortization schedule."),
        ("home-affordability-calculator.html", "Home Affordability Calculator", "How much house you can afford on your income, using the 28/36 rule lenders apply."),
        ("auto-loan-calculator.html", "Auto Loan Calculator", "Car payment after trade-in, down payment and sales tax, with total interest."),
        ("personal-loan-calculator.html", "Personal Loan Calculator", "Monthly payment, total interest and the true APR after origination fees."),
        ("credit-card-payoff-calculator.html", "Credit Card Payoff Calculator", "How long it takes to clear a balance, and the payment needed to be debt-free by a date."),
        ("debt-to-income-calculator.html", "Debt-to-Income Calculator", "The DTI ratio lenders check before approving a mortgage or loan."),
    ]),
    ("Income &amp; taxes", [
        ("paycheck-calculator.html", "Paycheck Calculator", "Take-home pay after 2026 federal income tax, Social Security, Medicare and state tax."),
        ("salary-to-hourly-calculator.html", "Salary to Hourly Calculator", "Convert any pay rate between hourly, daily, weekly, biweekly, monthly and yearly."),
    ]),
    ("Saving &amp; retirement", [
        ("401k-calculator.html", "401(k) Calculator", "Retirement balance with employer match, salary growth and 2026 contribution limits."),
        ("compound-interest-calculator.html", "Compound Interest Calculator", "How savings grow with monthly deposits and different compounding schedules."),
        ("savings-goal-calculator.html", "Savings Goal Calculator", "The monthly amount you need to save to reach a target by a deadline."),
    ]),
    ("Health &amp; fitness", [
        ("bmi-calculator.html", "BMI Calculator", "Body mass index from height and weight, with the healthy weight range for your height."),
        ("calorie-calculator.html", "Calorie Calculator", "Daily calories to maintain, lose or gain weight, based on your size, age and activity."),
        ("due-date-calculator.html", "Due Date Calculator", "Estimated due date, current week of pregnancy and trimester dates from your last period."),
    ]),
    ("Everyday math", [
        ("percentage-calculator.html", "Percentage Calculator", "Percent of a number, what percent one number is of another, and percent change."),
        ("tip-calculator.html", "Tip Calculator", "Tip and total for any bill, split between any number of people."),
        ("age-calculator.html", "Age Calculator", "Exact age in years, months and days, plus the days until your next birthday."),
        ("gpa-calculator.html", "GPA Calculator", "Semester and cumulative GPA on the 4.0 scale from your grades and credit hours."),
    ]),
]
CARDS = [c for _, cs in GROUPS for c in cs]
cards = "".join(
    f'<h2>{g}</h2><div class="calc-grid">'
    + "".join(f'<a class="calc-card" href="{h}"><strong>{t}</strong><span>{d}</span><em>Open calculator</em></a>' for h, t, d in cs)
    + "</div>"
    for g, cs in GROUPS
)
page(
    "index.html",
    "Free Online Calculators for Money, Health and Everyday Math",
    "Free, fast calculators for mortgages, loans, take-home pay, 401(k), BMI, calories, due dates, percentages, tips, age and GPA. No sign-up.",
    f"""
{ad("leaderboard")}
<p class="eyebrow">Updated for 2026 tax year</p>
<h1>Everyday math, done in seconds</h1>
<p class="lede">Free calculators for money, health and daily life: buying a home, paying off debt, understanding your paycheck, checking your BMI, planning meals, splitting a bill or working out a grade. Results update as you type, and nothing you enter leaves your browser.</p>
<div id="all">{cards}</div>
{ad("inline")}
<section class="prose">
<h2>Why use these calculators</h2>
<p>Each tool uses current official figures, such as IRS tax tables and CDC health ranges, and standard published formulas. Every assumption is shown and every result is broken down, so you can see how it was reached. They work on any phone or computer with no account and no tracking of your numbers.</p>
</section>
""",
)

# US states for the calculators that prefill state taxes (auto-detected from the visitor's IP).
STATES = [
    ("AL","Alabama"),("AK","Alaska"),("AZ","Arizona"),("AR","Arkansas"),("CA","California"),("CO","Colorado"),
    ("CT","Connecticut"),("DE","Delaware"),("DC","District of Columbia"),("FL","Florida"),("GA","Georgia"),
    ("HI","Hawaii"),("ID","Idaho"),("IL","Illinois"),("IN","Indiana"),("IA","Iowa"),("KS","Kansas"),
    ("KY","Kentucky"),("LA","Louisiana"),("ME","Maine"),("MD","Maryland"),("MA","Massachusetts"),
    ("MI","Michigan"),("MN","Minnesota"),("MS","Mississippi"),("MO","Missouri"),("MT","Montana"),
    ("NE","Nebraska"),("NV","Nevada"),("NH","New Hampshire"),("NJ","New Jersey"),("NM","New Mexico"),
    ("NY","New York"),("NC","North Carolina"),("ND","North Dakota"),("OH","Ohio"),("OK","Oklahoma"),
    ("OR","Oregon"),("PA","Pennsylvania"),("RI","Rhode Island"),("SC","South Carolina"),("SD","South Dakota"),
    ("TN","Tennessee"),("TX","Texas"),("UT","Utah"),("VT","Vermont"),("VA","Virginia"),("WA","Washington"),
    ("WV","West Virginia"),("WI","Wisconsin"),("WY","Wyoming"),
]

# ---------------------------------------------------------------- Mortgage
desc = "Estimate your monthly mortgage payment including property tax, homeowners insurance, PMI and HOA dues, with a year-by-year amortization schedule."
page(
    "mortgage-calculator.html",
    "Mortgage Calculator with Taxes, Insurance and PMI (2026)",
    desc,
    f"""
{ad("leaderboard")}
<h1>Mortgage Calculator</h1>
<p class="lede">See your full monthly housing payment, not just principal and interest.</p>
<div class="calc">
<form class="panel" id="form" novalidate><div class="fields">
{field("price", "Home price", "425000", pre="$")}
{field("downPct", "Down payment", "20", post="%")}
{field("rate", "Interest rate", "6.5", post="%", hint="30-yr fixed average")}
{select("term", "Loan term", [("30", "30 years"), ("20", "20 years"), ("15", "15 years"), ("10", "10 years")], "30")}
{select("state", "State", STATES, "TX")}
{field("taxRate", "Property tax", "1.58", post="%/yr", hint="Average for your state; edit if you know yours")}
{field("insurance", "Home insurance", "1800", pre="$", hint="per year")}
{field("hoa", "HOA dues", "0", pre="$", hint="per month")}
{field("pmiRate", "PMI rate", "0.5", post="%/yr", hint="Applies under 20% down")}
</div></form>
<section class="panel" aria-live="polite">
<div class="headline"><span class="eyebrow">Estimated monthly payment</span><span class="big" id="total">-</span></div>
<div class="bar" id="bar"></div>
<dl class="kv">
<dt><span class="swatch" style="background:var(--accent)"></span>Principal &amp; interest</dt><dd id="pi">-</dd>
<dt><span class="swatch" style="background:#5b8def"></span>Property tax</dt><dd id="tax">-</dd>
<dt><span class="swatch" style="background:#e0a64a"></span>Home insurance</dt><dd id="ins">-</dd>
<dt><span class="swatch" style="background:#c46b9a"></span>PMI</dt><dd id="pmi">-</dd>
<dt><span class="swatch" style="background:#8a8f8c"></span>HOA</dt><dd id="hoaOut">-</dd>
</dl>
<dl class="kv">
<dt>Loan amount</dt><dd id="loan">-</dd>
<dt>Total interest paid</dt><dd id="interest">-</dd>
<dt>Payoff date</dt><dd id="payoff">-</dd>
</dl>
<p class="note" id="pmiNote"></p>
</section>
</div>
{ad("inline")}
<h2>Amortization schedule</h2>
<div class="table-scroll"><table><thead><tr><th>Year</th><th>Principal</th><th>Interest</th><th>Balance</th></tr></thead><tbody id="sched"></tbody></table></div>
<section class="prose">
<h2>How your mortgage payment is calculated</h2>
<p>Principal and interest use the standard amortization formula: <code>M = P &times; r / (1 &minus; (1 + r)<sup>&minus;n</sup>)</code>, where P is the loan amount, r is the monthly rate and n is the number of payments. Property tax, insurance and HOA dues are added on top because most lenders collect them through escrow.</p>
<h3>When do you pay PMI?</h3>
<p>Conventional loans usually require private mortgage insurance when you put down less than 20%. PMI typically costs 0.3% to 1.5% of the loan per year and is removed once you reach 20% equity. This calculator drops PMI automatically when the balance falls below 80% of the home price.</p>
</section>
""",
    scripts=("states.js", "mortgage.js"),
    schema=calc_schema("Mortgage Calculator", desc, "mortgage-calculator.html"),
)

# ---------------------------------------------------------------- Auto loan
desc = "Calculate your monthly car payment with trade-in value, down payment, sales tax and fees. See total interest and the full cost of the loan."
page(
    "auto-loan-calculator.html",
    "Auto Loan Calculator: Monthly Car Payment with Tax and Trade-In",
    desc,
    f"""
{ad("leaderboard")}
<h1>Auto Loan Calculator</h1>
<p class="lede">Find the monthly payment and the true total cost of a new or used car.</p>
<div class="calc">
<form class="panel" id="form" novalidate><div class="fields">
{field("price", "Vehicle price", "38000", pre="$")}
{field("down", "Down payment", "4000", pre="$")}
{field("trade", "Trade-in value", "0", pre="$")}
{field("owed", "Owed on trade-in", "0", pre="$")}
{select("state", "State", STATES, "TX")}
{field("taxRate", "Sales tax", "8.2", post="%", hint="State plus average local rate; edit if yours differs")}
{field("fees", "Title &amp; fees", "800", pre="$")}
{field("rate", "Interest rate (APR)", "7.0", post="%")}
{select("term", "Loan term", [(str(m), f"{m} months") for m in (36, 48, 60, 72, 84)], "60")}
</div></form>
<section class="panel" aria-live="polite">
<div class="headline"><span class="eyebrow">Monthly payment</span><span class="big" id="monthly">-</span></div>
<div class="bar" id="bar"></div>
<dl class="kv">
<dt><span class="swatch" style="background:var(--accent)"></span>Amount financed</dt><dd id="financed">-</dd>
<dt><span class="swatch" style="background:#e0a64a"></span>Total interest</dt><dd id="interest">-</dd>
<dt>Sales tax</dt><dd id="tax">-</dd>
<dt class="total">Total cost of car</dt><dd class="total" id="totalCost">-</dd>
</dl>
<p class="note">Most states tax the price after subtracting the trade-in. Tax and fees are rolled into the loan here.</p>
</section>
</div>
{ad("inline")}
<section class="prose">
<h2>How to lower your car payment</h2>
<p>A larger down payment and a shorter term cut total interest the most. Stretching a loan to 72 or 84 months lowers the monthly payment but often leaves you owing more than the car is worth for several years.</p>
<h3>Compare terms</h3>
<div class="table-scroll"><table><thead><tr><th>Term</th><th>Monthly</th><th>Total interest</th></tr></thead><tbody id="compare"></tbody></table></div>
</section>
""",
    scripts=("states.js", "auto.js"),
    schema=calc_schema("Auto Loan Calculator", desc, "auto-loan-calculator.html"),
)

# ---------------------------------------------------------------- Paycheck
desc = "Estimate take-home pay after 2026 federal income tax, Social Security, Medicare, state income tax and 401(k) contributions for any US state."
page(
    "paycheck-calculator.html",
    "Paycheck Calculator 2026: Take-Home Pay After Taxes by State",
    desc,
    f"""
{ad("leaderboard")}
<h1>Paycheck Calculator</h1>
<p class="lede">Estimate your take-home pay per paycheck using 2026 federal tax brackets.</p>
<div class="calc">
<form class="panel" id="form" novalidate><div class="fields">
{field("salary", "Annual salary", "75000", pre="$")}
{select("freq", "Pay frequency", [("52","Weekly"),("26","Every 2 weeks"),("24","Twice a month"),("12","Monthly")], "26")}
{select("status", "Filing status", [("single","Single"),("mfj","Married filing jointly"),("hoh","Head of household")], "single")}
{select("state", "State", STATES, "TX")}
{field("stateRate", "Your own state tax rate", "", post="%", hint="Optional: leave blank to use your state's 2026 brackets", full=True)}
{field("k401", "401(k) contribution", "6", post="%", hint="Pre-tax, traditional")}
{field("health", "Health premium", "0", pre="$", hint="Pre-tax, per paycheck")}
</div></form>
<section class="panel" aria-live="polite">
<div class="headline"><span class="eyebrow" id="perLabel">Take-home per paycheck</span><span class="big" id="net">-</span></div>
<div class="bar" id="bar"></div>
<dl class="kv">
<dt>Gross pay</dt><dd id="gross">-</dd>
<dt><span class="swatch" style="background:#5b8def"></span>Federal income tax</dt><dd id="fed">-</dd>
<dt><span class="swatch" style="background:#e0a64a"></span>Social Security</dt><dd id="ss">-</dd>
<dt><span class="swatch" style="background:#c46b9a"></span>Medicare</dt><dd id="med">-</dd>
<dt><span class="swatch" style="background:#8a6fd1"></span>State income tax</dt><dd id="st">-</dd>
<dt><span class="swatch" style="background:#8a8f8c"></span>401(k) &amp; health</dt><dd id="pre">-</dd>
<dt class="total"><span class="swatch" style="background:var(--accent)"></span>Take-home</dt><dd class="total" id="net2">-</dd>
</dl>
<dl class="kv">
<dt>Annual take-home</dt><dd id="annualNet">-</dd>
<dt>Effective total tax rate</dt><dd id="eff">-</dd>
<dt>Federal marginal bracket</dt><dd id="marg">-</dd>
</dl>
<p class="note" id="stateNote"></p>
</section>
</div>
{ad("inline")}
<section class="prose">
<h2>What comes out of your paycheck</h2>
<p><strong>Federal income tax</strong> is calculated on your salary minus pre-tax deductions and the 2026 standard deduction ($16,100 single, $32,200 married filing jointly, $24,150 head of household), using the 2026 brackets from 10% to 37%.</p>
<p><strong>FICA</strong> is 6.2% for Social Security on wages up to $184,500 in 2026, plus 1.45% for Medicare on all wages and an extra 0.9% above $200,000 ($250,000 for joint filers).</p>
<p><strong>State income tax</strong> varies. Nine states have no wage income tax: Alaska, Florida, Nevada, New Hampshire, South Dakota, Tennessee, Texas, Washington and Wyoming. For every other state the calculator applies the 2026 state brackets, standard deduction and personal exemptions, using the single-filer brackets for heads of household. You can enter your own effective rate instead. Local and city taxes, such as those in New York City and Maryland counties, are not included.</p>
</section>
""",
    scripts=("paycheck.js",),
    schema=calc_schema("Paycheck Calculator", desc, "paycheck-calculator.html"),
)

# ---------------------------------------------------------------- 401(k)
desc = "Project your 401(k) balance at retirement with employer match, salary increases, investment returns and 2026 IRS contribution limits."
page(
    "401k-calculator.html",
    "401(k) Calculator: Retirement Savings with Employer Match",
    desc,
    f"""
{ad("leaderboard")}
<h1>401(k) Calculator</h1>
<p class="lede">See how much your 401(k) could be worth when you retire, including your employer match.</p>
<div class="calc">
<form class="panel" id="form" novalidate><div class="fields">
{field("age", "Current age", "30", step="1")}
{field("retire", "Retirement age", "65", step="1")}
{field("salary", "Annual salary", "75000", pre="$")}
{field("balance", "Current balance", "20000", pre="$")}
{field("contrib", "Your contribution", "8", post="%")}
{field("raise", "Annual raise", "3", post="%")}
{field("match", "Employer match", "50", post="%", hint="Of your contribution")}
{field("matchCap", "Match up to", "6", post="%", hint="Of salary")}
{field("ret", "Expected return", "7", post="%", hint="Before inflation", full=True)}
</div></form>
<section class="panel" aria-live="polite">
<div class="headline"><span class="eyebrow" id="atLabel">Balance at retirement</span><span class="big" id="final">-</span></div>
<dl class="kv">
<dt><span class="swatch" style="background:#5b8def"></span>Your contributions</dt><dd id="you">-</dd>
<dt><span class="swatch" style="background:#e0a64a"></span>Employer contributions</dt><dd id="emp">-</dd>
<dt><span class="swatch" style="background:var(--accent)"></span>Investment growth</dt><dd id="growth">-</dd>
<dt>Today's dollars (2.5% inflation)</dt><dd id="real">-</dd>
</dl>
<svg class="chart" id="chart" role="img" aria-label="401(k) balance by age"></svg>
<p class="note" id="limitNote"></p>
</section>
</div>
{ad("inline")}
<section class="prose">
<h2>2026 401(k) contribution limits</h2>
<p>You can defer up to $24,500 of salary in 2026. Workers aged 50 and older can add an $8,000 catch-up contribution, and those aged 60 to 63 get a higher catch-up of $11,250. Employer contributions do not count toward your personal limit. This calculator caps your own contributions at these limits and holds them flat in later years.</p>
<h3>Always get the full match</h3>
<p>An employer match is an instant return on your money. If your plan matches 50% up to 6% of pay, contributing at least 6% is the easiest raise you will ever get.</p>
</section>
""",
    scripts=("k401.js",),
    schema=calc_schema("401(k) Calculator", desc, "401k-calculator.html"),
)

# ---------------------------------------------------------------- Compound interest
desc = "See how your money grows with compound interest. Add monthly contributions, pick a compounding frequency and view year-by-year growth."
page(
    "compound-interest-calculator.html",
    "Compound Interest Calculator with Monthly Contributions",
    desc,
    f"""
{ad("leaderboard")}
<h1>Compound Interest Calculator</h1>
<p class="lede">Watch savings grow when interest earns interest.</p>
<div class="calc">
<form class="panel" id="form" novalidate><div class="fields">
{field("initial", "Initial deposit", "10000", pre="$")}
{field("monthly", "Monthly contribution", "500", pre="$")}
{field("rate", "Annual interest rate", "7", post="%")}
{field("years", "Years", "20", step="1")}
{select("comp", "Compounding", [("365","Daily"),("12","Monthly"),("4","Quarterly"),("1","Annually")], "12", full=True)}
</div></form>
<section class="panel" aria-live="polite">
<div class="headline"><span class="eyebrow">Future balance</span><span class="big" id="final">-</span></div>
<dl class="kv">
<dt><span class="swatch" style="background:#5b8def"></span>Total deposits</dt><dd id="dep">-</dd>
<dt><span class="swatch" style="background:var(--accent)"></span>Interest earned</dt><dd id="int">-</dd>
</dl>
<svg class="chart" id="chart" role="img" aria-label="Balance by year"></svg>
</section>
</div>
{ad("inline")}
<h2>Year-by-year growth</h2>
<div class="table-scroll"><table><thead><tr><th>Year</th><th>Deposits</th><th>Interest</th><th>Balance</th></tr></thead><tbody id="sched"></tbody></table></div>
<section class="prose">
<h2>The compound interest formula</h2>
<p>For a single deposit, <code>A = P(1 + r/n)<sup>nt</sup></code>, where P is the principal, r the annual rate, n the number of compounding periods per year and t the number of years. Regular contributions are added each month and then earn interest for the rest of the period.</p>
<h3>The rule of 72</h3>
<p>Divide 72 by your interest rate to estimate how many years it takes to double your money. At 7%, money doubles in about 10 years.</p>
</section>
""",
    scripts=("compound.js",),
    schema=calc_schema("Compound Interest Calculator", desc, "compound-interest-calculator.html"),
)

# ---------------------------------------------------------------- Home affordability
desc = "Find out how much house you can afford based on your income, debts, down payment and mortgage rate, using the 28/36 rule lenders use."
page(
    "home-affordability-calculator.html",
    "How Much House Can I Afford? Home Affordability Calculator",
    desc,
    f"""
{ad("leaderboard")}
<h1>Home Affordability Calculator</h1>
<p class="lede">See the home price your income supports before you talk to a lender.</p>
<div class="calc">
<form class="panel" id="form" novalidate><div class="fields">
{field("income", "Annual household income", "110000", pre="$", hint="Before taxes")}
{field("debts", "Monthly debt payments", "500", pre="$", hint="Car, student loans, card minimums")}
{field("down", "Down payment", "60000", pre="$")}
{field("rate", "Interest rate", "6.5", post="%")}
{select("term", "Loan term", [("30", "30 years"), ("20", "20 years"), ("15", "15 years")], "30")}
{select("state", "State", STATES, "TX")}
{field("taxRate", "Property tax", "1.58", post="%/yr", hint="Average for your state; edit if you know yours")}
{field("insurance", "Home insurance", "1800", pre="$", hint="per year")}
{field("hoa", "HOA dues", "0", pre="$", hint="per month")}
{select("rule", "Debt limit", [("36", "Conservative (28% / 36%)"), ("43", "Standard max (31% / 43%)")], "36", full=True, hint="Housing share / total debt share of gross income")}
</div></form>
<section class="panel" aria-live="polite">
<div class="headline"><span class="eyebrow">You can afford a home up to</span><span class="big" id="price">-</span></div>
<dl class="kv">
<dt>Loan amount</dt><dd id="loan">-</dd>
<dt>Down payment share</dt><dd id="downPct">-</dd>
<dt class="total">Monthly housing payment</dt><dd class="total" id="monthly">-</dd>
<dt><span class="swatch" style="background:var(--accent)"></span>Principal &amp; interest</dt><dd id="pi">-</dd>
<dt><span class="swatch" style="background:#5b8def"></span>Property tax</dt><dd id="tax">-</dd>
<dt><span class="swatch" style="background:#e0a64a"></span>Insurance &amp; HOA</dt><dd id="ins">-</dd>
</dl>
<p class="note" id="limitNote"></p>
</section>
</div>
{ad("inline")}
<section class="prose">
<h2>The 28/36 rule</h2>
<p>Most lenders want your housing payment (principal, interest, taxes and insurance) to stay under 28% of gross monthly income, and all debt payments together under 36%. Some loan programs, including many FHA and conventional loans, allow a total debt ratio up to 43% or higher with strong credit. This calculator uses whichever limit is lower for you.</p>
<h3>What raises your budget</h3>
<p>Paying off a car loan or credit card frees room under the 36% limit dollar for dollar. A larger down payment lowers the loan, and each 1 percentage point drop in the mortgage rate adds roughly 10% to the price you can afford. Remember to keep cash for closing costs, usually 2% to 5% of the price.</p>
</section>
""",
    scripts=("states.js", "affordability.js"),
    schema=calc_schema("Home Affordability Calculator", desc, "home-affordability-calculator.html"),
)

# ---------------------------------------------------------------- Personal loan
desc = "Calculate the monthly payment and total cost of a personal loan, including origination fees and the real APR you pay."
page(
    "personal-loan-calculator.html",
    "Personal Loan Calculator: Monthly Payment and True APR",
    desc,
    f"""
{ad("leaderboard")}
<h1>Personal Loan Calculator</h1>
<p class="lede">Compare loan offers by their real cost, including the origination fee.</p>
<div class="calc">
<form class="panel" id="form" novalidate><div class="fields">
{field("amount", "Loan amount", "15000", pre="$")}
{field("rate", "Interest rate", "12", post="%")}
{select("term", "Loan term", [(str(m), f"{m} months") for m in (12, 24, 36, 48, 60, 72, 84)], "36")}
{field("fee", "Origination fee", "5", post="%", hint="Taken out of the loan")}
</div></form>
<section class="panel" aria-live="polite">
<div class="headline"><span class="eyebrow">Monthly payment</span><span class="big" id="monthly">-</span></div>
<div class="bar" id="bar"></div>
<dl class="kv">
<dt><span class="swatch" style="background:var(--accent)"></span>Principal</dt><dd id="principal">-</dd>
<dt><span class="swatch" style="background:#e0a64a"></span>Total interest</dt><dd id="interest">-</dd>
<dt><span class="swatch" style="background:#c46b9a"></span>Origination fee</dt><dd id="feeOut">-</dd>
<dt class="total">Total cost of borrowing</dt><dd class="total" id="cost">-</dd>
</dl>
<dl class="kv">
<dt>Cash you receive</dt><dd id="cash">-</dd>
<dt>True APR with fee</dt><dd id="apr">-</dd>
</dl>
</section>
</div>
{ad("inline")}
<section class="prose">
<h2>Interest rate vs. APR</h2>
<p>The interest rate sets your payment. The APR adds the origination fee, which lenders usually subtract from the money you receive, so you pay interest on cash you never get. When comparing offers, compare APRs. A loan at 11% with a 6% fee can cost more than one at 13% with no fee.</p>
<h3>Typical rates</h3>
<p>Personal loan APRs in the US range from about 7% for excellent credit to 36% for fair or poor credit. Credit unions often charge less and rarely add origination fees.</p>
</section>
""",
    scripts=("personal-loan.js",),
    schema=calc_schema("Personal Loan Calculator", desc, "personal-loan-calculator.html"),
)

# ---------------------------------------------------------------- Credit card payoff
desc = "See how long it will take to pay off your credit card and how much interest you will pay, or find the payment needed to be debt-free by a target date."
page(
    "credit-card-payoff-calculator.html",
    "Credit Card Payoff Calculator: How Long to Pay Off Your Balance",
    desc,
    f"""
{ad("leaderboard")}
<h1>Credit Card Payoff Calculator</h1>
<p class="lede">Find your debt-free date and what the interest is really costing you.</p>
<div class="calc">
<form class="panel" id="form" novalidate><div class="fields">
{field("balance", "Card balance", "6500", pre="$")}
{field("apr", "APR", "22.9", post="%")}
{field("payment", "Monthly payment", "250", pre="$")}
{field("goal", "Or pay off in", "24", post="mo", hint="Shows the payment needed")}
</div></form>
<section class="panel" aria-live="polite">
<div class="headline"><span class="eyebrow">Paid off in</span><span class="big" id="time">-</span></div>
<dl class="kv">
<dt>Debt-free date</dt><dd id="date">-</dd>
<dt>Total interest</dt><dd id="interest">-</dd>
<dt class="total">Total paid</dt><dd class="total" id="total">-</dd>
</dl>
<dl class="kv">
<dt id="goalLabel">Payment to finish in 24 months</dt><dd id="goalPay">-</dd>
<dt>Interest with that plan</dt><dd id="goalInt">-</dd>
</dl>
<p class="note" id="warn"></p>
</section>
</div>
{ad("inline")}
<h2>How your payment changes the outcome</h2>
<div class="table-scroll"><table><thead><tr><th>Monthly payment</th><th>Months</th><th>Total interest</th></tr></thead><tbody id="compare"></tbody></table></div>
<section class="prose">
<h2>Why minimum payments take so long</h2>
<p>Card minimums are usually 1% of the balance plus interest, so most of each payment goes to interest and the balance barely moves. At a 22% APR, a $6,500 balance on minimum payments can take over 15 years to clear. Adding even $50 a month cuts years off.</p>
<h3>Ways to pay less interest</h3>
<p>A 0% balance transfer card stops interest for 12 to 21 months, usually for a 3% to 5% fee. A personal loan at a lower rate can also replace card debt with a fixed payoff date. If you have several cards, paying the highest APR first (the avalanche method) saves the most money.</p>
</section>
""",
    scripts=("credit-card.js",),
    schema=calc_schema("Credit Card Payoff Calculator", desc, "credit-card-payoff-calculator.html"),
)

# ---------------------------------------------------------------- Debt-to-income
desc = "Calculate your debt-to-income (DTI) ratio and see how lenders will view it for a mortgage, auto loan or personal loan."
page(
    "debt-to-income-calculator.html",
    "Debt-to-Income Ratio Calculator (DTI) for Mortgages and Loans",
    desc,
    f"""
{ad("leaderboard")}
<h1>Debt-to-Income Ratio Calculator</h1>
<p class="lede">Check the number lenders look at first when you apply for a loan.</p>
<div class="calc">
<form class="panel" id="form" novalidate><div class="fields">
{field("income", "Gross monthly income", "7000", pre="$", hint="Before taxes", full=True)}
{field("housing", "Rent or mortgage", "1900", pre="$", hint="Include tax, insurance, HOA")}
{field("car", "Car loans", "450", pre="$")}
{field("student", "Student loans", "300", pre="$")}
{field("cards", "Card minimums", "120", pre="$")}
{field("other", "Other debts", "0", pre="$", hint="Personal loans, child support")}
</div></form>
<section class="panel" aria-live="polite">
<div class="headline"><span class="eyebrow">Your debt-to-income ratio</span><span class="big" id="dti">-</span></div>
<p id="verdict" class="verdict"></p>
<dl class="kv">
<dt>Total monthly debt</dt><dd id="total">-</dd>
<dt>Housing ratio (front-end)</dt><dd id="front">-</dd>
<dt>Room left under 36%</dt><dd id="room">-</dd>
</dl>
<div class="scale" aria-hidden="true"><span style="flex:36"></span><span style="flex:7"></span><span style="flex:7"></span><span style="flex:10"></span><i id="marker"></i></div>
<div class="scale-labels" aria-hidden="true"><span>0%</span><span>36%</span><span>43%</span><span>50%</span><span>60%+</span></div>
</section>
</div>
{ad("inline")}
<section class="prose">
<h2>What is a good debt-to-income ratio?</h2>
<p><strong>36% or less</strong> is considered healthy and qualifies for the best rates. <strong>37% to 43%</strong> is acceptable for most mortgages, and 43% is the traditional limit for a qualified mortgage. <strong>44% to 49%</strong> is possible with some programs, such as FHA loans with strong credit or reserves. <strong>50% and above</strong> makes most loans hard to get.</p>
<h3>What counts as debt</h3>
<p>Count required monthly payments: housing, car loans, student loans, minimum card payments, personal loans, alimony and child support. Utilities, groceries, phone bills and insurance premiums are not included. Use income before taxes.</p>
</section>
""",
    scripts=("dti.js",),
    schema=calc_schema("Debt-to-Income Calculator", desc, "debt-to-income-calculator.html"),
)

# ---------------------------------------------------------------- Salary to hourly
desc = "Convert your salary to an hourly wage or your hourly rate to an annual salary, with daily, weekly, biweekly and monthly pay."
page(
    "salary-to-hourly-calculator.html",
    "Salary to Hourly Calculator: Convert Hourly Wage to Annual Salary",
    desc,
    f"""
{ad("leaderboard")}
<h1>Salary to Hourly Calculator</h1>
<p class="lede">Convert any pay rate to every other pay period at once.</p>
<div class="calc">
<form class="panel" id="form" novalidate><div class="fields">
{field("amount", "Pay amount", "65000", pre="$")}
{select("per", "Paid per", [("hour","Hour"),("day","Day"),("week","Week"),("biweek","2 weeks"),("semimonth","Half month"),("month","Month"),("year","Year")], "year")}
{field("hours", "Hours per week", "40")}
{field("days", "Days per week", "5")}
{field("weeks", "Paid weeks per year", "52", hint="Use 50 if 2 weeks are unpaid", full=True)}
</div></form>
<section class="panel" aria-live="polite">
<div class="headline"><span class="eyebrow">Hourly rate</span><span class="big" id="hourly">-</span></div>
<dl class="kv">
<dt>Daily</dt><dd id="daily">-</dd>
<dt>Weekly</dt><dd id="weekly">-</dd>
<dt>Every 2 weeks</dt><dd id="biweekly">-</dd>
<dt>Twice a month</dt><dd id="semimonthly">-</dd>
<dt>Monthly</dt><dd id="monthly">-</dd>
<dt class="total">Yearly</dt><dd class="total" id="yearly">-</dd>
</dl>
<p class="note">Amounts are gross pay before taxes. See the <a href="paycheck-calculator.html">paycheck calculator</a> for take-home pay.</p>
</section>
</div>
{ad("inline")}
<section class="prose">
<h2>Quick conversion rule</h2>
<p>For a full-time job of 40 hours a week and 52 paid weeks, a year has 2,080 work hours. Divide a salary by 2,080 to get the hourly rate, or multiply an hourly wage by 2,080 for the annual salary. A shortcut: double the hourly rate and add three zeros. $25 an hour is about $50,000 a year.</p>
<h3>Common salaries as hourly wages</h3>
<div class="table-scroll"><table><thead><tr><th>Salary</th><th>Hourly (2,080 hrs)</th><th>Monthly</th></tr></thead><tbody>
{"".join(f"<tr><td>${s:,}</td><td>${s / 2080:,.2f}</td><td>${s / 12:,.0f}</td></tr>" for s in (30000, 40000, 50000, 60000, 75000, 100000, 125000, 150000))}
</tbody></table></div>
</section>
""",
    scripts=("salary.js",),
    schema=calc_schema("Salary to Hourly Calculator", desc, "salary-to-hourly-calculator.html"),
)

# ---------------------------------------------------------------- Savings goal
desc = "Find out how much you need to save each month to reach a savings goal by a target date, including interest earned along the way."
page(
    "savings-goal-calculator.html",
    "Savings Goal Calculator: How Much to Save Each Month",
    desc,
    f"""
{ad("leaderboard")}
<h1>Savings Goal Calculator</h1>
<p class="lede">Turn a goal and a deadline into a monthly savings amount.</p>
<div class="calc">
<form class="panel" id="form" novalidate><div class="fields">
{field("goal", "Savings goal", "30000", pre="$")}
{field("current", "Already saved", "5000", pre="$")}
{field("years", "Years to reach it", "4", step="0.5")}
{field("rate", "Interest rate (APY)", "4", post="%", hint="High-yield savings")}
</div></form>
<section class="panel" aria-live="polite">
<div class="headline"><span class="eyebrow">Save each month</span><span class="big" id="monthly">-</span></div>
<dl class="kv">
<dt><span class="swatch" style="background:#5b8def"></span>Your deposits</dt><dd id="dep">-</dd>
<dt><span class="swatch" style="background:var(--accent)"></span>Interest earned</dt><dd id="int">-</dd>
<dt>Without interest you would need</dt><dd id="noInt">-</dd>
</dl>
<svg class="chart" id="chart" role="img" aria-label="Savings balance by month"></svg>
<p class="note" id="note"></p>
</section>
</div>
{ad("inline")}
<section class="prose">
<h2>Where to keep savings for a goal</h2>
<p>For goals under five years, such as an emergency fund, a down payment or a car, a high-yield savings account or certificates of deposit keep the money safe while earning interest. Money for goals more than five years away can be invested for higher growth, with more risk.</p>
<h3>Make it automatic</h3>
<p>Set up an automatic transfer on payday for the amount above. Saving first and spending what is left works better than saving what remains at the end of the month.</p>
</section>
""",
    scripts=("savings-goal.js",),
    schema=calc_schema("Savings Goal Calculator", desc, "savings-goal-calculator.html"),
)

HEALTH_NOTE = '<p class="note">For adults. This is an estimate for general information, not medical advice. Talk to a doctor about your own health.</p>'

# ---------------------------------------------------------------- BMI
desc = "Calculate your body mass index (BMI) from height and weight in feet, inches and pounds, see your weight category and the healthy weight range for your height."
page(
    "bmi-calculator.html",
    "BMI Calculator: Body Mass Index and Healthy Weight for Adults",
    desc,
    f"""
{ad("leaderboard")}
<h1>BMI Calculator</h1>
<p class="lede">Check your body mass index and the healthy weight range for your height.</p>
<div class="calc">
<form class="panel" id="form" novalidate><div class="fields">
{field("ft", "Height (feet)", "5", post="ft", step="1")}
{field("in", "Height (inches)", "9", post="in")}
{field("lb", "Weight", "170", post="lb", full=True)}
</div></form>
<section class="panel" aria-live="polite">
<div class="headline"><span class="eyebrow">Your BMI</span><span class="big" id="bmi">-</span></div>
<p id="verdict" class="verdict"></p>
<div class="scale bmi-scale" aria-hidden="true"><span style="flex:3.5"></span><span style="flex:6.5"></span><span style="flex:5"></span><span style="flex:10"></span><i id="marker"></i></div>
<div class="scale-labels bmi-labels" aria-hidden="true"><span>15</span><span>18.5</span><span>25</span><span>30</span><span>40</span></div>
<dl class="kv">
<dt>Healthy weight for your height</dt><dd id="range">-</dd>
<dt>Change to reach that range</dt><dd id="toRange">-</dd>
<dt>Metric</dt><dd id="metric">-</dd>
</dl>
{HEALTH_NOTE}
</section>
</div>
{ad("inline")}
<section class="prose">
<h2>BMI categories for adults</h2>
<div class="table-scroll"><table><thead><tr><th>BMI</th><th>Category</th></tr></thead><tbody>
<tr><td>Below 18.5</td><td>Underweight</td></tr>
<tr><td>18.5 to 24.9</td><td>Healthy weight</td></tr>
<tr><td>25.0 to 29.9</td><td>Overweight</td></tr>
<tr><td>30.0 and above</td><td>Obesity</td></tr>
</tbody></table></div>
<h2>How BMI is calculated</h2>
<p>BMI is your weight in kilograms divided by your height in meters squared. In US units the formula is <code>BMI = 703 &times; weight (lb) / height (in)<sup>2</sup></code>. A person 5 feet 9 inches tall (69 inches) who weighs 170 pounds has a BMI of 703 &times; 170 / 4,761 = 25.1.</p>
<h3>What BMI does not show</h3>
<p>BMI is a quick screening number, not a diagnosis. It does not separate muscle from fat, so athletes can score as overweight, and it does not show where fat is stored. Waist size, blood pressure, blood sugar and cholesterol give a fuller picture. These ranges are for adults 20 and older; children and teens use BMI-for-age percentiles.</p>
</section>
""",
    scripts=("bmi.js",),
    schema=calc_schema("BMI Calculator", desc, "bmi-calculator.html", "HealthApplication"),
)

# ---------------------------------------------------------------- Calories
desc = "Find how many calories you need per day to maintain, lose or gain weight, using the Mifflin-St Jeor equation with your age, sex, height, weight and activity level."
page(
    "calorie-calculator.html",
    "Calorie Calculator: Daily Calories to Lose, Maintain or Gain Weight",
    desc,
    f"""
{ad("leaderboard")}
<h1>Calorie Calculator</h1>
<p class="lede">Estimate the calories you burn each day and the intake that fits your goal.</p>
<div class="calc">
<form class="panel" id="form" novalidate><div class="fields">
{field("age", "Age", "35", post="yrs", step="1")}
{select("sex", "Sex", [("f", "Female"), ("m", "Male")], "f")}
{field("ft", "Height (feet)", "5", post="ft", step="1")}
{field("in", "Height (inches)", "5", post="in")}
{field("lb", "Weight", "160", post="lb", full=True)}
{select("activity", "Activity level", [("1.2", "Sedentary: little or no exercise"), ("1.375", "Light: exercise 1 to 3 days a week"), ("1.55", "Moderate: exercise 3 to 5 days a week"), ("1.725", "Active: hard exercise 6 to 7 days a week"), ("1.9", "Very active: physical job or training twice a day")], "1.375", full=True)}
</div></form>
<section class="panel" aria-live="polite">
<div class="headline"><span class="eyebrow">Calories to maintain your weight</span><span class="big" id="tdee">-</span></div>
<dl class="kv">
<dt>Lose 1 lb a week</dt><dd id="lose1">-</dd>
<dt>Lose 0.5 lb a week</dt><dd id="lose05">-</dd>
<dt>Gain 0.5 lb a week</dt><dd id="gain05">-</dd>
<dt>Gain 1 lb a week</dt><dd id="gain1">-</dd>
</dl>
<dl class="kv">
<dt>Calories burned at rest (BMR)</dt><dd id="bmr">-</dd>
</dl>
<p class="note" id="note"></p>
{HEALTH_NOTE}
</section>
</div>
{ad("inline")}
<section class="prose">
<h2>How your calorie needs are calculated</h2>
<p>The calculator first estimates your basal metabolic rate (BMR), the calories your body uses at rest, with the Mifflin-St Jeor equation: <code>10 &times; weight (kg) + 6.25 &times; height (cm) &minus; 5 &times; age + 5</code> for men, or <code>&minus; 161</code> instead of <code>+ 5</code> for women. It then multiplies BMR by an activity factor from 1.2 for a desk job with no exercise to 1.9 for very heavy activity. The result is your total daily energy expenditure, the calories that keep your weight steady.</p>
<h3>Calories and weight change</h3>
<p>A common rule of thumb is that a deficit of about 500 calories a day leads to roughly 1 pound of weight loss per week. Real results vary because the body adapts as weight changes, so recheck your numbers every 10 to 15 pounds. Most adults should not eat less than about 1,200 calories (women) or 1,500 calories (men) a day without medical supervision.</p>
</section>
""",
    scripts=("calories.js",),
    schema=calc_schema("Calorie Calculator", desc, "calorie-calculator.html", "HealthApplication"),
)

# ---------------------------------------------------------------- Due date
desc = "Estimate your pregnancy due date from the first day of your last period, with your current week of pregnancy, trimester dates and estimated conception date."
page(
    "due-date-calculator.html",
    "Due Date Calculator: When Is My Baby Due?",
    desc,
    f"""
{ad("leaderboard")}
<h1>Due Date Calculator</h1>
<p class="lede">Find your estimated due date and how far along you are.</p>
<div class="calc">
<form class="panel" id="form" novalidate><div class="fields">
{field("lmp", "First day of last period", "", type_="date", full=True)}
{field("cycle", "Average cycle length", "28", post="days", step="1", hint="Usually 21 to 35 days", full=True)}
</div></form>
<section class="panel" aria-live="polite">
<div class="headline"><span class="eyebrow">Estimated due date</span><span class="big" id="due">-</span></div>
<dl class="kv">
<dt>How far along you are</dt><dd id="week">-</dd>
<dt>Trimester</dt><dd id="trimester">-</dd>
<dt>Days until due date</dt><dd id="left">-</dd>
</dl>
<dl class="kv">
<dt>Estimated conception</dt><dd id="conception">-</dd>
<dt>Second trimester starts</dt><dd id="tri2">-</dd>
<dt>Third trimester starts</dt><dd id="tri3">-</dd>
</dl>
<p class="note">An estimate for general information, not medical advice. Your doctor or midwife may adjust the date after an ultrasound.</p>
</section>
</div>
{ad("inline")}
<section class="prose">
<h2>How the due date is calculated</h2>
<p>Doctors usually count pregnancy as 40 weeks (280 days) from the first day of your last menstrual period, a method known as Naegele's rule. Ovulation and conception happen about two weeks after that day in a 28-day cycle, so you are already considered two weeks pregnant at conception. If your cycles are longer or shorter than 28 days, the calculator moves the due date by the difference.</p>
<h3>How accurate is a due date?</h3>
<p>Only about 4% of babies arrive on the exact due date. Most are born within two weeks either side of it. A first-trimester ultrasound measures the baby and is the most accurate way to date a pregnancy, so your provider may change the date after your first scan.</p>
<h3>Trimesters</h3>
<p>The first trimester runs through week 13, the second from week 14 through week 27, and the third from week 28 until birth.</p>
</section>
""",
    scripts=("due-date.js",),
    schema=calc_schema("Due Date Calculator", desc, "due-date-calculator.html", "HealthApplication"),
)

# ---------------------------------------------------------------- Percentage
desc = "Free percentage calculator: find a percent of a number, what percent one number is of another, and the percent increase or decrease between two values."
page(
    "percentage-calculator.html",
    "Percentage Calculator: Percent Of, Percent Change and More",
    desc,
    f"""
{ad("leaderboard")}
<h1>Percentage Calculator</h1>
<p class="lede">Three common percent questions, answered as you type.</p>
<div class="calc">
<form class="panel" id="form" novalidate><div class="fields">
{field("p1", "What is", "15", post="%")}
{field("v1", "of", "80")}
{field("a2", "Number", "30")}
{field("b2", "is what % of", "120")}
{field("from", "Change from", "50")}
{field("to", "to", "65")}
</div></form>
<section class="panel" aria-live="polite">
<div class="headline"><span class="eyebrow">Percent of a number</span><span class="big" id="r1">-</span></div>
<dl class="kv">
<dt>Percent one number is of another</dt><dd id="r2">-</dd>
<dt>Percent change</dt><dd id="r3">-</dd>
<dt>Difference</dt><dd id="diff">-</dd>
</dl>
</section>
</div>
{ad("inline")}
<section class="prose">
<h2>Percentage formulas</h2>
<p><strong>Percent of a number:</strong> multiply the number by the percent and divide by 100. 15% of 80 is 80 &times; 15 / 100 = 12.</p>
<p><strong>What percent one number is of another:</strong> divide the part by the whole and multiply by 100. 30 is 30 / 120 &times; 100 = 25% of 120.</p>
<p><strong>Percent change:</strong> subtract the old value from the new one, divide by the old value and multiply by 100. Going from 50 to 65 is (65 &minus; 50) / 50 &times; 100 = a 30% increase.</p>
<h3>Percent change vs. percentage points</h3>
<p>When a rate rises from 4% to 5%, it went up 1 percentage point, but the rate itself increased by 25%. News reports and loan offers often mix these up, so check which one is meant.</p>
</section>
""",
    scripts=("percentage.js",),
    schema=calc_schema("Percentage Calculator", desc, "percentage-calculator.html", "UtilitiesApplication"),
)

# ---------------------------------------------------------------- Tip
desc = "Calculate the tip and total for a restaurant bill and split it between any number of people, with an option to round up each share."
page(
    "tip-calculator.html",
    "Tip Calculator: Tip, Total and Split the Bill",
    desc,
    f"""
{ad("leaderboard")}
<h1>Tip Calculator</h1>
<p class="lede">Work out the tip and split the check in seconds.</p>
<div class="calc">
<form class="panel" id="form" novalidate><div class="fields">
{field("bill", "Bill amount", "84.50", pre="$")}
{field("pct", "Tip", "18", post="%")}
{field("people", "Number of people", "2", step="1")}
{select("round", "Round up each share", [("0", "No"), ("1", "Yes, to the next dollar")], "0")}
</div></form>
<section class="panel" aria-live="polite">
<div class="headline"><span class="eyebrow">Each person pays</span><span class="big" id="perPerson">-</span></div>
<dl class="kv">
<dt>Tip</dt><dd id="tip">-</dd>
<dt>Tip per person</dt><dd id="tipPer">-</dd>
<dt>Effective tip</dt><dd id="effPct">-</dd>
<dt class="total">Total with tip</dt><dd class="total" id="total">-</dd>
</dl>
</section>
</div>
{ad("inline")}
<h2>Tip amounts for this bill</h2>
<div class="table-scroll"><table><thead><tr><th>Tip</th><th>Tip amount</th><th>Total</th><th>Per person</th></tr></thead><tbody id="compare"></tbody></table></div>
<section class="prose">
<h2>How much to tip in the US</h2>
<div class="table-scroll"><table><thead><tr><th>Service</th><th>Typical tip</th></tr></thead><tbody>
<tr><td>Sit-down restaurant</td><td>15% to 20% of the pre-tax bill</td></tr>
<tr><td>Bar</td><td>$1 to $2 per drink, or 15% to 20% of the tab</td></tr>
<tr><td>Food delivery</td><td>15% to 20%, at least $3 to $5</td></tr>
<tr><td>Taxi or rideshare</td><td>10% to 20%</td></tr>
<tr><td>Hair salon or barber</td><td>15% to 20%</td></tr>
<tr><td>Hotel housekeeping</td><td>$2 to $5 per night</td></tr>
</tbody></table></div>
<h3>Quick mental math</h3>
<p>For 20%, move the decimal point one place left and double it: on a $45 bill, 10% is $4.50, so 20% is $9. For 15%, add half of the 10% amount: $4.50 + $2.25 = $6.75.</p>
</section>
""",
    scripts=("tip.js",),
    schema=calc_schema("Tip Calculator", desc, "tip-calculator.html", "UtilitiesApplication"),
)

# ---------------------------------------------------------------- Age
desc = "Calculate your exact age in years, months and days from your date of birth, plus your age in months, weeks and days and the days until your next birthday."
page(
    "age-calculator.html",
    "Age Calculator: How Old Am I in Years, Months and Days?",
    desc,
    f"""
{ad("leaderboard")}
<h1>Age Calculator</h1>
<p class="lede">Your exact age on any date, down to the day.</p>
<div class="calc">
<form class="panel" id="form" novalidate><div class="fields">
{field("birth", "Date of birth", "1990-06-15", type_="date", full=True)}
{field("asof", "Age on this date", "", type_="date", hint="Today by default", full=True)}
</div></form>
<section class="panel" aria-live="polite">
<div class="headline"><span class="eyebrow">Age</span><span class="big" id="age">-</span></div>
<dl class="kv">
<dt>Exact age</dt><dd id="ymd">-</dd>
<dt>In months</dt><dd id="months">-</dd>
<dt>In weeks</dt><dd id="weeks">-</dd>
<dt>In days</dt><dd id="days">-</dd>
<dt>Day of the week you were born</dt><dd id="born">-</dd>
<dt>Next birthday in</dt><dd id="next">-</dd>
</dl>
</section>
</div>
{ad("inline")}
<section class="prose">
<h2>How age is calculated</h2>
<p>Age counts the full years since your date of birth, then the full months since your last birthday, then the days since that month began. Someone born on June 15, 1990 is 35 years, 4 months and 14 days old on October 29, 2025. Months have different lengths, so the day count borrows the length of the previous month when needed.</p>
<h3>Birthdays on February 29</h3>
<p>People born on leap day usually celebrate on March 1 in common years, and that is the date this calculator uses. In the US, legal age for things like a driver's license or voting is generally reached on March 1 in a non-leap year.</p>
</section>
""",
    scripts=("age.js",),
    schema=calc_schema("Age Calculator", desc, "age-calculator.html", "UtilitiesApplication"),
)

# ---------------------------------------------------------------- GPA
# Option values must be unique for select() to preselect one, so A+ and A differ only in spelling.
GRADES = [("", "-"), ("4.0", "A+"), ("4", "A"), ("3.7", "A-"), ("3.3", "B+"), ("3", "B"), ("2.7", "B-"), ("2.3", "C+"),
          ("2", "C"), ("1.7", "C-"), ("1.3", "D+"), ("1", "D"), ("0.7", "D-"), ("0", "F")]
COURSES = 8
desc = "Calculate your semester GPA and cumulative GPA on the 4.0 scale from letter grades and credit hours for up to 8 classes."
page(
    "gpa-calculator.html",
    "GPA Calculator: Semester and Cumulative GPA on a 4.0 Scale",
    desc,
    f"""
{ad("leaderboard")}
<h1>GPA Calculator</h1>
<p class="lede">Enter a letter grade and credit hours for each class. Leave unused rows blank.</p>
<div class="calc">
<form class="panel" id="form" novalidate><div class="fields">
{"".join(select(f"g{i}", f"Class {i} grade", GRADES, ["4", "3.3", "3.7", "3"][i - 1] if i <= 4 else "") + field(f"c{i}", f"Class {i} credits", "3" if i <= 4 else "", step="1") for i in range(1, COURSES + 1))}
{field("prevGpa", "Current cumulative GPA", "", hint="Optional")}
{field("prevCredits", "Credits already completed", "", step="1", hint="Optional")}
</div></form>
<section class="panel" aria-live="polite">
<div class="headline"><span class="eyebrow">Semester GPA</span><span class="big" id="gpa">-</span></div>
<dl class="kv">
<dt>Credits this term</dt><dd id="credits">-</dd>
<dt>Grade points</dt><dd id="points">-</dd>
<dt class="total">Cumulative GPA</dt><dd class="total" id="cum">-</dd>
</dl>
</section>
</div>
{ad("inline")}
<section class="prose">
<h2>Grade points on the 4.0 scale</h2>
<div class="table-scroll"><table><thead><tr><th>Grade</th><th>Points</th><th>Grade</th><th>Points</th></tr></thead><tbody>
<tr><td>A+ / A</td><td>4.0</td><td>C+</td><td>2.3</td></tr>
<tr><td>A-</td><td>3.7</td><td>C</td><td>2.0</td></tr>
<tr><td>B+</td><td>3.3</td><td>C-</td><td>1.7</td></tr>
<tr><td>B</td><td>3.0</td><td>D+ / D / D-</td><td>1.3 / 1.0 / 0.7</td></tr>
<tr><td>B-</td><td>2.7</td><td>F</td><td>0.0</td></tr>
</tbody></table></div>
<h2>How GPA is calculated</h2>
<p>Multiply each class's grade points by its credit hours, add the results, and divide by the total credit hours. An A (4.0) in a 3-credit class and a B (3.0) in a 4-credit class give (12 + 12) / 7 = 3.43. To get a cumulative GPA, add your previous grade points (old GPA &times; old credits) to this term's and divide by all credits combined.</p>
<h3>Weighted and unweighted GPA</h3>
<p>This calculator gives an unweighted GPA, the standard used by most colleges. Some high schools add a point for honors, AP or IB classes, so a weighted GPA can go above 4.0. Check your school's scale if it uses A+ as 4.3 or rounds differently.</p>
</section>
""",
    scripts=("gpa.js",),
    schema=calc_schema("GPA Calculator", desc, "gpa-calculator.html", "EducationalApplication"),
)

# ---------------------------------------------------------------- About / Privacy (required for AdSense review)
page(
    "about.html",
    f"About {SITE_NAME}",
    "About Plain Money Calculators: who makes them, our sources for tax, loan, BMI and calorie formulas, and why every calculation stays private in your browser.",
    f"""<section class="prose"><h1>About</h1>
<p>{SITE_NAME} builds free, fast and private calculators for money, health and everyday decisions. Every calculation runs in your browser, so the numbers you type are never sent to a server.</p>
<p>Tax figures come from IRS and Social Security Administration publications for the 2026 tax year. Health calculators use the CDC adult BMI ranges, the Mifflin-St Jeor equation and the standard 280-day pregnancy rule. Results are estimates for planning and are not financial, tax, legal or medical advice.</p>
<p>Questions or corrections: <strong>hello@plainmoneycalc.com</strong></p></section>""",
)
page(
    "privacy.html",
    "Privacy Policy",
    "How Plain Money Calculators handles your data: what you type stays in your browser, plus how we use cookies, Google AdSense ads and Google Analytics.",
    f"""<section class="prose"><h1>Privacy Policy</h1>
<p>Last updated: October 2026.</p>
<p>The numbers you enter in our calculators stay in your browser and are not collected or stored by us.</p>
<h2>Advertising</h2>
<p>We use Google AdSense to show ads. Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visits to this site and other sites on the internet. You may opt out of personalized advertising by visiting <a href="https://www.google.com/settings/ads" rel="nofollow">Google Ads Settings</a> or <a href="https://www.aboutads.info/choices/" rel="nofollow">aboutads.info</a>.</p>
<h2>Analytics</h2>
<p>We use Google Analytics to understand how visitors use the site, such as which pages are viewed. Google Analytics uses cookies and collects data like your approximate location, device and browser, but not the numbers you enter in calculators. You can opt out with the <a href="https://tools.google.com/dlpage/gaoptout" rel="nofollow">Google Analytics opt-out browser add-on</a>.</p>
<h2>California residents</h2>
<p>Under the CCPA you may request access to or deletion of personal information. Because our calculators do not collect personal data, we generally hold none about you. Contact <strong>hello@plainmoneycalc.com</strong> with any request.</p>
</section>""",
)


# ---------------------------------------------------------------- translated pages + script strings
# Strings the calculator scripts show; they call Calc.t() with these exact English templates.
JS_STRINGS = json.loads((I18N_DIR / "js-strings.json").read_text())
for text in JS_STRINGS:
    SOURCE[key(text)] = text
built = {}
for lang in TR:
    built[lang] = [f for f, *rest in PAGES if page(f, *rest, lang=lang)]
    js_tr = {t: TR[lang][key(t)] for t in JS_STRINGS if key(t) in TR[lang]}
    # Plural forms ({one, few, many, other}) for languages that need them; Calc.t picks one by number.
    if (plurals := I18N_DIR / f"{lang}-plurals.json").exists():
        js_tr.update(json.loads(plurals.read_text()))
    (ROOT / "assets" / f"i18n-{lang}.js").write_text(
        f"// Generated by build.py from i18n/{lang}.json.\nwindow.I18N = " + json.dumps(js_tr, ensure_ascii=False, indent=0) + ";\n"
    )
    # todo-{lang}.html is what goes to DeepL; each block keeps its key so translations map back.
    missing = {k: v for k, v in SOURCE.items() if k not in TR[lang]}
    todo = I18N_DIR / f"todo-{lang}.html"
    if missing:
        todo.write_text(
            f'<!doctype html><html lang="en"><head><meta charset="utf-8"></head><body>\n'
            + "".join(f'<article id="k{k}">\n{v}\n</article>\n' for k, v in missing.items())
            + "</body></html>\n"
        )
        print(f"{len(missing)} strings need {lang}: see i18n/README.md")
    elif todo.exists():
        todo.unlink()

# ---------------------------------------------------------------- robots.txt / sitemap.xml
pages = [p for p in ["", *(h for h, _, _ in CARDS), "about.html", "privacy.html"]]
(ROOT / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{SITE_URL}/{p.removesuffix('.html')}</loc></url>\n" for p in pages)
    + "".join(f"  <url><loc>{SITE_URL}/{lang}/{clean(f)}</loc></url>\n"
              for lang, files in built.items() for f in files)
    + "</urlset>\n"
)
if ADSENSE_CLIENT:
    (ROOT / "ads.txt").write_text(f"google.com, {ADSENSE_CLIENT.removeprefix('ca-')}, DIRECT, f08c47fec0942fa0\n")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
print(f"Built {len(PAGES)} English pages; " + ", ".join(f"{len(v)} {k}" for k, v in built.items()))
