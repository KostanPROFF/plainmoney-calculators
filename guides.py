"""In-depth guides shown under each calculator, above the worked examples.

Each guide is English HTML. Translated pages show it only once a translation exists (see build.extras).
Example figures were computed with the same formulas the calculators use.
"""

GUIDES = {}

GUIDES["mortgage-calculator.html"] = """
<h2>How to use this mortgage calculator</h2>
<ol>
<li><strong>Home price and down payment.</strong> Enter the price you expect to pay and your down payment as a percent. The loan amount is the price minus the down payment.</li>
<li><strong>Interest rate and term.</strong> Use a rate from a recent quote if you have one. Otherwise start with the current average for a 30-year fixed loan and try a rate half a point higher and lower to see the range.</li>
<li><strong>State and property tax.</strong> Picking a state fills in its average effective property tax rate. Your county and city can be far higher or lower, so replace it with the rate from the home's listing or tax bill when you can.</li>
<li><strong>Insurance, HOA and PMI.</strong> Add a homeowners insurance quote, any HOA dues and a PMI rate. PMI is only charged while your down payment or equity is under 20%.</li>
</ol>
<p>The result shows your full monthly payment, how it splits between principal, interest, taxes, insurance, PMI and HOA, the total interest over the life of the loan and the year-by-year amortization schedule.</p>

<h2>How the interest rate changes your payment</h2>
<p>Small rate changes have a large effect on a 30-year loan. On a $350,000 loan, principal and interest come to:</p>
<div class="table-scroll"><table><thead><tr><th>Rate</th><th>Monthly principal and interest</th><th>Difference from 5.5%</th></tr></thead><tbody>
<tr><td>5.5%</td><td>$1,987</td><td>-</td></tr>
<tr><td>6.5%</td><td>$2,212</td><td>+$225</td></tr>
<tr><td>7.5%</td><td>$2,447</td><td>+$460</td></tr>
</tbody></table></div>
<p>Each percentage point adds roughly $230 a month, or more than $80,000 over 30 years. That is why it pays to compare at least three lenders on the same day, improve your credit score before applying and ask whether buying discount points makes sense for how long you plan to stay.</p>

<h2>What extra payments do</h2>
<p>Any amount you pay above the required payment goes straight to principal, so the next month's interest is charged on a smaller balance. On a $360,000 loan at 6.75% for 30 years, the regular payment is $2,335 and total interest is about $480,600. Adding $200 a month pays the loan off in about 23 years and 10 months and cuts interest to about $364,700, a saving of nearly $116,000. Before you prepay, check that your loan has no prepayment penalty and that you already have an emergency fund and are getting any 401(k) match.</p>

<h2>Costs this calculator does not include</h2>
<p>Closing costs are paid separately at closing. Lender fees, title insurance, the appraisal and recording fees usually come to 2% to 5% of the loan. Your first few payments can also run a little high, because lenders may collect up to two months of taxes and insurance in advance as an escrow cushion.</p>
<p>Repairs are the other cost owners tend to forget. Many budget 1% to 2% of the home's value a year for maintenance. It is not part of the mortgage payment, but it still comes out of the same budget. Finally, the calculator assumes a fixed rate; on an adjustable-rate loan the payment can rise after the initial period ends.</p>

<h2>Where mortgage estimates go wrong</h2>
<p>The most common error is comparing loans by monthly payment alone. A longer term always lowers the payment and always raises total interest, so look at both numbers. The second is using a national average for property tax: in states such as New Jersey or Illinois, the real bill can add several hundred dollars a month more than the average suggests. And PMI is easy to overweight. On a conventional loan it stops once you reach 20% to 22% equity, so it is a temporary cost, unlike the mortgage insurance on most FHA loans.</p>

<h2>Sources</h2>
<ul>
<li>Consumer Financial Protection Bureau, <a href="https://www.consumerfinance.gov/owning-a-home/" rel="nofollow">Buying a House</a> and the Loan Estimate explainer.</li>
<li>Homeowners Protection Act rules on PMI cancellation at 80% and automatic termination at 78% of the original value.</li>
<li>Property tax averages by state from published Census Bureau American Community Survey data.</li>
</ul>
"""

GUIDES["home-affordability-calculator.html"] = """
<h2>How to use this affordability calculator</h2>
<ol>
<li><strong>Income.</strong> Enter gross household income before taxes, the figure lenders use. Include steady bonuses or second jobs only if you have received them for at least two years.</li>
<li><strong>Monthly debts.</strong> Add minimum payments on car loans, student loans, credit cards, personal loans and child support. Do not include rent, utilities or groceries.</li>
<li><strong>Down payment, rate and term.</strong> These turn your monthly budget into a loan amount and then a home price.</li>
<li><strong>Taxes, insurance and HOA.</strong> They come out of the same housing budget, so a high-tax area lowers the price you can afford.</li>
<li><strong>Debt limit.</strong> Choose 36% for a conservative budget or a higher limit to see what some loan programs allow.</li>
</ol>

<h2>How interest rates change what you can afford</h2>
<p>Lenders approve a payment, not a price. If $1,800 a month is available for principal and interest on a 30-year loan, that supports a loan of about $300,200 at 6% but only about $270,600 at 7%. One point of interest removes nearly $30,000 of buying power. When rates are high, a larger down payment or a lower-priced area does more for your budget than a higher income.</p>

<h2>Front-end and back-end ratios</h2>
<p>The <strong>front-end ratio</strong> is your housing payment divided by gross monthly income. The <strong>back-end ratio</strong> adds every other debt payment. Lenders look at both. With little other debt the 28% housing limit usually binds; with a car loan and student loans the 36% total limit often binds first. The calculator applies whichever is lower, and the result tells you which one is limiting you.</p>

<h2>How to afford more house</h2>
<p>Small debts often matter more than income. Clearing a $300 car payment frees $300 of the 36% limit, which can be worth $40,000 or more of home price. A bigger down payment lowers the loan and can remove PMI once you reach 20%, and a better credit score can lower your rate by a quarter to a half point.</p>
<p>It is also worth asking lenders about FHA, VA and USDA loans and your state's first-time buyer programs. They require smaller down payments and sometimes allow higher debt ratios.</p>

<h2>Affordable for the lender versus affordable for you</h2>
<p>The 28/36 rule uses gross income, but you live on take-home pay. A household earning $90,000 might take home about $5,800 a month after taxes and retirement savings, so a $2,100 housing payment is over a third of what actually reaches the bank account. Before you commit, add up your real monthly spending, keep three to six months of expenses in savings after closing and leave room for maintenance, which commonly runs 1% to 2% of the home's value a year.</p>

<h2>Sources</h2>
<ul>
<li>Consumer Financial Protection Bureau, <a href="https://www.consumerfinance.gov/owning-a-home/" rel="nofollow">Buying a House</a>.</li>
<li>Fannie Mae Selling Guide, debt-to-income ratio requirements for conventional loans.</li>
<li>HUD guidance on FHA loan qualifying ratios.</li>
</ul>
"""

