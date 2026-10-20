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
  return [y ? `${y} yr` : "", mo ? `${mo} mo` : ""].filter(Boolean).join(" ") || "0 mo";
}
Calc.bind("form", () => {
  const { num, money, money2, set, payment } = Calc;
  const bal = num("balance"), apr = num("apr"), pay = num("payment"), goal = Math.max(1, Math.round(num("goal")));
  const res = payoff(bal, apr, pay);
  if (res) {
    const d = new Date(); d.setMonth(d.getMonth() + res.months);
    set("time", duration(res.months));
    set("date", d.toLocaleDateString("en-US", { month: "short", year: "numeric" }));
    set("interest", money(res.interest)); set("total", money(bal + res.interest));
    set("warn", "");
  } else {
    set("time", "Never"); set("date", "-"); set("interest", "-"); set("total", "-");
    set("warn", `Your payment does not cover the monthly interest of ${money2(bal * apr / 1200)}. The balance will keep growing.`);
  }
  const gp = payment(bal, apr, goal);
  set("goalLabel", `Payment to finish in ${goal} months`);
  set("goalPay", money2(gp));
  set("goalInt", money(gp * goal - bal));
  const steps = [...new Set([pay, pay + 50, pay + 100, pay + 200, gp].map((v) => Math.round(v)))].sort((a, b) => a - b);
  document.getElementById("compare").innerHTML = steps.map((p) => {
    const r = payoff(bal, apr, p);
    return `<tr><td>${money(p)}</td><td>${r ? r.months : "Never"}</td><td>${r ? money(r.interest) : "-"}</td></tr>`;
  }).join("");
});
