#!/usr/bin/env python3
"""Generates the static HTML pages from the templates below.

Run `python3 build.py`; it writes *.html next to this file. Edit content here, not in the generated HTML.
"""
from pathlib import Path
import json

SITE_NAME = "Plain Money Calculators"
SITE_URL = "https://example.com"  # TODO: replace with the real domain before launch
ADSENSE_CLIENT = ""  # TODO: set to "ca-pub-XXXXXXXXXXXXXXXX" after AdSense approval
ROOT = Path(__file__).parent

NAV = [
    ("mortgage-calculator.html", "Mortgage"),
    ("auto-loan-calculator.html", "Auto Loan"),
    ("paycheck-calculator.html", "Paycheck"),
    ("401k-calculator.html", "401(k)"),
    ("compound-interest-calculator.html", "Compound Interest"),
]


def ad(kind, label="Advertisement"):
    # Placeholder that keeps its height; swap the inner content for an <ins class="adsbygoogle"> unit.
    return f'<div class="ad-slot ad-{kind}" aria-label="Advertisement">{label}</div>'


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


def page(filename, title, description, body, scripts=(), schema=None):
    nav = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == filename else ""}>{text}</a>' for href, text in NAV
    )
    adsense = (
        f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_CLIENT}" crossorigin="anonymous"></script>'
        if ADSENSE_CLIENT else "<!-- AdSense script goes here once ADSENSE_CLIENT is set in build.py -->"
    )
    canonical = f"{SITE_URL}/{'' if filename == 'index.html' else filename}"
    ld = f'<script type="application/ld+json">{json.dumps(schema)}</script>' if schema else ""
    js = "".join(f'<script src="assets/{s}"></script>' for s in ("common.js", *scripts))
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@700;800&family=IBM+Plex+Mono:wght@500;700&family=Public+Sans:wght@400;500;600&display=swap">
<link rel="stylesheet" href="assets/style.css">
{adsense}
{ld}
</head>
<body>
<header class="site-header"><div class="wrap">
<a class="logo" href="./">Plain<span>Money</span></a>
<nav class="site-nav" aria-label="Calculators">{nav}</nav>
</div></header>
<main class="wrap">
{body}
</main>
<footer class="site-footer"><div class="wrap">
<span>&copy; 2026 {SITE_NAME}. Estimates only, not financial or tax advice.</span>
<nav><a href="about.html">About</a><a href="privacy.html">Privacy Policy</a></nav>
</div></footer>
{js}
</body>
</html>
"""
    (ROOT / filename).write_text(html)


def calc_schema(name, description, filename):
    return {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": name,
        "description": description,
        "url": f"{SITE_URL}/{filename}",
        "applicationCategory": "FinanceApplication",
        "operatingSystem": "Any",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
    }


# ---------------------------------------------------------------- Home
CARDS = [
    ("mortgage-calculator.html", "Mortgage Calculator", "Monthly payment with taxes, insurance, PMI and HOA, plus a full amortization schedule."),
    ("auto-loan-calculator.html", "Auto Loan Calculator", "Car payment after trade-in, down payment and sales tax, with total interest."),
    ("paycheck-calculator.html", "Paycheck Calculator", "Take-home pay after 2026 federal income tax, Social Security, Medicare and state tax."),
    ("401k-calculator.html", "401(k) Calculator", "Retirement balance with employer match, salary growth and 2026 contribution limits."),
    ("compound-interest-calculator.html", "Compound Interest Calculator", "How savings grow with monthly deposits and different compounding schedules."),
]
cards = "".join(
    f'<a class="calc-card" href="{h}"><strong>{t}</strong><span>{d}</span><em>Open calculator</em></a>' for h, t, d in CARDS
)
page(
    "index.html",
    "Free Financial Calculators for Mortgages, Paychecks and Retirement",
    "Free, fast calculators for mortgage payments, car loans, take-home pay, 401(k) growth and compound interest. No sign-up.",
    f"""
{ad("leaderboard")}
<p class="eyebrow">Updated for 2026 tax year</p>
<h1>Money math, done in seconds</h1>
<p class="lede">Free calculators for the decisions that matter most: buying a home, financing a car, understanding your paycheck and planning for retirement. Results update as you type, and nothing you enter leaves your browser.</p>
<div class="calc-grid">{cards}</div>
{ad("inline")}
<section class="prose">
<h2>Why use these calculators</h2>
<p>Each tool uses the current IRS figures and standard loan formulas, shows every assumption, and breaks the result down so you can see where the money goes. They work on any phone or computer with no account and no tracking of your numbers.</p>
</section>
""",
)

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
{field("taxRate", "Property tax", "1.1", post="%/yr", hint="US median about 1%")}
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
    scripts=("mortgage.js",),
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
{field("taxRate", "Sales tax", "6.5", post="%")}
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
    scripts=("auto.js",),
    schema=calc_schema("Auto Loan Calculator", desc, "auto-loan-calculator.html"),
)

# ---------------------------------------------------------------- Paycheck
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
{field("stateRate", "State tax rate", "0", post="%", hint="Filled in from your state; edit if you know your rate", full=True)}
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
<p><strong>State income tax</strong> varies. Nine states have no wage income tax: Alaska, Florida, Nevada, New Hampshire, South Dakota, Tennessee, Texas, Washington and Wyoming. Flat-tax states use their single rate. For states with graduated brackets this version uses an approximate effective rate that you can override. Local and city taxes are not included.</p>
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

# ---------------------------------------------------------------- About / Privacy (required for AdSense review)
page(
    "about.html",
    f"About {SITE_NAME}",
    "Who builds these calculators and how the numbers are sourced.",
    f"""<section class="prose"><h1>About</h1>
<p>{SITE_NAME} builds free, fast and private financial calculators for everyday decisions. Every calculation runs in your browser, so the numbers you type are never sent to a server.</p>
<p>Tax figures come from IRS and Social Security Administration publications for the 2026 tax year. Results are estimates for planning and are not financial, tax or legal advice.</p>
<p>Questions or corrections: <strong>hello@example.com</strong></p></section>""",
)
page(
    "privacy.html",
    "Privacy Policy",
    f"Privacy policy for {SITE_NAME}.",
    f"""<section class="prose"><h1>Privacy Policy</h1>
<p>Last updated: October 2026.</p>
<p>The numbers you enter in our calculators stay in your browser and are not collected or stored by us.</p>
<h2>Advertising</h2>
<p>We use Google AdSense to show ads. Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visits to this site and other sites on the internet. You may opt out of personalized advertising by visiting <a href="https://www.google.com/settings/ads" rel="nofollow">Google Ads Settings</a> or <a href="https://www.aboutads.info/choices/" rel="nofollow">aboutads.info</a>.</p>
<h2>Analytics</h2>
<p>We may use privacy-friendly analytics to count page views. These do not identify you personally.</p>
<h2>California residents</h2>
<p>Under the CCPA you may request access to or deletion of personal information. Because our calculators do not collect personal data, we generally hold none about you. Contact <strong>hello@example.com</strong> with any request.</p>
</section>""",
)

print("Built", len(list(ROOT.glob("*.html"))), "pages")