GUIDES["auto-loan-calculator.html"] = """
<h2>How to use this auto loan calculator</h2>
<ol>
<li><strong>Vehicle price.</strong> Use the negotiated price before tax, not the sticker price.</li>
<li><strong>Down payment and trade-in.</strong> Both reduce the amount you borrow. If you still owe money on the trade-in, enter that too; it is added back to the new loan.</li>
<li><strong>State and sales tax.</strong> Picking a state fills in its combined average rate. Most states tax only the price minus the trade-in.</li>
<li><strong>Fees, rate and term.</strong> Add title, registration and dealer documentation fees, then the APR and length of the loan.</li>
</ol>
<p>The results show the monthly payment, the amount financed, total interest, sales tax and the full cost of the car, plus a table that compares the same loan across terms from 36 to 84 months.</p>

<h2>Dealer financing versus a cash rebate</h2>
<p>Manufacturers often offer a choice between a low promotional rate and a cash rebate. Run both through the calculator. On a $30,000 loan over 60 months, a 2.9% promotional rate gives a payment of $538 and about $2,260 of interest. Taking a $2,000 rebate instead and financing $28,000 at 6.9% gives a payment of $553 and about $5,190 of interest. Here the low rate wins by about $15 a month. With a larger rebate or a cheaper credit union loan the answer can flip, so compare the total you pay, not just the rate.</p>

<h2>Negative equity</h2>
<p>If you owe more on your current car than it is worth, the difference is rolled into the new loan. You then pay interest on a car you no longer own and start the new loan underwater. Paying the gap in cash, waiting until the old loan is paid down or choosing a cheaper car avoids carrying debt from one car to the next.</p>

<h2>Get pre-approved first</h2>
<p>A pre-approval from a bank or credit union tells you the rate you qualify for before you walk into a dealership. You can then ask the dealer to beat it. Rate shopping within about two weeks counts as a single inquiry for most credit scoring models, so comparing several lenders does little harm to your score.</p>

<h2>Total cost of owning the car</h2>
<p>The loan payment is only part of the cost. Insurance, fuel or charging, maintenance, registration and depreciation all add up. A common budgeting guideline is to keep all car costs, including the payment, under 10% to 15% of take-home pay, and to put at least 10% to 20% down so the loan does not exceed the car's value.</p>

<h2>Dealership traps</h2>
<p>Negotiate the price of the car, not the monthly payment: a dealer can hit almost any payment by stretching the term. Add-ons such as extended warranties, paint protection and GAP coverage are often rolled into the loan, so check what they cost elsewhere before agreeing. And if you need 84 months to afford a car, it is probably too expensive, because long terms raise the interest and keep you owing more than the car is worth.</p>

<h2>Sources</h2>
<ul>
<li>Consumer Financial Protection Bureau, <a href="https://www.consumerfinance.gov/consumer-tools/auto-loans/" rel="nofollow">Auto loans</a>.</li>
<li>Federal Trade Commission guidance on buying and financing a vehicle.</li>
<li>State sales tax rates from state revenue departments and published combined state and local averages.</li>
</ul>
"""

GUIDES["personal-loan-calculator.html"] = """
<h2>How to use this personal loan calculator</h2>
<ol>
<li><strong>Loan amount.</strong> Enter the amount you will repay, which is the amount the lender approves, not the cash you receive after fees.</li>
<li><strong>Interest rate and term.</strong> Use the rate from your offer and the length in months or years.</li>
<li><strong>Origination fee.</strong> Enter it as a percent. The calculator subtracts it from the money you receive and works out the true APR.</li>
</ol>
<p>You get the monthly payment, total interest, the cash you actually receive and the APR, which is the number to compare across lenders.</p>

<h2>Using a personal loan to pay off credit cards</h2>
<p>Debt consolidation is one of the most common reasons to borrow. Suppose you owe $12,000 on cards at 24% and pay $400 a month. It would take about 47 months and roughly $6,500 of interest to clear. A 36-month personal loan at 12% has a payment of about $399 and total interest of about $2,350. For almost the same monthly payment you finish 11 months sooner and save about $4,160.</p>
<p>The saving only holds if the cards stay paid off. Running the balances up again leaves you with both the loan and new card debt. Many people keep the cards open for their credit history but remove them from online wallets.</p>

<h2>What lenders look at</h2>
<p>Your credit score has the biggest effect on the rate, and scores above about 720 usually get the best offers. Lenders also check your debt-to-income ratio; many want total debt payments, including the new loan, under 35% to 45% of gross income. Steady income and employment history lower their risk as well.</p>
<p>Most online lenders let you check your rate with a soft credit pull that does not affect your score, so you can compare several offers before formally applying.</p>

<h2>Fixed payments and early payoff</h2>
<p>Personal loans are usually fixed-rate installment loans, so the payment never changes. Interest is charged on the remaining balance, which means early or extra payments reduce the total you pay. Most lenders do not charge prepayment penalties, but read the agreement. A shorter term raises the payment and lowers total interest; a longer term does the opposite.</p>

<h2>Alternatives worth comparing</h2>
<ul>
<li>A 0% balance transfer card, if you can repay within the promotional period.</li>
<li>A credit union personal loan, often with lower rates and smaller fees.</li>
<li>A hardship or payment plan from your current creditor.</li>
<li>Nonprofit credit counseling and a debt management plan, which can lower card interest rates.</li>
</ul>

<h2>Before you accept an offer</h2>
<p>Compare APRs rather than interest rates whenever the fees differ. If a fee will be deducted from the loan, borrow enough to cover it so you are not left short. And check total interest before picking the longest term just because its payment is lowest.</p>

<h2>Sources</h2>
<ul>
<li>Consumer Financial Protection Bureau, information on personal installment loans and comparing APRs.</li>
<li>Truth in Lending Act (Regulation Z), which requires lenders to disclose the APR including finance charges.</li>
</ul>
"""

