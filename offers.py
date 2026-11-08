"""Partner offers shown under a calculator's result ("Compare rates").

Each calculator lists the offers that fit it. An offer appears only once its `url` is filled in with
the affiliate link from the partner network, so the block stays hidden until there is a real link.
`title`, `text` and `cta` are English; translated pages show an offer once these are translated."""

# Short ids used by OFFERS below; fill in url with the tracking link from the network.
PARTNERS = {
    "mortgage": {"url": "", "title": "Compare mortgage rates",
                 "text": "See rates from several lenders for your price and down payment. Checking rates does not affect your credit score.",
                 "cta": "Compare mortgage offers"},
    "refi": {"url": "", "title": "Check refinance rates",
             "text": "If rates have dropped since you bought, see what a refinance could save on your monthly payment.",
             "cta": "See refinance offers"},
    "auto": {"url": "", "title": "Get pre-approved for a car loan",
             "text": "A rate from a bank or credit union gives you a number to beat before you talk to the dealer.",
             "cta": "Compare auto loan rates"},
    "personal": {"url": "", "title": "Compare personal loan offers",
                 "text": "Prequalify with several lenders at once to see real rates. A soft check does not affect your credit score.",
                 "cta": "See personal loan rates"},
    "transfer": {"url": "", "title": "Look at balance transfer cards",
                 "text": "A 0% intro APR card can stop interest while you pay down the balance. Check the transfer fee first.",
                 "cta": "Compare balance transfer cards"},
    "savings": {"url": "", "title": "Find a high-yield savings account",
                "text": "Online banks often pay several times the national average rate, with FDIC insurance.",
                "cta": "Compare savings rates"},
}

OFFERS = {
    "mortgage-calculator.html": ["mortgage", "refi"],
    "home-affordability-calculator.html": ["mortgage"],
    "debt-to-income-calculator.html": ["mortgage", "personal"],
    "auto-loan-calculator.html": ["auto"],
    "personal-loan-calculator.html": ["personal"],
    "credit-card-payoff-calculator.html": ["transfer", "personal"],
    "savings-goal-calculator.html": ["savings"],
    "compound-interest-calculator.html": ["savings"],
}

DISCLOSURE = "We may earn a commission if you use these links. It does not change what you pay or how our calculators work."
