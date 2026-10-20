// Months and interest to clear `bal` paying `pay` monthly; null if the payment never covers interest.
function payoff(bal, apr, pay) {
  const r = apr / 100 / 12;
  let m = 0, interest = 0;
  while (bal > 0.005) {
    const i = bal * r;
    if (pay <= i || m > 1200) return null;
    interest += i; bal = bal + i - pay; m++;
  }
  return { months: m, interest };
}
function duration(m) {
  const y = Math.floor(m / 12), mo = m % 12;
  const yr = y === 1 ? Calc.t("1 yr") : Calc.t("{n} yr", { n: y });
  const mos = mo === 1 ? Calc.t("1 mo") : Calc.t("{n} mo", { n: mo });
  return [y ? yr : "", mo ? mos : ""].filter(Boolean).join(" ") || Calc.t("{n} mo", { n: 0 });
}
Calc.bind("form", () => {
  const { num, money, money2, set, payment, t, date } = Calc;
  const bal = num("balance"), apr = num("apr"), pay = num("payment"), goal = Math.max(1, Math.round(num("goal")));
  const res = payoff(bal, apr, pay);
  if (res) {
    const d = new Date(); d.setMonth(d.getMonth() + res.months);
    set("time", duration(res.months));
    set("date", date(d));
    set("interest", money(res.interest)); set("total", money(bal + res.interest));
    set("warn", "");
  } else {
    set("time", t("Never")); set("date", "-"); set("interest", "-"); set("total", "-");
    set("warn", t("Your payment does not cover the monthly interest of {amount}. The balance will keep growing.", { amount: money2(bal * apr / 1200) }));
  }
  const gp = payment(bal, apr, goal);
  set("goalLabel", t("Payment to finish in {n} months", { n: goal }));
  set("goalPay", money2(gp));
  set("goalInt", money(gp * goal - bal));
  const steps = [...new Set([pay, pay + 50, pay + 100, pay + 200, gp].map((v) => Math.round(v)))].sort((a, b) => a - b);
  document.getElementById("compare").innerHTML = steps.map((p) => {
    const r = payoff(bal, apr, p);
    return `<tr><td>${money(p)}</td><td>${r ? r.months : t("Never")}</td><td>${r ? money(r.interest) : "-"}</td></tr>`;
  }).join("");
});