GUIDES["credit-card-payoff-calculator.html"] = """
<h2>How to use this credit card payoff calculator</h2>
<ol>
<li><strong>Card balance and APR.</strong> Copy both from your latest statement. If part of the balance has a different rate, such as a cash advance, use the higher rate for a cautious estimate.</li>
<li><strong>Monthly payment.</strong> Enter what you can pay every month. The calculator shows how many months it takes and the total interest.</li>
<li><strong>Or pay off in.</strong> Enter a number of months instead to see the payment needed to be debt-free by a date.</li>
</ol>
<p>The calculator assumes you stop using the card while paying it off. New purchases add to the balance and push the payoff date back.</p>

<h2>How card interest is charged</h2>
<p>Card issuers divide the APR by 365 to get a daily rate and apply it to your average daily balance, then add the interest at the end of each billing cycle. A 22% APR is about 0.06% a day. On a $6,500 balance that is roughly $119 of interest a month, so a $150 payment only reduces the balance by about $31. Paying more than the interest charge is what moves the balance, which is why each extra dollar matters so much early on.</p>

<h2>Avalanche or snowball for several cards</h2>
<p>If you have more than one card, pay the minimum on all of them and put every extra dollar toward one card at a time.</p>
<p>The avalanche method targets the card with the highest APR first, which costs the least interest. The snowball method targets the smallest balance first instead. It costs a little more, but you clear whole cards sooner, and many people find that easier to stick with.</p>
<p>When one card is paid off, add its whole payment to the next card. Run each card through this calculator to see when each will be gone.</p>

<h2>When a balance transfer pays off</h2>
<p>A $6,000 balance at 22% paid at $350 a month takes 21 months and costs about $1,270 in interest. Moving it to a card with 0% for 18 months and a 3% transfer fee adds $180 to the balance, and $350 a month clears $6,180 in about 18 months. The transfer saves around $1,090, but only if you pay it off before the promotion ends. Any balance left after that is charged the card's regular APR, which is often over 20%.</p>

<h2>What paying down a card does for your credit</h2>
<p>Credit utilization, the share of your card limits you are using, is one of the largest factors in credit scores. Keeping it under 30% helps, and under 10% is better. Paying down balances usually raises your score within a month or two as the new balances are reported, which can also help you qualify for lower rates on a mortgage or car loan.</p>

<h2>Habits that keep balances high</h2>
<p>Paying only the minimum is the slowest route; the minimum payment warning on your statement shows how many years it would take. Closing cards as soon as they are paid off can backfire too, because it lowers your available credit and raises utilization. Also check the APR on cash advances and any penalty rate, which are often much higher than the purchase APR.</p>

<h2>Sources</h2>
<ul>
<li>Consumer Financial Protection Bureau, <a href="https://www.consumerfinance.gov/consumer-tools/credit-cards/" rel="nofollow">Credit cards</a>.</li>
<li>Credit CARD Act of 2009, which requires the minimum payment warning on monthly statements.</li>
</ul>
"""

GUIDES["debt-to-income-calculator.html"] = """
<h2>How to use this debt-to-income calculator</h2>
<ol>
<li><strong>Gross monthly income.</strong> Enter income before taxes and deductions. For a yearly salary, divide by 12. Lenders average variable income, such as overtime or self-employment income, over the last two years.</li>
<li><strong>Housing payment.</strong> Enter rent, or the full mortgage payment including taxes, insurance and HOA dues. When applying for a new mortgage, enter the expected new payment instead of your current rent.</li>
<li><strong>Other debts.</strong> Enter required monthly payments on car loans, student loans, credit card minimums and anything else that shows on your credit report or court orders, such as child support.</li>
</ol>
<p>The calculator shows your total debt-to-income ratio, your housing ratio and how lenders are likely to view the result.</p>

<h2>Front-end and back-end DTI</h2>
<p>Lenders usually check two numbers. The <strong>front-end ratio</strong> is housing alone; the <strong>back-end ratio</strong> includes all debts. For example, with $6,000 of gross monthly income, a $1,500 mortgage payment gives a front-end ratio of 25%. Add a $450 car payment, $250 of student loans and $100 of card minimums and the back-end ratio is $2,300 / $6,000, or 38.3%. That is acceptable for most mortgages but above the 36% that gets the best terms.</p>

<h2>Typical limits by loan type</h2>
<div class="table-scroll"><table><thead><tr><th>Loan</th><th>Common back-end limit</th></tr></thead><tbody>
<tr><td>Conventional mortgage</td><td>36% to 45%, up to 50% with strong credit and reserves</td></tr>
<tr><td>FHA mortgage</td><td>43%, higher with compensating factors</td></tr>
<tr><td>VA mortgage</td><td>41% guideline, with residual income also checked</td></tr>
<tr><td>Auto and personal loans</td><td>Often 40% to 50%, varies by lender</td></tr>
</tbody></table></div>
<p>These are general guidelines. Each lender and automated underwriting system weighs DTI together with your credit score, down payment and savings.</p>

<h2>What does not count as debt</h2>
<p>Utilities, phone bills, insurance premiums other than those in your mortgage payment, groceries, subscriptions and income taxes are not part of DTI, even though they come out of your budget. Student loans in deferment may still count: many lenders use a percentage of the balance, such as 0.5% or 1%, if no payment is reported.</p>

<h2>How to lower your ratio</h2>
<p>Paying off a small loan entirely helps more than paying a little off a large one, because it removes the whole payment from the ratio. Avoid taking on new debt before you apply: a car loan taken out the month before a mortgage application can push you over a limit. Refinancing or extending a loan lowers the payment and the ratio, though it may cost more interest over time. A co-borrower's income or documented side income lowers it as well.</p>

<h2>Sources</h2>
<ul>
<li>Consumer Financial Protection Bureau, explanation of debt-to-income ratio and the qualified mortgage rule.</li>
<li>Fannie Mae Selling Guide, debt-to-income ratio requirements.</li>
<li>HUD and VA lender guidance on qualifying ratios.</li>
</ul>
"""

