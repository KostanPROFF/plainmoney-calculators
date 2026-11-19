"""Standalone articles. They are English only: build.py keeps them out of the translation pipeline."""

ARTICLES = {
    "how-to-choose-a-mortgage-calculator.html": {
        "title": "How to Choose an Online Mortgage Calculator",
        "description": "What a good mortgage calculator should include, how simple and advanced tools differ, and the mistakes that make a payment estimate too low.",
        "related": "mortgage-calculator.html",
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
}
