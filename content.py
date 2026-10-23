"""Worked examples and FAQs shown under each calculator.

Example figures come from the same formulas the calculators use (checked against the live scripts).
Each FAQ answer is HTML; it is also published, without tags, as FAQPage structured data.
"""

CONTENT = {
    "mortgage-calculator.html": {
        "examples": """
<h3>Example 1: a $400,000 home with 10% down</h3>
<p>You put $40,000 down, so the loan is $360,000 at 6.75% for 30 years. Principal and interest come to $2,335 a month. Add property tax at 1.2% ($400 a month), homeowners insurance of $1,500 a year ($125) and PMI at 0.5% of the loan ($150), and the full payment is about $3,010. Over 30 years you would pay roughly $480,600 in interest.</p>
<h3>Example 2: 15-year vs. 30-year loan on $300,000</h3>
<p>A 30-year loan at 6.5% costs $1,896 a month and about $382,600 in total interest. A 15-year loan at 5.75% costs $2,491 a month, $595 more, but total interest drops to about $148,400. The shorter loan saves more than $234,000 if you can afford the higher payment.</p>
""",
        "faq": [
            ("What is included in a mortgage payment?",
             "Most payments include principal, interest, property tax and homeowners insurance, often shortened to PITI. If you put down less than 20% on a conventional loan you also pay PMI, and condos or planned communities may add HOA dues."),
            ("How much should my down payment be?",
             "Twenty percent avoids PMI on a conventional loan, but many buyers put down 3% to 10%. FHA loans allow 3.5% down with a credit score of 580 or higher. A smaller down payment means a larger loan, a higher payment and PMI until you reach 20% equity."),
            ("How do I remove PMI?",
             "On conventional loans you can ask your lender to cancel PMI once your balance reaches 80% of the home's original value, and it ends automatically at 78%. Extra principal payments or a new appraisal after your home gains value can get you there sooner."),
            ("Is a 15-year or 30-year mortgage better?",
             "A 15-year loan has a lower rate and far less total interest, but a higher monthly payment. A 30-year loan keeps the payment lower and leaves room in your budget. You can also take a 30-year loan and make extra payments when you can."),
            ("Why is my estimate different from my lender's quote?",
             "Lenders use your actual property tax bill, insurance quote, credit score and loan program. Closing costs, points and escrow cushions can also change the first payments. Use this calculator to compare scenarios, then confirm numbers with a Loan Estimate."),
        ],
    },
    "home-affordability-calculator.html": {
        "examples": """
<h3>Example: $90,000 income with a car payment</h3>
<p>A household earning $90,000 a year has $7,500 a month before taxes. The 28% housing limit allows $2,100 a month. With a $400 car payment, the 36% total debt limit allows $2,300 for housing, so the lower $2,100 applies. With $40,000 down, a 6.75% rate, 1.1% property tax and $1,600 a year in insurance, that supports a home price of about $300,700 and a loan of about $260,700.</p>
<p>If the car loan were paid off, the debt limit would rise to $2,700, but the 28% housing limit would still cap the budget. Raising the down payment or finding a lower rate are the main ways to afford more in this case.</p>
""",
        "faq": [
            ("How much house can I afford on my salary?",
             "A common guideline is a home price of about 3 to 4 times your annual income, but your debts, down payment and interest rate matter more. This calculator applies the 28/36 rule lenders use to turn your actual numbers into a price."),
            ("What is the 28/36 rule?",
             "Lenders prefer that housing costs stay under 28% of your gross monthly income and that all debt payments, including housing, stay under 36%. Some programs allow a total of 43% or more with strong credit or cash reserves."),
            ("Does the calculator include closing costs?",
             "No. Closing costs usually run 2% to 5% of the price and are paid in cash at closing, separate from the down payment. Keep that money aside, along with an emergency fund, before you settle on a price."),
            ("Should I buy at the top of my budget?",
             "Not necessarily. The maximum a lender approves leaves little room for repairs, savings or a change in income. Many buyers aim below the limit so the payment stays comfortable."),
        ],
    },
    "auto-loan-calculator.html": {
        "examples": """
<h3>Example: a $35,000 car with a trade-in</h3>
<p>You trade in a car worth $5,000 and put $3,000 down. Sales tax of 7% applies to $30,000 after the trade-in, adding $2,100, and title and registration fees add $700. The amount financed is $29,800. At 6.9% for 60 months the payment is $588.67 and total interest is about $5,520.</p>
<p>Stretching the same loan to 72 months lowers the payment to $506.63, but interest rises to about $6,680, and you stay in debt a year longer.</p>
""",
        "faq": [
            ("What is a good interest rate on a car loan?",
             "Rates depend on your credit score, the loan term and whether the car is new or used. Borrowers with excellent credit often get rates under 7% on new cars, while fair or poor credit can mean rates well above 12%. Credit unions and manufacturer offers are worth checking."),
            ("How long should a car loan be?",
             "Sixty months or less is a common target. Longer terms lower the payment but cost more interest, and the car may be worth less than you owe for years. If you need 72 or 84 months to afford the payment, consider a less expensive car."),
            ("Is sales tax included in the loan?",
             "Often, yes. Many buyers roll sales tax and fees into the loan, which this calculator does. Paying them in cash lowers the amount financed and the interest you pay."),
            ("How does a trade-in lower my cost?",
             "The trade-in value is subtracted from the price, and in most states sales tax is charged only on the difference. If you still owe money on the trade-in, that balance is added to the new loan."),
        ],
    },
    "personal-loan-calculator.html": {
        "examples": """
<h3>Example: comparing two $10,000 offers</h3>
<p>Offer A has an 11% rate and a 6% origination fee over 36 months. The payment is $327.39 and interest totals about $1,790, but the $600 fee is taken out up front, so you receive $9,400. The true APR is about 15.3%.</p>
<p>Offer B has a 13% rate with no fee. The payment is $336.94 and interest is about $2,130, but you receive the full $10,000, so the APR is 13%. Offer B costs less overall even though its rate looks higher.</p>
""",
        "faq": [
            ("What is an origination fee?",
             "It is a one-time fee, usually 1% to 10% of the loan, that many online lenders charge. It is normally subtracted from the money you receive, so you repay the full loan amount while getting less cash."),
            ("What is the difference between interest rate and APR?",
             "The interest rate determines your monthly payment. The APR also includes fees, so it shows the real yearly cost of borrowing. Use the APR to compare offers from different lenders."),
            ("How much should I borrow if there is a fee?",
             "If you need a specific amount in hand, divide it by one minus the fee rate. To receive $10,000 with a 6% fee, you would borrow about $10,640."),
            ("Does paying off a personal loan early save money?",
             "Yes, because interest is charged on the remaining balance. Most personal lenders do not charge prepayment penalties, but check your loan agreement first."),
        ],
    },
    "credit-card-payoff-calculator.html": {
        "examples": """
<h3>Example: $5,000 at 24% APR</h3>
<p>Paying $150 a month clears the balance in 56 months, almost five years, and costs about $3,320 in interest. Raising the payment to $250 cuts the time to 26 months and interest to about $1,450, saving nearly $1,900.</p>
<p>To be debt-free in 18 months, you would need to pay $333.51 a month.</p>
""",
        "faq": [
            ("Why does my balance go down so slowly?",
             "At a high APR, a large part of each payment goes to interest. On a $5,000 balance at 24%, interest is about $100 in the first month, so a $150 payment reduces the balance by only $50."),
            ("Should I pay off the highest interest card first?",
             "Paying the highest APR first, called the avalanche method, saves the most money. Paying the smallest balance first, the snowball method, gives quicker wins and can help you stay motivated. Both work if you keep paying more than the minimum."),
            ("Is a balance transfer worth it?",
             "It can be. A 0% intro APR card stops interest for 12 to 21 months, usually for a 3% to 5% fee. Divide the balance by the number of intro months to see the payment needed to clear it before the regular rate starts."),
            ("How is credit card interest calculated?",
             "Card issuers divide the APR by 365 to get a daily rate and apply it to your average daily balance. This calculator uses a monthly rate of APR divided by 12, which gives very close results."),
        ],
    },
    "debt-to-income-calculator.html": {
        "examples": """
<h3>Example: $6,000 monthly income</h3>
<p>Rent is $1,600, a car loan is $400, student loans are $250 and card minimums are $100, for $2,350 in monthly debt. Dividing by $6,000 gives a DTI of 39.2%. The housing ratio is 26.7%, inside the 28% guideline, but total debt is above 36%. Paying off the $400 car loan would bring the DTI down to 32.5%.</p>
""",
        "faq": [
            ("What DTI do I need for a mortgage?",
             "Most conventional loans look for 36% or less and accept up to about 45% with strong credit. FHA loans can allow up to 50% in some cases. Lower is always better for approval and rates."),
            ("Does DTI affect my credit score?",
             "No. Credit scores do not use income, so DTI is not part of your score. Lenders calculate it separately when you apply. Credit card utilization, which compares balances to limits, does affect your score."),
            ("Should I use gross or net income?",
             "Use gross income, before taxes and deductions. That is what lenders use. If you are self-employed, lenders usually average your net business income from the last two tax returns."),
            ("How can I lower my DTI quickly?",
             "Pay off small loans entirely, since that removes a whole payment. Paying down credit cards lowers the minimum payment. Adding income, such as a co-borrower's salary, also lowers the ratio."),
        ],
    },
    "paycheck-calculator.html": {
        "examples": """
<h3>Example: $60,000 salary paid every two weeks</h3>
<p>A single filer contributes 5% ($3,000 a year) to a traditional 401(k). Federal taxable income is $60,000 minus $3,000 minus the $16,100 standard deduction, or $40,900, which gives about $4,660 in federal income tax. Social Security takes $3,720 and Medicare $870. In Texas, with no state income tax, take-home pay is about $47,750 a year, or $1,836.54 per paycheck.</p>
<p>The same salary in Illinois, at a flat 4.95%, adds about $2,820 in state tax, so each paycheck drops to about $1,728.</p>
""",
        "faq": [
            ("Why is my paycheck different from this estimate?",
             "Your employer withholds based on your Form W-4, which may differ from your actual tax. Health, dental and other benefit deductions, local taxes and state disability insurance can also reduce your check."),
            ("What is the 2026 standard deduction?",
             "It is $16,100 for single filers, $32,200 for married couples filing jointly and $24,150 for heads of household. It is subtracted from your income before federal tax brackets apply."),
            ("Do 401(k) contributions reduce my taxes?",
             "Traditional 401(k) contributions reduce federal and most state income tax, but not Social Security or Medicare tax. Roth 401(k) contributions are taxed now and come out tax-free in retirement."),
            ("What is the difference between marginal and effective tax rate?",
             "Your marginal rate is the rate on your last dollar of income. Your effective rate is total tax divided by total income, which is always lower because the first dollars are taxed at lower rates."),
            ("Which states have no income tax?",
             "Alaska, Florida, Nevada, New Hampshire, South Dakota, Tennessee, Texas, Washington and Wyoming do not tax wages. Washington taxes some capital gains."),
        ],
    },
    "salary-to-hourly-calculator.html": {
        "examples": """
<h3>Example 1: $22 an hour, full time</h3>
<p>At 40 hours a week for 52 weeks, $22 an hour equals $45,760 a year, $3,813 a month and $1,760 every two weeks.</p>
<h3>Example 2: $72,000 salary</h3>
<p>Divided by 2,080 hours, a $72,000 salary equals $34.62 an hour. Paid every two weeks, each gross paycheck is $2,769.23.</p>
""",
        "faq": [
            ("How many work hours are in a year?",
             "A full-time schedule of 40 hours a week for 52 weeks is 2,080 hours. With two weeks of unpaid time off it is 2,000 hours. Paid holidays and vacation still count as paid hours."),
            ("Is biweekly the same as twice a month?",
             "No. Biweekly pay comes every two weeks, which is 26 paychecks a year, so two months each year have three paydays. Twice-monthly pay is 24 paychecks, usually on the 15th and the last day of the month."),
            ("How do I compare a salary job with an hourly job?",
             "Convert both to an annual figure, then add the value of benefits such as health insurance, retirement match and paid time off. Hourly jobs may also pay overtime at 1.5 times the regular rate after 40 hours a week."),
            ("Are these amounts before or after taxes?",
             "They are gross amounts before taxes and deductions. Use the paycheck calculator to estimate take-home pay."),
        ],
    },
    "401k-calculator.html": {
        "examples": """
<h3>Example: starting at 35 with $25,000 saved</h3>
<p>You earn $60,000, get 3% raises, contribute 10% and your employer matches 50% up to 6% of pay. With a 7% annual return, your balance at 65 could reach about $1.24 million. Your own contributions total about $285,500 and your employer adds about $85,600; the rest is investment growth.</p>
<p>Contributing only 3% instead gives about $552,500 at 65, because both your deposits and the match are smaller. Contributing at least enough to get the full match is the single biggest step.</p>
""",
        "faq": [
            ("How much can I contribute to a 401(k) in 2026?",
             "The employee limit is $24,500. Workers aged 50 and older can add $8,000, and those aged 60 to 63 can add $11,250 instead. Employer contributions do not count toward your personal limit."),
            ("What return should I assume?",
             "Many planners use 5% to 7% a year for a diversified stock and bond portfolio before inflation. Returns vary a lot from year to year, so it helps to test a lower rate as well."),
            ("What does an employer match mean?",
             "Your employer adds money based on what you contribute. A 50% match up to 6% of pay means that if you put in 6%, your employer adds 3%. Contributing less than the match limit leaves free money on the table."),
            ("Should I choose a traditional or Roth 401(k)?",
             "Traditional contributions lower your taxes now and are taxed when you withdraw. Roth contributions are taxed now and are tax-free in retirement. If you expect a higher tax rate later, Roth often makes sense."),
            ("What does today's dollars mean?",
             "It adjusts the future balance for 2.5% yearly inflation, showing what that amount would buy at today's prices."),
        ],
    },
    "compound-interest-calculator.html": {
        "examples": """
<h3>Example: $5,000 plus $200 a month at 6%</h3>
<p>Starting with $5,000 and adding $200 every month at 6% compounded monthly, you would have about $160,900 after 25 years. You deposit $65,000, so about $95,900 is interest.</p>
<p>After 15 years the same plan holds about $70,400, of which $29,400 is interest. The last ten years add more than twice as much as the first fifteen, which is compounding at work.</p>
""",
        "faq": [
            ("What is compound interest?",
             "It is interest earned on both your deposits and on interest already earned. Over time the interest itself grows, so balances rise faster the longer money stays invested."),
            ("Does compounding frequency matter?",
             "A little. Daily compounding earns slightly more than monthly or yearly at the same rate, but the difference is small. The rate, the amount you add and the number of years matter far more."),
            ("What is the difference between APR and APY?",
             "APR is the simple yearly rate. APY includes the effect of compounding, so it is slightly higher. Savings accounts usually advertise APY."),
            ("Where can I earn compound interest?",
             "High-yield savings accounts, certificates of deposit, money market funds and bonds pay interest. Stock investments grow when dividends are reinvested and prices rise, which works in a similar way over the long term."),
        ],
    },
    "savings-goal-calculator.html": {
        "examples": """
<h3>Example 1: $20,000 down payment in 3 years</h3>
<p>You already have $2,000 and keep your savings in an account paying 4% APY. You need to save $465.38 a month. Without any interest you would need $500 a month.</p>
<h3>Example 2: a $10,000 emergency fund in 2 years</h3>
<p>Starting from zero at 4.5% APY, you need to save $399.33 a month.</p>
""",
        "faq": [
            ("How much should I keep in an emergency fund?",
             "A common target is three to six months of essential expenses. People with irregular income or a single household income often aim for more."),
            ("Where should I keep money for a short-term goal?",
             "For goals under five years, a high-yield savings account, money market account or CDs keep the money safe and earn interest. Stocks can fall right when you need the money."),
            ("What if I cannot save the full monthly amount?",
             "Extend the deadline, lower the goal, or start with a smaller amount and raise it when your income grows. Saving something every month builds the habit."),
            ("Does the calculator account for taxes on interest?",
             "No. Interest from savings accounts is taxable income, so your real growth will be slightly lower. The difference is small at typical savings rates."),
        ],
    },
}