GUIDES["paycheck-calculator.html"] = """
<h2>How to use this paycheck calculator</h2>
<ol>
<li><strong>Annual salary and pay frequency.</strong> Enter your yearly gross pay and how often you are paid. Hourly workers can multiply their rate by hours per week and 52.</li>
<li><strong>Filing status.</strong> Choose the status you expect to file with. It sets the standard deduction and tax brackets.</li>
<li><strong>State.</strong> The calculator applies your state's 2026 income tax. You can enter your own rate if you know it.</li>
<li><strong>401(k) and health premium.</strong> Pre-tax deductions lower your taxable income, so they reduce your take-home pay by less than their full amount.</li>
</ol>

<h2>Marginal versus effective tax rate</h2>
<p>Tax brackets apply in layers. Only the income inside each bracket is taxed at that bracket's rate. A single filer with $50,000 of taxable income in 2026 pays 10% on the first $12,400 ($1,240) and 12% on the remaining $37,600 ($4,512), for $5,752 of federal income tax. The top rate reached is 12%, but the effective rate is about 11.5%. A raise that moves you into a higher bracket never lowers your take-home pay, because only the extra dollars are taxed at the higher rate.</p>

<h2>Pre-tax and after-tax deductions</h2>
<p>Pre-tax deductions include traditional 401(k) and 403(b) contributions, most employer health, dental and vision premiums, and contributions to a health savings account (HSA) or flexible spending account (FSA). They reduce federal income tax, and all of them except 401(k) contributions usually reduce FICA too. After-tax deductions, such as Roth 401(k) contributions, union dues, wage garnishments and some insurance, come out after the tax is calculated.</p>
<p>Because of the tax saving, contributing $200 per paycheck to a traditional 401(k) lowers take-home pay by less than $200, often by $150 to $170 depending on your bracket.</p>

<h2>Why your actual paycheck may differ</h2>
<p>Your Form W-4 is the usual reason. Extra withholding, dependents or a second job entered there change how much federal tax your employer takes out. Local income taxes are another: some cities and counties, including New York City and many in Ohio and Pennsylvania, add their own, and this calculator leaves them out. A few states also take disability or paid family leave contributions from wages. Bonuses are often withheld at a flat 22% federal rate, which can differ from your regular rate.</p>

<h2>Check your withholding once a year</h2>
<p>Withholding is an estimate of your final tax bill. If too little is withheld you owe money in April; too much and you have given the government an interest-free loan. The IRS Tax Withholding Estimator compares your year-to-date pay stubs with your expected tax and tells you how to update your W-4. It is worth running after a raise, a new job, marriage or a new child.</p>

<h2>Sources</h2>
<ul>
<li>IRS, <a href="https://www.irs.gov/publications/p15t" rel="nofollow">Publication 15-T, Federal Income Tax Withholding Methods</a>, and the 2026 inflation adjustments to brackets and the standard deduction.</li>
<li>Social Security Administration, <a href="https://www.ssa.gov/oact/cola/cbb.html" rel="nofollow">Contribution and benefit base</a> for 2026.</li>
<li>Tax Foundation, State Individual Income Tax Rates and Brackets, 2026.</li>
</ul>
"""

GUIDES["salary-to-hourly-calculator.html"] = """
<h2>How to use this salary converter</h2>
<ol>
<li><strong>Pay amount and period.</strong> Enter any rate, such as $25 an hour or $65,000 a year, and choose how often it is paid.</li>
<li><strong>Hours and days per week.</strong> Change these for part-time work, a four-day week or regular overtime.</li>
<li><strong>Paid weeks per year.</strong> Use 52 if you get paid time off. For contract or seasonal work, enter only the weeks you are paid.</li>
</ol>
<p>The calculator converts the amount to hourly, daily, weekly, biweekly, semimonthly, monthly and yearly pay at the same time.</p>

<h2>Biweekly versus semimonthly pay</h2>
<p>Biweekly pay arrives every two weeks, 26 times a year. Semimonthly pay arrives twice a month, 24 times a year. On the same $60,000 salary, a biweekly check is $2,307.69 and a semimonthly check is $2,500. With biweekly pay, two months each year have three paydays, which many people use for savings or extra debt payments.</p>

<h2>Overtime</h2>
<p>Under the federal Fair Labor Standards Act, non-exempt employees must be paid at least 1.5 times their regular rate for hours over 40 in a workweek. Someone earning $22 an hour who works 45 hours earns $880 for the first 40 hours plus $165 for five overtime hours, $1,045 in total. Many salaried professional, executive and administrative employees are exempt from overtime, but only if they meet the duties test and a minimum salary threshold. Some states, including California, have stricter rules, such as daily overtime.</p>

<h2>Comparing a salaried job with contract work</h2>
<p>A salary of $75,000 works out to about $36 an hour over 2,080 hours. A contractor charging $36 an hour earns much less in practice, because employees also receive paid time off, the employer's half of Social Security and Medicare (7.65%), health insurance and retirement contributions. Benefits commonly add 25% to 40% to the cost of a salaried worker. To match the $75,000 job with benefits worth 30%, a contractor would need around $47 an hour for the same hours, before accounting for unpaid time between projects.</p>

<h2>Comparing offers fairly</h2>
<p>When you compare an hourly offer with a salary, count unpaid weeks and benefits, not just the rate. Remember that both figures are gross pay; the paycheck calculator shows what you keep after taxes. Salaried jobs also do not pay for extra hours if you are exempt, so a 50-hour week lowers your effective hourly rate.</p>

<h2>Sources</h2>
<ul>
<li>US Department of Labor, <a href="https://www.dol.gov/agencies/whd/flsa" rel="nofollow">Fair Labor Standards Act</a> overtime and exemption rules.</li>
<li>Bureau of Labor Statistics, Employer Costs for Employee Compensation, for the share of pay that goes to benefits.</li>
</ul>
"""

