Calc.bind("form", () => {
  const { num, money, money2, set, payment, t } = Calc;
  const price = num("price"), down = num("down"), trade = num("trade"), owed = num("owed");
  const taxRate = num("taxRate"), fees = num("fees"), rate = num("rate"), term = num("term");
  const tax = Math.max(0, price - trade) * taxRate / 100;
  const financed = Math.max(0, price + tax + fees - down - trade + owed);
  const monthly = payment(financed, rate, term);
  const interest = monthly * term - financed;

  set("monthly", money2(monthly));
  set("financed", money(financed));
  set("interest", money(interest));
  set("tax", money(tax));
  set("totalCost", money(price + tax + fees + interest + owed));
  const sum = financed + interest;
  document.getElementById("bar").innerHTML = sum > 0
    ? `<span style="width:${financed / sum * 100}%;background:var(--accent)"></span><span style="width:${interest / sum * 100}%;background:#e0a64a"></span>` : "";
  document.getElementById("compare").innerHTML = [36, 48, 60, 72, 84].map((term_) => {
    const m = payment(financed, rate, term_);
    const cur = term_ === term ? ' style="font-weight:700"' : "";
    return `<tr${cur}><td>${t("{n} months", { n: term_ })}</td><td>${money2(m)}</td><td>${money(m * term_ - financed)}</td></tr>`;
  }).join("");
});
