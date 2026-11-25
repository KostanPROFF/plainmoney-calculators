"""Standalone articles. They are English only: build.py keeps them out of the translation pipeline."""

ARTICLES = {
    "how-to-choose-a-mortgage-calculator.html": {
        "title": "How to Choose an Online Mortgage Calculator",
        "description": "What a good mortgage calculator should include, how simple and advanced tools differ, and the mistakes that make a payment estimate too low.",
        "related": "mortgage-calculator.html",
        "published": "2026-11-19",
        "body": """<article class="prose">
<h1>How to choose an online mortgage calculator</h1>
<p class="lede">Most mortgage calculators give you a number in seconds. The question is whether that number is close to what you will actually pay each month.</p>

<p>A mortgage calculator is only as useful as what it counts. A tool that shows principal and interest alone can leave out several hundred dollars a month in property tax, insurance and mortgage insurance. This guide covers what to look for, how simple and advanced calculators differ, what to have ready before you start, and the mistakes that make estimates come out too low.</p>

<h2>What a mortgage calculator does</h2>
<p>At its simplest, you enter a home price, a down payment, an interest rate and a loan term, and the calculator returns a monthly payment. That payment comes from the standard amortization formula, which spreads the loan and its interest into equal monthly installments.</p>
<p>More detailed calculators add the costs most lenders collect with the payment: property tax, homeowners insurance, private mortgage insurance (PMI) when you put down less than 20%, and HOA dues. Some also show how each payment splits between principal and interest over the life of the loan, or let you pick a loan type and enter a credit score.</p>

<h2>Simple and advanced calculators</h2>
<p>A simple calculator is fine for a first look, when you only want to know whether a price range is realistic. Once you are comparing homes or talking to lenders, you need one that shows the full monthly cost.</p>
<div class="table-scroll"><table>
<thead><tr><th>Feature</th><th>Simple calculator</th><th>Advanced calculator</th></tr></thead>
<tbody>
<tr><td>Home price and down payment</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Loan term and loan type</td><td>Term only, or fixed</td><td>Yes</td></tr>
<tr><td>Property tax and insurance</td><td>No</td><td>Yes</td></tr>
<tr><td>PMI and HOA dues</td><td>No</td><td>Yes</td></tr>
<tr><td>Credit score</td><td>No</td><td>Sometimes</td></tr>
<tr><td>Result</td><td>Monthly principal and interest</td><td>Full monthly payment with a breakdown and schedule</td></tr>
</tbody></table></div>

<h2>What to look for</h2>
<h3>The full monthly payment</h3>
<p>This matters more than anything else on the list. Property tax, homeowners insurance and PMI are part of what leaves your bank account each month, so a calculator that skips them understates your payment. Check that each cost has its own field and that the result shows how much each one adds.</p>
<h3>Inputs you can change</h3>
<p>You should be able to edit every number: the price, the down payment, the rate, the term and the yearly costs. Default values are a starting point, not your situation. A good calculator also updates as you type, so you can see how a bigger down payment or a shorter term changes the result without starting over.</p>
<h3>A breakdown over time</h3>
<p>An amortization schedule shows how much of each year's payments goes to interest and how much to the loan balance, and how much interest you pay in total. It is the clearest way to compare a 15-year loan with a 30-year one, or to see when PMI would drop off.</p>
<h3>Affordability, not just payment</h3>
<p>A payment calculator tells you what a given house costs per month. An affordability calculator works the other way, starting from your income and debts and estimating the price you can carry. Lenders look at your debt-to-income ratio, so it helps to check both.</p>
<h3>Easy to use on any device</h3>
<p>Labels should be clear, fields should explain what they want (yearly or monthly, percent or dollars), and the page should work on a phone as well as a laptop. You will probably run numbers while looking at listings, often away from a desk.</p>
<h3>No sign-up</h3>
<p>You should not have to give an email address or phone number to see a payment estimate. If a calculator asks for contact details before showing a result, it is usually collecting leads for lenders.</p>

<h2>Get your numbers ready first</h2>
<p>An estimate is only as good as what you type in. Before you start, gather your gross monthly income, your monthly debt payments (car loans, student loans, credit card minimums), the cash you can put down, and an interest rate. A rate quote from a lender is better than a national average, because your credit score and loan type change the rate you are offered. If you know the property tax rate for the area or have an insurance quote, use those too.</p>
<p>Think about what you want from the loan as well. A shorter term means higher payments and much less total interest. A longer term keeps the monthly amount lower. Running both is the fastest way to see the tradeoff.</p>

<h2>A worked example</h2>
<p>Take a $425,000 home in Texas with a 30-year fixed rate of 6.5%, property tax of 1.58% a year and $1,800 a year for insurance.</p>
<p>With 20% down, the loan is $340,000. Principal and interest come to about $2,149 a month. Add $560 for property tax and $150 for insurance, and the full payment is about $2,859. A calculator that shows only principal and interest would put it about $710 too low.</p>
<p>With 10% down, the loan is $382,500 and principal and interest rise to about $2,418. PMI at 0.5% a year adds about $159, so the full payment is about $3,287, roughly $428 more than with 20% down. If the rate is 7% instead of 6.5%, principal and interest go up by another $127 or so.</p>
<p>These figures come from the <a href="mortgage-calculator.html">mortgage calculator</a> on this site, which you can use to run the same numbers with your own price, rate and costs.</p>

<h2>Common mistakes</h2>
<h3>Counting only principal and interest</h3>
<p>As the example shows, leaving out tax, insurance and PMI can understate the payment by hundreds of dollars. Use a calculator that includes them, and replace the defaults with local figures when you have them.</p>
<h3>Using an old rate</h3>
<p>Mortgage rates move, and so does your own situation. An estimate from three months ago may no longer be right. Run the numbers again when rates change, when you get a new quote, or when your income or debts change.</p>
<h3>Forgetting when PMI ends</h3>
<p>On a conventional loan, PMI usually comes off once you reach 20% equity. A calculator that keeps charging it for the whole loan overstates your total cost, and one that ignores it understates the first years.</p>
<h3>Treating the estimate as an offer</h3>
<p>A calculator gives a planning number. Your lender's Loan Estimate is the document that shows the actual rate, fees and payment, so use the calculator to prepare and compare, then check the figures against what lenders send you.</p>

<h2>Tools that go with a mortgage calculator</h2>
<p>A <a href="home-affordability-calculator.html">home affordability calculator</a> starts from your income and debts and estimates the price range you can afford. A <a href="debt-to-income-calculator.html">debt-to-income calculator</a> shows the ratio lenders check before approving a loan. If you already own a home, a refinance calculator compares your current loan with a new one, and the better ones let you include closing costs so you can see how long it takes to break even.</p>

<h2>After you choose</h2>
<p>Start with your real numbers and save a baseline result. Then change one thing at a time: the down payment, the term, the rate, the price. Watching each change on its own shows which choices matter most for your budget. When you are ready to talk to lenders, you will know what monthly payment you are comfortable with and can compare their offers against it.</p>

<h2>Frequently asked questions</h2>
<div class="faq">
{faq}
</div>
<p class="note">Last reviewed: November 2026. This guide is general information, not financial advice.</p>
</article>""",
        "faq": [
            ("What should a good mortgage calculator include?",
             "At a minimum: home price, down payment, interest rate and loan term, plus fields for property tax, homeowners insurance, PMI and HOA dues. A breakdown of the payment and an amortization schedule make the result much easier to understand."),
            ("What is the difference between a simple and an advanced mortgage calculator?",
             "A simple calculator returns principal and interest from the price, down payment, rate and term. An advanced one adds taxes, insurance, PMI and HOA dues, and may let you choose a loan type or enter a credit score, so it shows the full monthly payment."),
            ("Why does my lender's payment differ from the calculator?",
             "Lenders use your actual rate, which depends on your credit score and loan type, plus local tax and insurance figures and their own fees. A calculator is only as close as the numbers you enter, so use a rate quote and local costs when you can."),
            ("What is the most common mistake people make with mortgage calculators?",
             "Looking only at principal and interest. Property tax, homeowners insurance and PMI can add several hundred dollars a month, so an estimate without them comes out too low."),
            ("When should I start using a mortgage calculator?",
             "Before you start looking at homes. Knowing the payment for different prices and down payments early helps you set a budget, decide how much to save, and compare lender offers when they arrive."),
        ],
    },
    "how-much-house-can-i-afford-on-my-salary.html": {
        "title": "How Much House Can I Afford on My Salary? A 2026 Table",
        "description": "The home price lenders' 28/36 rule allows at salaries from $40,000 to $200,000, and how debts, rates and the down payment move that number.",
        "related": "home-affordability-calculator.html",
        "published": "2026-11-24",
        "body": """<article class="prose">
<h1>How much house can I afford on my salary?</h1>
<p class="lede">Lenders do not look at the price of the house first. They look at how much of your income the monthly payment would take, and work backward from there.</p>

<p>The rule most lenders start with is called 28/36. Your housing payment, meaning principal, interest, property tax, insurance and mortgage insurance, should stay under 28% of your gross monthly income. All of your debt payments together, housing included, should stay under 36%. Whichever limit is lower decides how big a payment you qualify for, and the payment decides the price.</p>
<p>We ran that rule through our <a href="home-affordability-calculator.html">home affordability calculator</a> for a range of salaries. The table below is the result, followed by what changes it the most.</p>

<h2>The assumptions behind the table</h2>
<p>Every figure below uses the same starting point, so you can compare rows. It is a 30-year fixed loan at 6.5%, 10% down, property tax of 1.1% of the price a year, homeowners insurance of $1,800 a year and private mortgage insurance at 0.5% of the loan a year. We also assumed $400 a month of other debt, roughly a car payment or a student loan, because few buyers have none.</p>

<h2>Home price by salary</h2>
<div class="table-scroll"><table>
<thead><tr><th>Gross salary</th><th>Max housing payment</th><th>Home price</th><th>Which limit applies</th></tr></thead>
<tbody>
<tr><td>$40,000</td><td>$800</td><td>$93,000</td><td>36% (total debt)</td></tr>
<tr><td>$50,000</td><td>$1,100</td><td>$136,000</td><td>36% (total debt)</td></tr>
<tr><td>$60,000</td><td>$1,400</td><td>$179,000</td><td>36% (total debt)</td></tr>
<tr><td>$75,000</td><td>$1,750</td><td>$229,000</td><td>28% (housing)</td></tr>
<tr><td>$90,000</td><td>$2,100</td><td>$279,000</td><td>28% (housing)</td></tr>
<tr><td>$100,000</td><td>$2,333</td><td>$313,000</td><td>28% (housing)</td></tr>
<tr><td>$125,000</td><td>$2,917</td><td>$396,000</td><td>28% (housing)</td></tr>
<tr><td>$150,000</td><td>$3,500</td><td>$480,000</td><td>28% (housing)</td></tr>
<tr><td>$175,000</td><td>$4,083</td><td>$563,000</td><td>28% (housing)</td></tr>
<tr><td>$200,000</td><td>$4,667</td><td>$647,000</td><td>28% (housing)</td></tr>
</tbody></table></div>
<p>A rough shortcut falls out of the table: with these rates and costs, the price works out to a little over three times salary once income passes about $75,000. Below that, the $400 of other debt eats a bigger share of income, and the 36% limit pulls the price down faster. At $40,000 a year, that one car payment takes 12% of gross income before housing is counted at all.</p>

<h2>Debts cut the price faster than most people expect</h2>
<p>Here is the same calculation at an $80,000 salary, changing only the monthly debt payments.</p>
<div class="table-scroll"><table>
<thead><tr><th>Other monthly debts</th><th>Home price</th></tr></thead>
<tbody>
<tr><td>$0</td><td>$246,000</td></tr>
<tr><td>$300</td><td>$246,000</td></tr>
<tr><td>$600</td><td>$236,000</td></tr>
<tr><td>$900</td><td>$193,000</td></tr>
<tr><td>$1,200</td><td>$150,000</td></tr>
</tbody></table></div>
<p>Up to about $530 a month, debts make no difference, because the 28% housing limit is the tighter one. Past that point every extra $100 of monthly payments removes about $14,000 from the price you qualify for. Paying off a $350 car loan before applying can be worth more than saving another $10,000 for the down payment.</p>

<h2>What a rate change does</h2>
<p>At a $100,000 salary with the same debts and down payment:</p>
<div class="table-scroll"><table>
<thead><tr><th>Interest rate</th><th>Home price</th></tr></thead>
<tbody>
<tr><td>5.5%</td><td>$341,000</td></tr>
<tr><td>6.0%</td><td>$326,000</td></tr>
<tr><td>6.5%</td><td>$313,000</td></tr>
<tr><td>7.0%</td><td>$300,000</td></tr>
<tr><td>7.5%</td><td>$288,000</td></tr>
</tbody></table></div>
<p>Each full point of interest moves the price by roughly $26,000, about 8%. A better credit score, a rate quote from more than one lender and, sometimes, paying for discount points all show up here.</p>

<h2>What the down payment changes</h2>
<p>Still at $100,000 a year:</p>
<div class="table-scroll"><table>
<thead><tr><th>Down payment</th><th>Home price</th><th>Cash needed for the down payment</th></tr></thead>
<tbody>
<tr><td>3.5%</td><td>$294,000</td><td>$10,300</td></tr>
<tr><td>5%</td><td>$298,000</td><td>$14,900</td></tr>
<tr><td>10%</td><td>$313,000</td><td>$31,300</td></tr>
<tr><td>20%</td><td>$366,000</td><td>$73,100</td></tr>
</tbody></table></div>
<p>Going from 3.5% to 10% down only adds about $19,000 to the price, because the payment limit stays the same. The jump at 20% is bigger because mortgage insurance disappears, which frees up about $120 a month for principal and interest. Remember that closing costs, usually 2% to 5% of the loan, come on top of the down payment. FHA loans, the usual route for 3.5% down, also charge an upfront mortgage insurance premium of 1.75% of the loan, which is normally added to the balance.</p>

<h2>When the 28/36 rule is too strict, or not strict enough</h2>
<p>Many lenders approve higher ratios. Conventional loans often go to a 45% total debt ratio and FHA loans can go higher with strong credit or savings, which is why the calculator also offers a 31/43 option. Approval is a ceiling, though, not advice. The 28/36 rule leaves room for things a lender does not count: childcare, retirement saving, commuting and the 1% to 2% of the home's value a year that maintenance tends to cost.</p>
<p>Property tax matters as much as the rate in some places. The table uses 1.1%, close to the national average. In New Jersey or Illinois, where effective rates run above 2%, the same salary buys noticeably less. In Hawaii or Alabama, where they are well under 1%, it buys more. The calculator fills in your state's average when you pick it.</p>

<h2>Run it for yourself</h2>
<p>The figures here are a starting point. Put in your own income, debts, savings and a real rate quote in the <a href="home-affordability-calculator.html">home affordability calculator</a>, then check the payment on a specific listing with the <a href="mortgage-calculator.html">mortgage calculator</a>. If debts are what holds you back, the <a href="debt-to-income-calculator.html">debt-to-income calculator</a> shows how much each one counts.</p>

<h2>Frequently asked questions</h2>
<div class="faq">
{faq}
</div>
<p class="note">Last reviewed: November 2026. Figures are estimates for planning, not a loan offer or financial advice.</p>
</article>""",
        "faq": [
            ("How much house can I afford on a $100,000 salary?",
             "About $313,000 with 10% down, a 6.5% rate, average property tax and insurance and $400 a month of other debt. That keeps the full housing payment near $2,333, or 28% of gross income. Less debt or a lower rate raises the figure; higher local taxes lower it."),
            ("What is the 28/36 rule?",
             "A lending guideline that keeps housing costs under 28% of gross monthly income and all debt payments, housing included, under 36%. The lower of the two limits sets the largest payment, and so the largest price, a lender is comfortable with."),
            ("Does the 28/36 rule use gross or take-home pay?",
             "Gross pay, before taxes and deductions. That is why the payment it allows can feel tight on a take-home budget, especially with high state taxes or large 401(k) contributions."),
            ("Is it better to pay off debt or save a bigger down payment?",
             "If your debts are above the point where the 36% limit applies, paying them off usually raises the price you qualify for more than the same money added to the down payment. Below that point, extra down payment helps more, especially if it gets you to 20% and removes mortgage insurance."),
            ("Why is the price so low at $40,000 to $60,000 a year?",
             "At lower incomes a fixed debt like a $400 car payment takes a larger share of income, so the 36% total debt limit is reached before the 28% housing limit. Property tax and insurance also take a fixed bite out of a smaller payment."),
        ],
    },
    "how-long-to-pay-off-credit-card-debt.html": {
        "title": "How Long Does It Take to Pay Off Credit Card Debt?",
        "description": "Payoff times and total interest for $2,000 to $20,000 of card debt at 22% APR, paying the minimum or a fixed amount, plus what a balance transfer saves.",
        "related": "credit-card-payoff-calculator.html",
        "published": "2026-11-24",
        "body": """<article class="prose">
<h1>How long does it take to pay off credit card debt?</h1>
<p class="lede">Paying only the minimum keeps a card in good standing, but it is designed to take a very long time. A fixed monthly amount changes the picture completely.</p>

<p>Your statement already shows one version of this answer, in the box that says how long payoff takes at the minimum. What it does not show is how fast the number drops when you pay a little more. We ran the same balances through our <a href="credit-card-payoff-calculator.html">credit card payoff calculator</a> at several payment levels to show both.</p>

<h2>The assumptions</h2>
<p>All examples use a 22% APR, close to the average the Federal Reserve reports for card accounts that are charged interest. The minimum payment follows a formula many large issuers use: 1% of the balance plus that month's interest, with a floor of $25. Your card's formula may differ, so check the minimum payment section of your cardholder agreement. We also assume no new purchases go on the card while you pay it down.</p>

<h2>Payoff time and interest by balance</h2>
<div class="table-scroll"><table>
<thead><tr><th>Balance</th><th>Minimum payment only</th><th>$200 a month</th><th>$300 a month</th><th>$500 a month</th></tr></thead>
<tbody>
<tr><td>$2,000</td><td>11 yr 7 mo, $2,600 interest</td><td>12 mo, $230</td><td>8 mo, $153</td><td>5 mo, $97</td></tr>
<tr><td>$5,000</td><td>19 yr 2 mo, $8,100</td><td>2 yr 10 mo, $1,750</td><td>1 yr 9 mo, $1,022</td><td>1 yr, $574</td></tr>
<tr><td>$10,000</td><td>24 yr 11 mo, $17,266</td><td>11 yr 5 mo, $17,356</td><td>4 yr 4 mo, $5,596</td><td>2 yr 2 mo, $2,571</td></tr>
<tr><td>$20,000</td><td>30 yr 8 mo, $35,600</td><td>Never</td><td>Never</td><td>6 yr 1 mo, $16,378</td></tr>
</tbody></table></div>
<p>Two things stand out. At the minimum, the interest on a $5,000 balance ends up larger than the balance itself. And on a $20,000 balance, $200 or $300 a month never pays it off, because the interest alone is about $367 a month at 22%. Any payment below the monthly interest lets the balance grow.</p>

<h2>Why the minimum takes so long</h2>
<p>The minimum is a percentage of what you owe, so it shrinks as the balance shrinks. On $5,000 the first minimum is about $142. A year later it is about $127, and three years in it is about $100, with almost two thirds of that still going to interest. The payment keeps stepping down, so the balance never falls as fast as it did in the first month.</p>
<p>The simplest fix is to keep paying that first minimum as a fixed amount. Paying $142 every month on the same $5,000 clears it in 4 years and 10 months with about $3,100 of interest, instead of 19 years and $8,100. On $10,000, a fixed $283 does it in the same 4 years and 10 months for about $6,300 of interest. You do not need a bigger budget, only a payment that stops shrinking.</p>

<h2>How much the APR matters</h2>
<p>For a $5,000 balance paid at $200 a month:</p>
<div class="table-scroll"><table>
<thead><tr><th>APR</th><th>Time to pay off</th><th>Total interest</th></tr></thead>
<tbody>
<tr><td>0%</td><td>2 yr 1 mo</td><td>$0</td></tr>
<tr><td>15%</td><td>2 yr 7 mo</td><td>$1,033</td></tr>
<tr><td>20%</td><td>2 yr 9 mo</td><td>$1,522</td></tr>
<tr><td>25%</td><td>3 yr</td><td>$2,137</td></tr>
<tr><td>29.99%</td><td>3 yr 4 mo</td><td>$2,943</td></tr>
</tbody></table></div>
<p>It is worth calling your issuer and asking for a lower rate, particularly if you have paid on time for a year or more. A few points off the APR saves a few hundred dollars here, more on a larger balance.</p>

<h2>Does a balance transfer help?</h2>
<p>A balance transfer card moves the debt to a 0% introductory rate for a set period, usually 12 to 21 months, in exchange for a fee, usually 3% to 5% of the amount moved. Take the same $5,000 with a 3% fee ($150) and an 18-month 0% period, still paying $200 a month. After 18 months, $1,550 is left. If the rate then goes to 22%, the rest is gone nine months later with about $138 of interest. Total cost: roughly $290, against $1,750 on the original card, and seven months sooner.</p>
<p>The catch is discipline. It only works if the old card does not fill up again, and if you plan to finish, or nearly finish, before the intro period ends. Check whether the transfer fee and the rate after the intro period make the numbers work for your balance before you apply.</p>

<h2>Which card to pay first</h2>
<p>If you carry balances on several cards, pay the minimum on all of them and put every extra dollar on one. Paying the highest APR first, often called the avalanche method, costs the least interest. Paying the smallest balance first, the snowball method, clears whole accounts sooner, which some people find easier to stick with. The difference in interest is often smaller than the difference between sticking with a plan and dropping it, so pick the one you will keep doing.</p>

<h2>Run your own numbers</h2>
<p>Enter your balance, APR and payment in the <a href="credit-card-payoff-calculator.html">credit card payoff calculator</a>. It shows the payoff date, the total interest, the payment needed to be debt-free by a date you choose, and how much a bigger payment saves. If you are thinking about consolidating with a loan instead, compare the cost in the <a href="personal-loan-calculator.html">personal loan calculator</a>, including any origination fee.</p>

<h2>Frequently asked questions</h2>
<div class="faq">
{faq}
</div>
<p class="note">Last reviewed: November 2026. Figures are estimates for planning, not financial advice.</p>
</article>""",
        "faq": [
            ("How long does it take to pay off $5,000 on a credit card?",
             "At 22% APR, about 19 years with only the minimum payment, about 2 years and 10 months at $200 a month and about a year at $500 a month. Interest ranges from about $8,100 at the minimum to under $600 at $500 a month."),
            ("Why does my balance barely go down when I pay the minimum?",
             "Most of a minimum payment covers that month's interest. On a 22% card, interest is about 1.8% of the balance each month, and a common minimum is only 1% of the balance on top of that, so principal falls slowly."),
            ("What happens if my payment is less than the interest?",
             "The unpaid interest is added to the balance, so you owe more each month even though you are paying. On $20,000 at 22%, any payment below about $367 a month never pays the card off."),
            ("Is a balance transfer worth the fee?",
             "Usually, if you can pay most of the balance during the 0% period. On $5,000 paid at $200 a month, a 3% fee and 18 months at 0% cost about $290 in total, against about $1,750 of interest on a 22% card."),
            ("Should I pay off the highest interest or the smallest balance first?",
             "The highest interest rate first saves the most money. The smallest balance first closes accounts sooner and can be easier to keep going. Either works if you keep paying the extra amount every month."),
        ],
    },
    "how-long-should-a-car-loan-be.html": {
        "title": "How Long Should a Car Loan Be? 36 to 84 Months Compared",
        "description": "Monthly payment, total interest and how long you owe more than the car is worth on a $30,000 auto loan at 36, 48, 60, 72 and 84 months.",
        "related": "auto-loan-calculator.html",
        "published": "2026-11-24",
        "body": """<article class="prose">
<h1>How long should a car loan be?</h1>
<p class="lede">A longer loan makes the monthly payment smaller. It also makes the car cost more and keeps you owing more than it is worth for longer. The question is how much of each you are trading.</p>

<p>Dealers rarely start with the loan term. They start with the payment you want, then find a term that reaches it. That is why 72 and 84 month loans have become an ordinary part of buying a car. We ran one loan through the same formula our <a href="auto-loan-calculator.html">auto loan calculator</a> uses, at every common term, to show what the extra years actually cost.</p>

<h2>The assumptions</h2>
<p>Every example uses $30,000 borrowed at a 7% APR, with equal monthly payments and no prepayment penalty. That amount is meant to cover the car plus the sales tax and fees that are often rolled into the loan. Your own rate depends on your credit, the lender, whether the car is new or used and the term itself, so treat 7% as a round number for comparison, not a forecast.</p>

<h2>Payment and interest by loan term</h2>
<div class="table-scroll"><table>
<thead><tr><th>Term</th><th>Payment</th><th>Total interest</th><th>Owed after 3 years</th></tr></thead>
<tbody>
<tr><td>36 months</td><td>$926</td><td>$3,347</td><td>$0</td></tr>
<tr><td>48 months</td><td>$718</td><td>$4,483</td><td>$8,302</td></tr>
<tr><td>60 months</td><td>$594</td><td>$5,642</td><td>$13,268</td></tr>
<tr><td>72 months</td><td>$511</td><td>$6,826</td><td>$16,565</td></tr>
<tr><td>84 months</td><td>$453</td><td>$8,034</td><td>$18,908</td></tr>
</tbody></table></div>
<p>Going from 60 to 84 months lowers the payment by $141 a month and adds about $2,400 of interest. That is the visible cost. The last column shows a less visible one. Three years in, the 84-month borrower still owes almost $19,000, about $5,600 more than the 60-month borrower, on a car that is now three years old.</p>
<p>The payment savings also shrink as the term grows. Stretching from 36 to 48 months saves $208 a month. Stretching from 72 to 84 saves only $59, while still adding more than $1,200 of interest.</p>

<h2>Longer terms often come with higher rates</h2>
<p>The table above gives every term the same 7% rate, which flatters the long loans. Many lenders charge more for longer terms because the loan carries more risk for them. Here is what happens if the 72-month loan costs one point more and the 84-month loan two points more, a spread we picked for illustration.</p>
<div class="table-scroll"><table>
<thead><tr><th>Term and rate</th><th>Monthly payment</th><th>Total interest</th></tr></thead>
<tbody>
<tr><td>60 months at 7%</td><td>$594</td><td>$5,642</td></tr>
<tr><td>72 months at 8%</td><td>$526</td><td>$7,872</td></tr>
<tr><td>84 months at 9%</td><td>$483</td><td>$10,544</td></tr>
</tbody></table></div>
<p>With a higher rate the 84-month loan almost doubles the interest of the 60-month one, and the payment is only $111 lower. Ask each lender for a quote at two or three terms, not just the one you think you want, so you can see whether they price the terms differently.</p>
<p>The rate matters more on a long loan, too. At 5%, the 84-month version of this loan costs $5,617 in interest. At 12%, which borrowers with weaker credit can see, it costs $14,485, against $10,040 for 60 months at the same rate.</p>

<h2>How long you stay underwater</h2>
<p>Being underwater, or upside down, means you owe more on the loan than the car would sell for. It does not matter while you keep the car and keep paying. It matters a great deal if the car is totaled, stolen or needs to be sold early, because the insurance check or the sale price may not cover the loan. Any shortfall is still yours to pay, or it gets rolled into the next loan.</p>
<p>To see how term affects this, we assumed a car worth $28,000, with the other $2,000 of the loan being tax and fees and nothing put down. We then assumed it loses 20% of its value in the first year and 15% a year after that. Real depreciation varies a lot by model and mileage, so take these as an illustration, not a prediction for your car.</p>
<div class="table-scroll"><table>
<thead><tr><th>End of year</th><th>Car value</th><th>Owed, 60 months</th><th>Owed, 72 months</th><th>Owed, 84 months</th></tr></thead>
<tbody>
<tr><td>1</td><td>$22,400</td><td>$24,807</td><td>$25,830</td><td>$26,558</td></tr>
<tr><td>2</td><td>$19,040</td><td>$19,239</td><td>$21,359</td><td>$22,866</td></tr>
<tr><td>3</td><td>$16,184</td><td>$13,268</td><td>$16,565</td><td>$18,908</td></tr>
<tr><td>4</td><td>$13,756</td><td>$6,865</td><td>$11,424</td><td>$14,664</td></tr>
<tr><td>5</td><td>$11,693</td><td>$0</td><td>$5,911</td><td>$10,113</td></tr>
</tbody></table></div>
<p>Under these assumptions the 60-month loan climbs above water after about 2 years. The 72-month loan takes a little over 3 years and the 84-month loan almost 4 and a half. A 48-month loan, not shown in the table, gets there in about 15 months. A down payment of 10% to 20% shortens all of these, because you start with some equity instead of a gap.</p>
<p>If you do take a long loan with little down, GAP coverage pays the difference between the insurance payout and the loan balance after a total loss. Dealers often add it to the loan. Your own auto insurer or credit union may sell it for less, so compare before you sign.</p>

<h2>Turning the question around: what the payment buys</h2>
<p>Most people shop with a monthly budget in mind. Here is how much you could borrow for $550 a month at 7%, depending on the term.</p>
<div class="table-scroll"><table>
<thead><tr><th>Term</th><th>Amount you can borrow</th><th>Interest you pay</th></tr></thead>
<tbody>
<tr><td>36 months</td><td>$17,813</td><td>$1,987</td></tr>
<tr><td>48 months</td><td>$22,968</td><td>$3,432</td></tr>
<tr><td>60 months</td><td>$27,776</td><td>$5,224</td></tr>
<tr><td>72 months</td><td>$32,260</td><td>$7,340</td></tr>
<tr><td>84 months</td><td>$36,442</td><td>$9,758</td></tr>
</tbody></table></div>
<p>This is how a $550 payment ends up on a car that costs twice as much as the 36-month figure. The same payment for longer reaches a bigger loan, and a bigger loan on a longer term pays the most interest of all. Settling the price of the car first, and only then talking about financing, keeps the term from being used to make an expensive car look affordable. The Consumer Financial Protection Bureau makes a similar point in its auto loan guides: compare the total cost of the loan, not only the monthly payment.</p>

<h2>A middle path: a longer term, paid like a shorter one</h2>
<p>Some buyers take a longer term for the lower required payment, as a cushion in case money gets tight, and then pay more each month. On the 72-month loan above, paying $100 a month over the required $511 clears it in 58 months with $5,444 of interest, about $1,380 less than paying the minimum. That is close to what the 60-month loan costs.</p>
<p>This only works if you actually make the extra payments and the lender applies them to principal. Check that the loan has no prepayment penalty, and if the lender offers a lower rate for the shorter term, the shorter term is usually still the better deal.</p>

<h2>The new car loan interest deduction</h2>
<p>For tax years 2025 through 2028, federal law lets many buyers deduct interest on a loan for a new car, SUV, van, pickup or motorcycle whose final assembly took place in the United States. According to the IRS, the deduction is capped at $10,000 a year, phases out for modified adjusted gross income above $100,000 ($200,000 on a joint return), and is available whether or not you itemize. Used cars and leases do not qualify.</p>
<p>It helps, but it does not change the math much. In the first year of the 60-month loan above you would pay about $1,935 of interest. In the 22% tax bracket that deduction is worth roughly $426. Paying more interest to get a bigger deduction still leaves you paying more. Check the IRS rules for your vehicle and income before counting on it.</p>

<h2>So how long should it be?</h2>
<p>If the payment fits your budget at 48 or 60 months, that range usually balances the payment against interest and the time spent underwater. Going beyond 60 months makes sense mainly when the rate is low, you put a solid amount down and you plan to keep the car well past the end of the loan. If 84 months is the only way the payment works, the problem is usually the price of the car rather than the term.</p>
<p>Try your own numbers in the <a href="auto-loan-calculator.html">auto loan calculator</a>, which shows every term from 36 to 84 months side by side. To see how a car payment fits with your other debts, run it through the <a href="debt-to-income-calculator.html">debt-to-income calculator</a>, and if you are deciding between a car loan and saving up first, the <a href="savings-goal-calculator.html">savings goal calculator</a> shows how long that would take.</p>

<h2>Frequently asked questions</h2>
<div class="faq">
{faq}
</div>
<p class="note">Last reviewed: November 2026. Figures are estimates for planning, not a loan offer or financial advice.</p>
</article>""",
        "faq": [
            ("Is a 72-month car loan a bad idea?",
             "Not always, but it is expensive. On $30,000 at 7%, a 72-month loan costs about $1,180 more in interest than 60 months and keeps you owing more than a typical car is worth for about a year longer. It is more reasonable with a low rate, a solid down payment and a plan to keep the car for many years."),
            ("How much does an 84-month car loan cost compared with 60 months?",
             "At 7% on $30,000, the payment drops from $594 to $453, and interest rises from $5,642 to $8,034. If the lender charges 9% for 84 months, interest reaches $10,544."),
            ("What is the most common car loan length?",
             "Five and six year loans are common for new cars, and many lenders also offer seven years. A common term is not the same as a good one, so compare the total interest at two or three terms before choosing."),
            ("Can I pay off a car loan early?",
             "Most auto loans let you pay early without a penalty, but check your contract. Extra payments that go to principal cut the interest. Paying $100 a month extra on a $30,000, 72-month loan at 7% finishes it 14 months early and saves about $1,380."),
            ("How do I avoid being upside down on a car loan?",
             "Put at least 10% to 20% down, avoid rolling old loan balances into the new one, choose a shorter term and pick a car that holds its value. If you still start with a gap, GAP coverage protects you if the car is totaled."),
        ],
    },
}