GUIDES["401k-calculator.html"] = """
<h2>How to use this 401(k) calculator</h2>
<ol>
<li><strong>Ages.</strong> Enter your current age and the age you plan to retire. The gap is how many years your money compounds.</li>
<li><strong>Salary and raises.</strong> Your contribution and your employer's match are a percent of salary, so expected raises increase both over time.</li>
<li><strong>Current balance and contribution.</strong> Include any old 401(k) or rollover IRA you plan to keep invested. Enter your own contribution as a percent of pay.</li>
<li><strong>Employer match.</strong> Enter the match rate and the share of salary it applies to, for example 50% up to 6%.</li>
<li><strong>Expected return.</strong> A long-run average of 5% to 7% a year is a common planning range for a diversified portfolio after fees.</li>
</ol>
<p>The calculator caps your own contributions at the 2026 IRS limits, including the catch-up for ages 50 and over, and shows the balance at retirement, how much came from you, your employer and investment growth.</p>

<h2>The cost of waiting</h2>
<p>Time matters more than any other input. Saving $300 a month from age 25 to 65 at a 7% return grows to about $787,000, from $144,000 of contributions. Starting at 35 with the same $300 a month grows to about $366,000. Ten years of delay costs $36,000 in contributions but more than $420,000 in final balance, because the earliest dollars compound the longest.</p>

<h2>Traditional or Roth 401(k)</h2>
<p>Traditional contributions go in before tax, which lowers your taxable income now, and withdrawals in retirement are taxed as income. Roth contributions go in after tax, and qualified withdrawals, growth included, are tax-free.</p>
<p>A traditional account tends to win if you expect a lower tax rate in retirement than today; a Roth tends to win if you expect the same or higher rate, which is common early in a career. Many people split contributions to hedge. Employer matching contributions have traditionally gone into the pre-tax side, though plans may now offer Roth matching. The calculator's projection applies to either type; only the taxes differ.</p>

<h2>Vesting</h2>
<p>Your own contributions are always 100% yours. Employer contributions may vest over time, for example 20% a year over five years, or all at once after three years. If you leave before you are fully vested, you forfeit the unvested part of the match. Check your plan's summary plan description before changing jobs.</p>

<h2>Fees</h2>
<p>A fund's expense ratio comes out of your return every year. On a long horizon, the difference between a 0.05% index fund and a 1% actively managed fund can reduce the final balance by 20% or more. If your plan offers low-cost index funds or target-date funds, compare their expense ratios with the alternatives. Lower the expected return in the calculator by your total fees to see their effect.</p>

<h2>Withdrawals before retirement</h2>
<p>Withdrawals before age 59 and a half usually face income tax plus a 10% penalty, with some exceptions, such as separating from your employer in or after the year you turn 55. Loans from a 401(k) avoid the penalty but must be repaid, and the borrowed money misses out on market growth while it is out of the account.</p>

<h2>Sources</h2>
<ul>
<li>IRS, <a href="https://www.irs.gov/retirement-plans/401k-plans" rel="nofollow">401(k) plans</a> and the 2026 contribution limits: $24,500 deferral, $8,000 catch-up at 50 and over, $11,250 for ages 60 to 63.</li>
<li>US Department of Labor, guidance on 401(k) plan fees.</li>
</ul>
"""

GUIDES["compound-interest-calculator.html"] = """
<h2>How to use this compound interest calculator</h2>
<ol>
<li><strong>Initial deposit.</strong> The amount you start with today. It can be zero.</li>
<li><strong>Monthly contribution.</strong> What you plan to add each month.</li>
<li><strong>Annual interest rate.</strong> For a savings account use its APY. For investments, use a long-run average return you are comfortable assuming.</li>
<li><strong>Years and compounding.</strong> Choose how long to save and how often interest is added: daily, monthly, quarterly or yearly.</li>
</ol>
<p>The results show the final balance, how much of it you contributed and how much is interest, along with a year-by-year table.</p>

<h2>How much compounding frequency matters</h2>
<p>$10,000 at 5% for 10 years grows to:</p>
<div class="table-scroll"><table><thead><tr><th>Compounding</th><th>Balance after 10 years</th></tr></thead><tbody>
<tr><td>Yearly</td><td>$16,289</td></tr>
<tr><td>Monthly</td><td>$16,470</td></tr>
<tr><td>Daily</td><td>$16,487</td></tr>
</tbody></table></div>
<p>Moving from yearly to monthly compounding adds about $180; going from monthly to daily adds only $17. The rate and the length of time matter far more than the frequency.</p>

<h2>APR versus APY</h2>
<p>APR is the simple annual rate. APY, or annual percentage yield, includes the effect of compounding within the year. A 5% APR compounded monthly equals an APY of about 5.12%. Banks advertise APY on savings because it is the higher number, and lenders advertise APR on loans for the same reason. When comparing savings accounts, compare APYs.</p>

<h2>Inflation and real returns</h2>
<p>A balance that grows at 7% while prices rise 3% a year gains only about 3.9% a year in purchasing power. To see what a future balance is worth in today's dollars, subtract the expected inflation rate from your interest rate and run the calculator again. This matters most for long goals such as retirement, where even modest inflation roughly halves the value of a dollar over 25 years.</p>

<h2>Taxes on interest and investment growth</h2>
<p>Interest from savings accounts and CDs is taxed as ordinary income each year, which reduces the effective rate. Growth in tax-advantaged accounts such as a 401(k), IRA or HSA compounds without yearly tax, which is one reason those accounts grow faster for the same return.</p>

<h2>Where compounding works against you</h2>
<p>The same math applies to debt. A credit card balance at 22% compounds daily, so an unpaid balance grows quickly. Paying off high-interest debt is often the best guaranteed return available.</p>

<h2>Sources</h2>
<ul>
<li>US Securities and Exchange Commission, <a href="https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator" rel="nofollow">Investor.gov compound interest resources</a>.</li>
<li>Truth in Savings Act (Regulation DD), which requires banks to disclose APY.</li>
</ul>
"""

GUIDES["savings-goal-calculator.html"] = """
<h2>How to use this savings goal calculator</h2>
<ol>
<li><strong>Savings goal.</strong> The total you want to have, such as $20,000 for a down payment.</li>
<li><strong>Already saved.</strong> Money set aside for this goal today. It earns interest too.</li>
<li><strong>Years to reach it.</strong> Your deadline. Shorter deadlines need larger monthly amounts.</li>
<li><strong>Interest rate (APY).</strong> The yield on the account where you will keep the money.</li>
</ol>
<p>The calculator shows the amount to save each month, how much of the goal comes from your deposits and how much from interest.</p>

<h2>Example: a down payment in three years</h2>
<p>To reach $20,000 in 36 months starting from zero, you would need $555.56 a month with no interest. In a high-yield savings account earning 4% APY, interest does part of the work and the required deposit falls to about $524 a month. The longer the deadline and the higher the rate, the more interest contributes.</p>

<h2>How big should an emergency fund be?</h2>
<p>A common guideline is three to six months of essential expenses: housing, utilities, food, insurance, transportation and minimum debt payments. Aim for the higher end if your income is irregular, you are self-employed, you are the only earner in your household or you work in an industry with frequent layoffs. Build a starter fund of $1,000 to $2,000 first, then work toward the full amount.</p>

<h2>Where to keep the money</h2>
<p>For most short-term goals, a high-yield savings account is the simplest choice. You can withdraw at any time, and FDIC or NCUA insurance covers up to $250,000 per depositor, per bank, per ownership category. Certificates of deposit lock in a fixed rate for a set term, which suits a goal with a firm date, though early withdrawal usually costs some interest. Treasury bills are short-term government debt and are exempt from state income tax. Stocks and other investments only make sense for goals more than about five years away, because prices can fall right when you need the money.</p>

<h2>Saving for several goals</h2>
<p>Run the calculator once for each goal, then add up the monthly amounts. If the total is more than you can afford, push back the least urgent deadline or lower its target. Many banks let you open separate savings buckets for each goal, which makes progress easy to see.</p>

<h2>Making the plan stick</h2>
<p>Keep goal money out of checking, where it earns little or nothing, and out of stocks if you need it within a year or two. Saving whatever is left at the end of the month rarely works; an automatic transfer on payday is far more reliable.</p>

<h2>Sources</h2>
<ul>
<li>Federal Deposit Insurance Corporation, <a href="https://www.fdic.gov/resources/deposit-insurance" rel="nofollow">Deposit insurance</a> coverage limits.</li>
<li>Consumer Financial Protection Bureau, guidance on building an emergency fund.</li>
</ul>
"""

