Calc.bind("form", () => {
  const { num, money, money2, set, payment } = Calc;
  const monthlyIncome = num("income") / 12, debts = num("debts"), down = num("down");
  const rate = num("rate"), months = num("term") * 12;
  const taxM = num("taxRate") / 100 / 12, insHoa = num("insurance") / 12 + num("hoa");
  const [frontPct, backPct] = num("rule") === 43 ? [0.31, 0.43] : [0.28, 0.36];
  const front = monthlyIncome * frontPct, back = monthlyIncome * backPct - debts;
  const housing = Math.max(0, Math.min(front, back));
  // housing = (price - down) * f + price * taxM + insHoa  ->  solve for price
  const f = payment(1, rate, months);
  const price = Math.max(0, (housing - insHoa + down * f) / (f + taxM));
  const loan = Math.max(0, price - down);
  const pi = payment(loan, rate, months), tax = price * taxM;
  set("price", money(price));
  set("loan", money(loan));
  set("downPct", price > 0 ? (down / price * 100).toFixed(1) + "%" : "-");
  set("monthly", money2(pi + tax + insHoa));
  set("pi", money2(pi)); set("tax", money2(tax)); set("ins", money2(insHoa));
  const limiting = back < front ? `your other debts (total debt capped at ${Math.round(backPct * 100)}% of income)` : `the housing limit (${Math.round(frontPct * 100)}% of income)`;
  set("limitNote", housing <= insHoa
    ? "Your debts leave no room for a housing payment at this income. Try paying down debt first."
    : `Limited by ${limiting}.` + (down / price < 0.2 ? " With under 20% down, expect PMI on top." : ""));
});
