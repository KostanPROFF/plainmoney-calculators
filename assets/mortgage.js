Calc.bind("form", () => {
  const { num, money, money2, set, payment } = Calc;
  const price = num("price"), downPct = num("downPct"), rate = num("rate");
  const years = num("term"), months = years * 12;
  const loan = Math.max(0, price * (1 - downPct / 100));
  const pi = payment(loan, rate, months);
  const tax = (price * num("taxRate")) / 100 / 12;
  const ins = num("insurance") / 12;
  const hoa = num("hoa");
  const needsPmi = downPct < 20 && loan > 0;
  const pmi = needsPmi ? (loan * num("pmiRate")) / 100 / 12 : 0;
  const total = pi + tax + ins + pmi + hoa;

  // Amortize month by month; PMI stops once balance reaches 80% of price.
  const r = rate / 100 / 12;
  let bal = loan, totalInt = 0, pmiMonths = 0, rows = "";
  let yP = 0, yI = 0;
  for (let m = 1; m <= months && bal > 0.005; m++) {
    const i = bal * r;
    const p = Math.min(pi - i, bal);
    if (needsPmi && bal > price * 0.8) pmiMonths++;
    bal -= p; totalInt += i; yP += p; yI += i;
    if (m % 12 === 0 || bal <= 0.005) {
      rows += `<tr><td>${Math.ceil(m / 12)}</td><td>${money(yP)}</td><td>${money(yI)}</td><td>${money(Math.max(bal, 0))}</td></tr>`;
      yP = yI = 0;
    }
  }
  const end = new Date(); end.setMonth(end.getMonth() + months);

  set("total", money2(total));
  set("pi", money2(pi)); set("tax", money2(tax)); set("ins", money2(ins));
  set("pmi", money2(pmi)); set("hoaOut", money2(hoa));
  set("loan", money(loan)); set("interest", money(totalInt));
  set("payoff", end.toLocaleDateString("en-US", { month: "short", year: "numeric" }));
  set("pmiNote", needsPmi
    ? `PMI applies because your down payment is under 20%. It drops off after about ${Math.round(pmiMonths / 12 * 10) / 10} years, when your loan reaches 80% of the home price.`
    : "No PMI: your down payment is 20% or more.");
  document.getElementById("sched").innerHTML = rows;
  const parts = [[pi, "var(--accent)"], [tax, "#5b8def"], [ins, "#e0a64a"], [pmi, "#c46b9a"], [hoa, "#8a8f8c"]];
  document.getElementById("bar").innerHTML = total > 0
    ? parts.map(([v, c]) => `<span style="width:${(v / total) * 100}%;background:${c}"></span>`).join("") : "";
});