GUIDES["bmi-calculator.html"] = """
<h2>How to use this BMI calculator</h2>
<ol>
<li><strong>Height.</strong> Enter your height in feet and inches without shoes.</li>
<li><strong>Weight.</strong> Weigh yourself in light clothing, ideally in the morning, since weight can vary by a few pounds over a day.</li>
</ol>
<p>You will see your BMI, its category and the healthy weight range for your height. This calculator is for adults 20 and older.</p>

<h2>Healthy weight range by height</h2>
<p>A healthy BMI is 18.5 to 24.9. Converted to pounds, that range depends on height. At 5 feet 5 inches, for example, it runs from about 111 to 150 pounds. The calculator works out the range for your exact height, which is often a more useful target than the BMI number itself.</p>

<h2>What BMI does not tell you</h2>
<p>BMI is a quick screening tool based only on height and weight. It does not measure body fat directly, so it has known limits:</p>
<p>Athletes and other people with a lot of muscle can have a high BMI with little body fat. Older adults tend to carry more fat than younger adults at the same BMI, and women generally carry more than men. Ancestry matters too: health risks for some groups, including many people of Asian descent, start at a lower BMI, and some guidelines use lower cutoffs for them. BMI also says nothing about where fat sits, and fat around the abdomen carries more risk than fat elsewhere.</p>

<h2>Waist size as a second check</h2>
<p>Measuring your waist adds information BMI misses. Place a tape measure around your bare abdomen just above the hip bones and breathe out normally. A waist over 40 inches for men or over 35 inches for women, if you are not pregnant, is linked to a higher risk of type 2 diabetes and heart disease, even when BMI is in the healthy range.</p>

<h2>Children and teens</h2>
<p>For people aged 2 to 19, BMI is compared with others of the same age and sex using CDC growth charts and reported as a percentile. The adult categories on this page do not apply to them; a pediatrician can interpret a child's BMI percentile.</p>

<h2>If your BMI is outside the healthy range</h2>
<p>A BMI result is a starting point for a conversation, not a diagnosis. A doctor can consider your blood pressure, blood sugar, cholesterol, family history and activity level. If weight loss is a goal, even 5% to 10% of body weight can improve blood pressure and blood sugar. The calorie calculator on this site can help you estimate a daily target.</p>

<h2>Sources</h2>
<ul>
<li>Centers for Disease Control and Prevention, <a href="https://www.cdc.gov/bmi/" rel="nofollow">Body Mass Index (BMI)</a>, adult categories and child percentiles.</li>
<li>National Heart, Lung, and Blood Institute, guidance on waist circumference and health risk.</li>
</ul>
"""

GUIDES["calorie-calculator.html"] = """
<h2>How to use this calorie calculator</h2>
<ol>
<li><strong>Age, sex, height and weight.</strong> These feed the Mifflin-St Jeor equation, which estimates the calories your body burns at rest.</li>
<li><strong>Activity level.</strong> Choose the level that matches a typical week, not your most active one. Most people overestimate their activity.</li>
</ol>
<p>The calculator shows the calories to maintain your weight and targets for losing or gaining weight at different rates.</p>

<h2>Example</h2>
<p>A 35-year-old woman who is 5 feet 5 inches tall and weighs 150 pounds has an estimated resting metabolic rate of about 1,376 calories. With a moderate activity level (exercise 3 to 5 days a week, factor 1.55), her maintenance calories are about 2,130 a day. Eating about 500 fewer calories a day, roughly 1,630, is a common starting point for losing weight gradually.</p>

<h2>The 3,500-calorie rule and why progress slows</h2>
<p>A pound of body fat stores roughly 3,500 calories, which is where the idea that a 500-calorie daily deficit loses a pound a week comes from. It works as a rough starting point, but real weight loss slows over time: as you lose weight your body needs fewer calories, and it adapts by using a little less energy. Recalculate your target every 10 to 15 pounds, and judge progress by the trend over several weeks rather than daily weigh-ins.</p>

<h2>Safe limits</h2>
<p>Losing 0.5 to 2 pounds a week is a common recommendation. Very low intake makes it hard to get enough protein, vitamins and minerals. Many health professionals advise not going below about 1,200 calories a day for women or 1,500 for men without medical supervision. People who are pregnant, breastfeeding, under 18 or managing a health condition should get advice from a doctor or registered dietitian.</p>

<h2>What to eat, not just how much</h2>
<p>Protein helps preserve muscle while you lose weight and keeps you full, so spread it across your meals. Vegetables, fruit, beans and whole grains add fiber and volume for few calories. Sugary drinks, juice and alcohol do the opposite, adding calories without making you feel full.</p>
<p>The Dietary Guidelines for Americans suggest getting 10% to 35% of calories from protein, 45% to 65% from carbohydrates and 20% to 35% from fat.</p>

<h2>How accurate is the estimate?</h2>
<p>The Mifflin-St Jeor equation predicts resting metabolic rate within about 10% for most people, and activity is harder still to estimate. Treat the result as a starting point. Track your intake and weight for two to three weeks; if your weight is stable at a different intake, that number is your real maintenance level.</p>

<h2>Sources</h2>
<ul>
<li>Mifflin MD, St Jeor ST, et al. A new predictive equation for resting energy expenditure in healthy individuals. American Journal of Clinical Nutrition, 1990.</li>
<li>US Department of Agriculture and HHS, <a href="https://www.dietaryguidelines.gov/" rel="nofollow">Dietary Guidelines for Americans</a>.</li>
<li>National Institute of Diabetes and Digestive and Kidney Diseases, Body Weight Planner research on metabolic adaptation.</li>
</ul>
"""

