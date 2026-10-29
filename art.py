"""Small illustrations for each calculator, shown on the home cards and beside each page title.

Inline SVG coloured through CSS classes (see .art in style.css), so they follow light and dark themes.
"""

BG = '<circle class="bg" cx="60" cy="50" r="42"/>'

_ART = {
    "mortgage-calculator.html": """
<path class="wh ln" d="M32 52 L60 30 L88 52 V80 H32 Z"/>
<path class="ln" d="M76 38 V26 H84 V45"/>
<path class="ln" d="M24 58 L60 28 L96 58"/>
<rect class="fl" x="53" y="62" width="14" height="18" rx="2"/>
<rect class="ln" x="38" y="58" width="10" height="10" rx="1"/>
<rect class="ln" x="72" y="58" width="10" height="10" rx="1"/>""",
    "home-affordability-calculator.html": """
<path class="wh ln" d="M26 54 L52 34 L78 54 V80 H26 Z"/>
<path class="ln" d="M20 59 L52 32 L84 59"/>
<rect class="fl" x="45" y="62" width="14" height="18" rx="2"/>
<circle class="fl" cx="88" cy="72" r="13"/>
<path class="wl" d="M82 72 L86.5 76.5 L94 68"/>""",
    "auto-loan-calculator.html": """
<path class="wh ln" d="M20 66 V56 L32 52 L44 38 H76 L88 52 L100 56 V66 Z"/>
<path class="ln" d="M48 43 L42 51 H58 V43 Z M64 43 V51 H82 L76 43 Z"/>
<circle class="fl" cx="40" cy="67" r="9"/><circle class="wh" cx="40" cy="67" r="3.5"/>
<circle class="fl" cx="80" cy="67" r="9"/><circle class="wh" cx="80" cy="67" r="3.5"/>""",
    "personal-loan-calculator.html": """
<rect class="wh ln" x="22" y="34" width="58" height="32" rx="4" transform="rotate(-10 51 50)"/>
<rect class="wh ln" x="32" y="44" width="58" height="32" rx="4"/>
<circle class="ln" cx="61" cy="60" r="8"/>
<path class="ln" d="M40 52 H44 M78 68 H82"/>
<circle class="fl" cx="94" cy="76" r="11"/><circle class="wl" cx="94" cy="76" r="5"/>""",
    "credit-card-payoff-calculator.html": """
<rect class="wh ln" x="22" y="28" width="72" height="46" rx="6"/>
<rect class="fl" x="22" y="38" width="72" height="8"/>
<rect class="fl" x="30" y="54" width="12" height="9" rx="2"/>
<path class="ln" d="M50 66 H62 M68 66 H80"/>
<circle class="fl" cx="92" cy="74" r="13"/>
<path class="wl" d="M92 67 V81 M86 75.5 L92 81.5 L98 75.5"/>""",
    "debt-to-income-calculator.html": """
<path class="soft" d="M26 72 A34 34 0 0 1 94 72"/>
<path class="arc" d="M26 72 A34 34 0 0 1 60 38"/>
<path class="ln" d="M60 72 L80 50"/>
<circle class="fl" cx="60" cy="72" r="6"/>
<path class="ln" d="M22 80 H98"/>""",
    "paycheck-calculator.html": """
<rect class="wh ln" x="34" y="18" width="52" height="66" rx="4"/>
<path class="ln" d="M44 32 H76 M44 42 H68 M44 52 H76"/>
<rect class="fl" x="44" y="63" width="32" height="11" rx="2"/>""",
    "salary-to-hourly-calculator.html": """
<circle class="wh ln" cx="54" cy="50" r="27"/>
<path class="ln" d="M54 34 V50 L65 57"/>
<path class="ln" d="M54 26 V28 M54 72 V74 M30 50 H32 M76 50 H78"/>
<circle class="fl" cx="88" cy="74" r="13"/><circle class="wl" cx="88" cy="74" r="6"/>""",
    "401k-calculator.html": """
<ellipse class="wh ln" cx="56" cy="58" rx="30" ry="21"/>
<path class="wh ln" d="M40 42 L44 31 L53 39"/>
<rect class="wh ln" x="83" y="52" width="9" height="12" rx="3"/>
<path class="ln" d="M42 78 V85 M68 78 V85 M50 40 H62"/>
<circle class="fl" cx="73" cy="52" r="2.6"/>
<circle class="fl" cx="56" cy="20" r="9"/><circle class="wl" cx="56" cy="20" r="4"/>""",
    "compound-interest-calculator.html": """
<rect class="fl" x="28" y="64" width="12" height="16" rx="2"/>
<rect class="fl" x="46" y="54" width="12" height="26" rx="2"/>
<rect class="fl" x="64" y="42" width="12" height="38" rx="2"/>
<rect class="fl" x="82" y="28" width="12" height="52" rx="2"/>
<path class="ln" d="M22 58 Q56 54 86 18"/>
<path class="ln" d="M77 17 H87 V27"/>
<path class="ln" d="M20 80 H100"/>""",
    "savings-goal-calculator.html": """
<circle class="wh ln" cx="56" cy="54" r="28"/>
<circle class="ln" cx="56" cy="54" r="17"/>
<circle class="fl" cx="56" cy="54" r="7"/>
<path class="ln" d="M56 54 L90 22"/>
<path class="ln" d="M82 20 L91 21 L92 30"/>""",
    "bmi-calculator.html": """
<rect class="wh ln" x="28" y="34" width="64" height="46" rx="8"/>
<path class="soft" d="M40 60 A20 20 0 0 1 80 60"/>
<path class="arc" d="M40 60 A20 20 0 0 1 60 40"/>
<path class="ln" d="M60 60 L70 47"/>
<circle class="fl" cx="60" cy="60" r="4"/>
<path class="ln" d="M40 72 H80"/>""",
    "calorie-calculator.html": """
<circle class="wh ln" cx="56" cy="54" r="26"/>
<circle class="ln" cx="56" cy="54" r="16"/>
<path class="ln" d="M20 30 V46 M16 30 V40 Q16 46 20 46 Q24 46 24 40 V30 M20 46 V80"/>
<path class="ln" d="M94 30 Q102 40 94 52 V80"/>
<circle class="fl" cx="90" cy="76" r="11"/>
<path class="wl" d="M90 70 Q86 75 88 79 Q90 82 92 79 Q94 75 90 70 Z"/>""",
    "due-date-calculator.html": """
<rect class="wh ln" x="26" y="28" width="62" height="54" rx="6"/>
<rect class="fl" x="26" y="28" width="62" height="12" rx="6"/>
<path class="ln" d="M40 22 V32 M74 22 V32"/>
<path class="ln" d="M36 52 H44 M52 52 H60 M68 52 H76 M36 66 H44 M52 66 H60"/>
<circle class="fl" cx="90" cy="74" r="13"/>
<path class="wl" d="M90 81 L84 75 Q81 70 85.5 68 Q88.5 67 90 71 Q91.5 67 94.5 68 Q99 70 96 75 Z"/>""",
    "percentage-calculator.html": """
<circle class="wh ln" cx="58" cy="50" r="30"/>
<circle class="ln" cx="46" cy="38" r="7"/>
<circle class="ln" cx="70" cy="62" r="7"/>
<path class="ln" d="M74 32 L42 68"/>
<circle class="fl" cx="92" cy="76" r="11"/>""",
    "tip-calculator.html": """
<path class="wh ln" d="M34 20 H82 V82 L76 77 L70 82 L64 77 L58 82 L52 77 L46 82 L40 77 L34 82 Z"/>
<path class="ln" d="M44 34 H72 M44 44 H64 M44 54 H72"/>
<circle class="fl" cx="88" cy="70" r="14"/>
<path class="wl" d="M92 64 Q88 61 85 63.5 Q83 66.5 88 68.5 Q93 70.5 91 74.5 Q88 77 84 74 M88 59 V61 M88 77 V79"/>""",
    "age-calculator.html": """
<rect class="wh ln" x="30" y="50" width="56" height="30" rx="4"/>
<path class="ln" d="M30 62 Q37 68 44 62 Q51 56 58 62 Q65 68 72 62 Q79 56 86 62"/>
<path class="ln" d="M44 50 V38 M58 50 V38 M72 50 V38"/>
<path class="fl" d="M44 28 Q48 33 44 35 Q40 33 44 28 Z M58 28 Q62 33 58 35 Q54 33 58 28 Z M72 28 Q76 33 72 35 Q68 33 72 28 Z"/>
<path class="ln" d="M22 84 H98"/>""",
    "gpa-calculator.html": """
<path class="wh ln" d="M20 44 L60 28 L100 44 L60 60 Z"/>
<path class="ln" d="M36 51 V66 Q60 78 84 66 V51"/>
<path class="ln" d="M100 44 V62"/>
<circle class="fl" cx="100" cy="66" r="4"/>""",
}

ART = {k: f'<svg class="art" viewBox="0 0 120 96" aria-hidden="true">{BG}{v}</svg>' for k, v in _ART.items()}
