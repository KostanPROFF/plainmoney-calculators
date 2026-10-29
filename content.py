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
    "bmi-calculator.html": {
        "examples": """
<h3>Example 1: 5 feet 4 inches and 145 pounds</h3>
<p>Height is 64 inches, so BMI is 703 &times; 145 / 64<sup>2</sup> = 24.9, at the top of the healthy range. For this height, a healthy weight runs from about 108 to 145 pounds.</p>
<h3>Example 2: 6 feet and 220 pounds</h3>
<p>At 72 inches, BMI is 703 &times; 220 / 72<sup>2</sup> = 29.8, which falls in the overweight range. The healthy range for this height is about 136 to 184 pounds, so reaching it means losing about 37 pounds.</p>
""",
        "faq": [
            ("What is a healthy BMI?",
             "For adults, the CDC defines a BMI from 18.5 to 24.9 as a healthy weight. Below 18.5 is underweight, 25 to 29.9 is overweight, and 30 or higher is obesity."),
            ("Is BMI accurate?",
             "BMI is a useful screening tool for groups of people, but it can mislead for individuals. It cannot tell muscle from fat, so muscular people may show a high BMI, and older adults with little muscle may show a normal BMI with excess fat."),
            ("Is BMI different for men and women?",
             "No. Adults use the same formula and the same categories regardless of sex. Women tend to carry more body fat than men at the same BMI, which is one of the limits of the measure."),
            ("Can children use this calculator?",
             "No. For children and teens aged 2 to 19, BMI is compared with others of the same age and sex using growth charts, so the adult categories do not apply."),
        ],
    },
    "calorie-calculator.html": {
        "examples": """
<h3>Example 1: a moderately active 40-year-old man</h3>
<p>A man who is 40 years old, 5 feet 10 inches tall and weighs 190 pounds has a BMR of about 1,780 calories. With exercise 3 to 5 days a week (factor 1.55), he burns about 2,760 calories a day. Eating about 2,260 calories a day would put him on track to lose about 1 pound a week.</p>
<h3>Example 2: a sedentary 28-year-old woman</h3>
<p>A woman who is 28, 5 feet 4 inches tall and weighs 140 pounds has a BMR of about 1,350 calories and maintains her weight on about 1,620 calories a day with little exercise. A 500-calorie deficit would drop her below 1,200 calories, so the calculator holds the target at 1,200. Adding activity is a safer way to widen the gap.</p>
""",
        "faq": [
            ("How many calories should I eat to lose weight?",
             "Start from the calories that maintain your weight and subtract 250 to 500 a day. That usually leads to a loss of about half a pound to 1 pound a week, a pace that is easier to keep up and preserves more muscle."),
            ("What is the difference between BMR and TDEE?",
             "BMR, basal metabolic rate, is what your body burns at complete rest to keep you alive. TDEE, total daily energy expenditure, adds digestion and every kind of movement, from walking around the house to workouts. Your diet should be planned around TDEE."),
            ("Which activity level should I choose?",
             "Pick the level that matches a typical week, not your best week. Most people with desk jobs who exercise a few times a week fit the light or moderate level. Overestimating activity is the most common reason weight loss stalls."),
            ("How accurate is the Mifflin-St Jeor equation?",
             "Studies find it is the most accurate of the common formulas for most adults, usually within about 10% of measured values. Treat the result as a starting point and adjust after two to three weeks based on how your weight actually changes."),
        ],
    },
    "due-date-calculator.html": {
        "examples": """
<h3>Example 1: a 28-day cycle</h3>
<p>If the first day of your last period was March 1, 2026, adding 280 days gives an estimated due date of December 6, 2026. Conception most likely happened around March 15.</p>
<h3>Example 2: a longer cycle</h3>
<p>With the same start date but a 33-day cycle, ovulation comes about 5 days later than in a 28-day cycle, so the due date moves to December 11, 2026.</p>
""",
        "faq": [
            ("How is my due date calculated?",
             "Your due date is 280 days, or 40 weeks, after the first day of your last menstrual period. If your cycle is longer or shorter than 28 days, the date moves by the same number of days."),
            ("Why am I counted as pregnant before conception?",
             "Doctors count from your last period because that date is usually known, while the exact day of conception rarely is. So in the first two weeks of the 40 you are not yet pregnant."),
            ("Can my due date change?",
             "Yes. An early ultrasound is the most accurate way to date a pregnancy, especially if your cycles are irregular or you are unsure of your last period. Your provider may update the due date after the first scan."),
            ("What if I conceived through IVF?",
             "With IVF the transfer date is known, so the due date is counted from it instead: about 261 days after a 5-day embryo transfer or 263 days after a 3-day transfer. Ask your clinic for your exact date."),
        ],
    },
    "percentage-calculator.html": {
        "examples": """
<h3>Example 1: a sale price</h3>
<p>A $79.99 jacket is 25% off. The discount is 79.99 &times; 25 / 100 = $20.00, so you pay $59.99.</p>
<h3>Example 2: a raise</h3>
<p>Your salary goes from $52,000 to $55,640. The increase is $3,640, and 3,640 / 52,000 &times; 100 = a 7% raise.</p>
<h3>Example 3: a test score</h3>
<p>You answered 42 of 48 questions correctly. 42 / 48 &times; 100 = 87.5%.</p>
""",
        "faq": [
            ("How do I calculate a percentage of a number?",
             "Convert the percent to a decimal by dividing by 100, then multiply. For 20% of 150, multiply 150 by 0.20 to get 30."),
            ("How do I calculate percent increase?",
             "Subtract the original value from the new value, divide by the original value and multiply by 100. A price that goes from $40 to $50 rose by 10 / 40 &times; 100 = 25%."),
            ("Why does a 50% drop need a 100% gain to recover?",
             "Percent change is measured from the starting value. If $100 falls 50% to $50, getting back to $100 means adding $50, which is 100% of the new $50 base."),
            ("How do I add a percentage to a number?",
             "Multiply by 1 plus the percent as a decimal. To add 8% sales tax to $25, multiply 25 by 1.08 to get $27."),
        ],
    },
    "tip-calculator.html": {
        "examples": """
<h3>Example 1: dinner for four</h3>
<p>The bill is $68.40 and you tip 20%. The tip is $13.68, the total is $82.08, and each of the four people pays $20.52.</p>
<p>If everyone rounds up to $21, the group pays $84.00, which works out to a tip of about 22.8%.</p>
<h3>Example 2: a $112 bill at 15%</h3>
<p>A 15% tip is $16.80, for a total of $128.80.</p>
""",
        "faq": [
            ("Should I tip on the bill before or after tax?",
             "Etiquette guides say to tip on the pre-tax amount, which is what this calculator expects. Tipping on the total after tax is also common and simply adds a little more for the server."),
            ("How much should I tip at a restaurant?",
             "In the US, 15% to 20% is standard for sit-down service, with 20% now common for good service. Servers often earn a lower base wage and rely on tips for most of their income."),
            ("Do I need to tip if a service charge is included?",
             "Check the receipt. Many restaurants add an automatic gratuity of about 18% for large groups. If it is there, no additional tip is expected unless the service was exceptional."),
            ("How do I split a bill with a different tip for each person?",
             "Run the calculator once for each person's share of the bill with their chosen tip and a party size of one. For equal shares, enter the full bill and the number of people."),
        ],
    },
    "age-calculator.html": {
        "examples": """
<h3>Example: born December 3, 1985</h3>
<p>On October 29, 2026, this person is 40 years, 10 months and 26 days old. Their 41st birthday is 35 days away.</p>
<p>The last full month ended on October 3, so the remaining 26 days are counted from that date.</p>
""",
        "faq": [
            ("How do I calculate my age?",
             "Subtract your birth year from the current year, then subtract one if your birthday has not happened yet this year. For months and days, count the full months since your last birthday and then the remaining days."),
            ("How many days old am I?",
             "Enter your date of birth and the calculator shows your age in days, counting leap years. Someone who has just turned 30 has lived about 10,957 days."),
            ("Can I find someone's age on a past or future date?",
             "Yes. Change the second date to any day, such as a wedding date or a future retirement date, to see the age on that day."),
            ("What day of the week was I born?",
             "The calculator shows it under the results. It uses the standard Gregorian calendar used in the US since 1752."),
        ],
    },
    "gpa-calculator.html": {
        "examples": """
<h3>Example: a 12-credit semester</h3>
<p>You take four classes: an A in a 4-credit class (16 points), a B+ in a 3-credit class (9.9 points), an A- in a 3-credit class (11.1 points) and a C in a 2-credit class (4 points). That is 41 grade points over 12 credits, a semester GPA of 3.42.</p>
<p>If you came into the semester with a 3.20 GPA over 45 credits, you had 144 grade points. The new cumulative GPA is (144 + 41) / 57 = 3.25.</p>
""",
        "faq": [
            ("What is a good GPA?",
             "A 3.0 is a common minimum for scholarships and many graduate programs, and 3.5 or higher is considered strong. Competitive programs and employers in some fields look for 3.7 and up."),
            ("How do I raise my GPA?",
             "Classes with more credit hours move your GPA the most, so focus on doing well in them. The more credits you have already completed, the more slowly your cumulative GPA changes, so early semesters matter a lot."),
            ("Does a pass/fail class count toward GPA?",
             "Usually not. Pass, credit or satisfactory grades give credit hours but no grade points, so leave those classes out. A failed pass/fail class may count as an F at some schools."),
            ("What if my school uses a different scale?",
             "Some schools count an A+ as 4.3 or do not use minus grades. Check your registrar's grading table and adjust the grades you enter, since this calculator uses the most common 4.0 scale."),
        ],
    },
}