GUIDES["due-date-calculator.html"] = """
<h2>How to use this due date calculator</h2>
<ol>
<li><strong>First day of your last period.</strong> Enter the date your last menstrual period started, not the day it ended.</li>
<li><strong>Average cycle length.</strong> Count from the first day of one period to the first day of the next. The default is 28 days. Longer or shorter cycles shift the due date.</li>
</ol>
<p>The calculator shows your estimated due date, how far along you are in weeks and days and when each trimester starts.</p>

<h2>Weeks of pregnancy at a glance</h2>
<div class="table-scroll"><table><thead><tr><th>Stage</th><th>Weeks</th></tr></thead><tbody>
<tr><td>First trimester</td><td>Week 1 to the end of week 13</td></tr>
<tr><td>Second trimester</td><td>Week 14 to the end of week 27</td></tr>
<tr><td>Third trimester</td><td>Week 28 until birth</td></tr>
<tr><td>Early term</td><td>37 weeks 0 days to 38 weeks 6 days</td></tr>
<tr><td>Full term</td><td>39 weeks 0 days to 40 weeks 6 days</td></tr>
<tr><td>Late term</td><td>41 weeks 0 days to 41 weeks 6 days</td></tr>
<tr><td>Post-term</td><td>42 weeks and later</td></tr>
</tbody></table></div>

<h2>How accurate is a due date?</h2>
<p>A due date is an estimate. Only a small share of babies, often quoted at around 4% to 5%, are born on the exact day; most arrive within two weeks before or after it. The date from your last period assumes ovulation on about day 14 of your cycle, which varies from person to person and month to month.</p>

<h2>When an ultrasound changes the date</h2>
<p>An ultrasound in the first trimester measures the embryo and is the most accurate way to date a pregnancy. If it differs from the date based on your last period by more than about 5 to 7 days in early pregnancy, your provider will usually use the ultrasound date. After that, the due date normally stays fixed, even if later scans measure the baby as larger or smaller.</p>

<h2>Pregnancies after IVF</h2>
<p>With in vitro fertilization the due date is calculated from the embryo transfer date: 266 days after the transfer of a day-5 embryo, or 263 days after a day-3 transfer is commonly used. This calculator is based on the last period, so use the date your fertility clinic gives you.</p>

<h2>Early prenatal care</h2>
<p>Most providers like to see you for a first prenatal visit around 8 to 10 weeks. Start a daily prenatal vitamin with at least 400 micrograms of folic acid as soon as you know you are pregnant, ideally before conception, to lower the risk of neural tube defects. Contact your provider right away about heavy bleeding, severe pain, fever or severe vomiting.</p>

<h2>Sources</h2>
<ul>
<li>American College of Obstetricians and Gynecologists, Committee Opinion 700, <a href="https://www.acog.org/clinical/clinical-guidance/committee-opinion/articles/2017/05/methods-for-estimating-the-due-date" rel="nofollow">Methods for Estimating the Due Date</a>.</li>
<li>ACOG Committee Opinion 579, Definition of Term Pregnancy.</li>
<li>Centers for Disease Control and Prevention, folic acid recommendations.</li>
</ul>
"""

GUIDES["percentage-calculator.html"] = """
<h2>How to use this percentage calculator</h2>
<p>The page has three calculators. Fill in whichever matches your question; each updates as you type.</p>
<ol>
<li><strong>What is X% of Y?</strong> For discounts, tips, tax and commissions. 15% of $80 is $12.</li>
<li><strong>X is what percent of Y?</strong> For test scores, budgets and progress toward a goal. 30 out of 120 is 25%.</li>
<li><strong>Percent change from X to Y.</strong> For price increases, salary raises and investment returns. From 50 to 65 is a 30% increase.</li>
</ol>

<h2>Percent versus percentage points</h2>
<p>When a rate changes, the difference can be described two ways. If a mortgage rate rises from 6% to 7%, it went up by <strong>one percentage point</strong>, but by <strong>16.7 percent</strong>, because 1 is 16.7% of 6. News reports and loan offers sometimes mix the two, so check which one is meant.</p>

<h2>Stacked discounts do not add up</h2>
<p>A sale of 20% off with an extra 10% off at checkout is not 30% off. The second discount applies to the already reduced price: a $100 item becomes $80, then $72. The total discount is 28%. To combine discounts, multiply the remaining shares: 0.80 &times; 0.90 = 0.72, so you pay 72% of the original price.</p>

<h2>Increases and decreases are not symmetric</h2>
<p>A 50% drop followed by a 50% gain does not get you back to where you started. $100 falls to $50, and a 50% gain on $50 only brings it to $75. To recover from a 50% loss you need a 100% gain. This matters for investments: losses hurt more than equal-sized gains help.</p>

<h2>Working backward from a total</h2>
<p>To find the original amount before tax or a markup was added, divide by one plus the rate. A receipt total of $54 with 8% sales tax had a pre-tax price of $54 / 1.08 = $50. To undo a discount, divide by one minus the rate: a $72 price after 10% off was originally $72 / 0.90 = $80. Taking 8% off $54 gives $49.68, which is a common mistake.</p>

<h2>Everyday uses</h2>
<p>A raise from $62,000 to $65,000 is a 4.8% increase. A test with 42 of 50 answers right scores 84%. Rent of $1,500 on $5,000 of take-home pay takes 30% of the budget, and a $4.00 item that now costs $4.60 has gone up 15%.</p>

<h2>Easy ways to get it wrong</h2>
<p>For percent change, divide by the old value, not the new one. Percentages that apply to different bases, such as stacked discounts, cannot simply be added. And when comparing rates, keep percent changes and percentage point changes apart.</p>
"""

