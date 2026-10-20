// APR: the rate at which the payments discount back to the cash actually received.
function trueApr(cash, pay, n) {
  if (cash <= 0 || pay * n <= cash) return 0;
  let lo = 0, hi = 2;
  for (let k = 0; k < 100; k++) {
    const mid = (lo + hi) / 2, r = mid / 12;
    const pv = pay * (1 - Math.pow(1 + r, -n)) / r;
    if (pv > cash) lo = mid; else hi = mid;
  }
  return lo * 100;
}
Calc.bind("form", () => {
  const { num, money, money2, set, payment } = Calc;
  const amount = num("amount"), rate = num("rate"), n = num("term");
  const fee = amount * num("fee") / 100;
  const monthly = payment(amount, rate, n), interest = monthly * n - amount;
  set("monthly", money2(monthly));
  set("principal", money(amount)); set("interest", money(interest)); set("feeOut", money(fee));
  set("cost", money(interest + fee));
  set("cash", money(amount - fee));
  set("apr", trueApr(amount - fee, monthly, n).toFixed(2) + "%");
  const sum = amount + interest + fee;
  document.getElementById("bar").innerHTML = sum > 0
    ? [[amount, "var(--accent)"], [interest, "#e0a64a"], [fee, "#c46b9a"]].map(([v, c]) => `<span style="width:${v / sum * 100}%;background:${c}"></span>`).join("") : "";
});