GUIDES["tip-calculator.html"] = """
<h2>How to use this tip calculator</h2>
<ol>
<li><strong>Bill amount.</strong> Enter the total from your check. Many people tip on the amount before tax; enter that if you prefer.</li>
<li><strong>Tip percentage.</strong> Choose 15%, 18%, 20% or 25%, or type your own.</li>
<li><strong>Number of people.</strong> The calculator splits the tip and total evenly.</li>
<li><strong>Round up each share.</strong> Turn this on to round each person's share up to a whole dollar, which makes paying in cash or by app easier.</li>
</ol>

<h2>Before tax or after tax?</h2>
<p>Etiquette guides traditionally recommend tipping on the pre-tax amount, since sales tax is not part of the service. On a $60 meal with 8% tax, a 20% tip is $12 on the pre-tax bill or $12.96 on the $64.80 total. The difference is small, and many people simply tip on the total. Either is acceptable.</p>

<h2>Discounts, coupons and comps</h2>
<p>When you use a coupon, gift card or get an item comped, tip on what the bill would have been at full price. Your server did the same work for the full order.</p>

<h2>Service charges and automatic gratuity</h2>
<p>Some restaurants add an automatic gratuity, often 18% to 20%, for large groups, or a service charge to every bill. Check the receipt before adding a tip so you do not pay twice. A service charge is not always paid to the staff, so you can ask the restaurant how it is used if it matters to you.</p>

<h2>Splitting a bill fairly</h2>
<p>An even split is simplest when everyone ordered similar amounts. When orders differ a lot, add up each person's items, add a share of tax, and apply the tip percentage to each subtotal. Sharing appetizers or a bottle of wine can be split evenly and added on top.</p>

<h2>Counter service, takeout and tip screens</h2>
<p>Payment screens at coffee shops and counters often suggest tips of 15% to 25%. Tipping is optional for counter and takeout orders, where customs vary. Many people leave a small amount, such as a dollar or 10%, for takeout and coffee, and more for complicated or large orders. Whatever you choose, it is your decision rather than the screen's.</p>

<h2>Tipping outside the US</h2>
<p>Tipping customs differ widely. In much of Europe service is included and rounding up or leaving 5% to 10% is common. In Japan and South Korea tipping is generally not expected. In Canada and Mexico, practices are closer to the US, with 15% to 20% typical at restaurants. Check local guidance before you travel.</p>
"""

GUIDES["age-calculator.html"] = """
<h2>How to use this age calculator</h2>
<ol>
<li><strong>Date of birth.</strong> Enter the full date.</li>
<li><strong>Age on this date.</strong> Leave today's date to get your current age, or choose any past or future date, for example a deadline on an application.</li>
</ol>
<p>You get your exact age in years, months and days, your age as a total number of months, weeks and days, and a countdown to your next birthday.</p>

<h2>Age milestones in the US</h2>
<div class="table-scroll"><table><thead><tr><th>Age</th><th>Milestone</th></tr></thead><tbody>
<tr><td>18</td><td>Legal adult in most states; can vote in federal elections</td></tr>
<tr><td>21</td><td>Legal age to buy alcohol and tobacco nationwide</td></tr>
<tr><td>26</td><td>Coverage on a parent's health plan under the Affordable Care Act ends</td></tr>
<tr><td>50</td><td>Eligible for 401(k) and IRA catch-up contributions</td></tr>
<tr><td>59&frac12;</td><td>Withdrawals from 401(k)s and IRAs no longer face the 10% early withdrawal penalty</td></tr>
<tr><td>62</td><td>Earliest age to claim Social Security retirement benefits, at a reduced amount</td></tr>
<tr><td>65</td><td>Eligible for Medicare</td></tr>
<tr><td>67</td><td>Full retirement age for Social Security if you were born in 1960 or later</td></tr>
<tr><td>73</td><td>Required minimum distributions from most retirement accounts begin (75 for those born in 1960 or later)</td></tr>
</tbody></table></div>

<h2>Checking eligibility by a deadline</h2>
<p>Many rules depend on your age on a specific date rather than today: school enrollment cut-offs, sports leagues, insurance policies and job requirements. Enter that date in the second field to see your exact age on it. For example, a child born on October 15, 2021 is 4 years and 10 months old on a September 1, 2026 kindergarten cut-off, not yet 5.</p>

<h2>Why months and days can look uneven</h2>
<p>Months have 28 to 31 days, so there is no fixed number of days in "one month". The calculator counts full calendar months since your last birthday and then the days since that month began, the same way you would count on a calendar. Two people with the same age in years and months can therefore show a different number of total days.</p>

<h2>Age in total days and weeks</h2>
<p>The total days count every day you have been alive, including leap days. Turning 10,000 days old happens at about 27 years and 4 months, a milestone some people like to celebrate. You can use the date field to find exactly when yours falls.</p>

<h2>Sources</h2>
<ul>
<li>Social Security Administration, full retirement age by year of birth.</li>
<li>IRS, required minimum distribution rules under the SECURE 2.0 Act.</li>
<li>Medicare.gov, eligibility at age 65.</li>
</ul>
"""

GUIDES["gpa-calculator.html"] = """
<h2>How to use this GPA calculator</h2>
<ol>
<li><strong>Your classes.</strong> For each class, choose the letter grade and enter its credit hours. Leave unused rows blank.</li>
<li><strong>Cumulative GPA (optional).</strong> Enter your current cumulative GPA and the credits already completed to see how this semester changes it.</li>
</ol>
<p>The calculator shows your semester GPA, total credits and quality points, and your new cumulative GPA.</p>

<h2>How much can you raise your GPA?</h2>
<p>The more credits you have completed, the harder your GPA is to move. A student with a 3.0 over 60 credits who earns straight A's in a 15-credit semester reaches (180 + 60) / 75 = 3.2. Two straight-A semesters bring it to about 3.33. Raising a GPA is fastest in the first year or two, so early semesters matter most. Use the cumulative fields to test different targets before the semester starts.</p>

<h2>Weighted and unweighted GPA</h2>
<p>This calculator gives an unweighted GPA on the standard 4.0 scale, the scale most colleges use. Many high schools also report a weighted GPA that adds points for harder classes, often 0.5 for honors and 1.0 for AP or IB courses, so an A in an AP class counts as 5.0. Weighting rules differ by school, and many colleges recalculate GPA their own way when reviewing applications.</p>

<h2>Pass/fail, withdrawals and retakes</h2>
<p>A pass in a pass/fail class usually earns credit but no grade points, so it does not count in your GPA, although some schools count a fail as an F. A withdrawal (W) normally has no effect. Retakes vary: many colleges replace the original grade with the new one, while others average the two. Schools also differ on plus grades; some do not use A+, some count it as 4.0 and others as 4.3.</p>

<h2>Why GPA matters</h2>
<p>Many scholarships require a minimum GPA, often 3.0 or higher, to keep the award. Federal financial aid requires satisfactory academic progress, which usually means at least a 2.0 cumulative GPA by the end of the second year. Graduate programs and some employers also set GPA cut-offs, commonly 3.0.</p>

<h2>Sources</h2>
<ul>
<li>Federal Student Aid, <a href="https://studentaid.gov/" rel="nofollow">satisfactory academic progress</a> requirements.</li>
<li>Standard 4.0 grade point scale used by most US colleges and universities.</li>
</ul>
"""
