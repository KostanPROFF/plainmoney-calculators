// 2026 limits: $24,500 deferral, $8,000 catch-up at 50+, $11,250 at ages 60-63.
function limitFor(age) {
  if (age >= 60 && age <= 63) return 24500 + 11250;
  if (age >= 50) return 24500 + 8000;
  return 24500;
}

Calc.bind("form", () => {
  const { num, money, set, areaChart } = Calc;
  const age = Math.round(num("age")), retire = Math.round(num("retire"));
  let salary = num("salary"), bal = num("balance");
  const pct = num("contrib") / 100, raise = num("raise") / 100, ret = num("ret") / 100;
  const matchRate = num("match") / 100, matchCap = num("matchCap") / 100;
  const years = Math.max(0, retire - age);
  const start = bal;
  let you = 0, emp = 0, capped = false;
  const xs = [age], sYou = [0], sEmp = [0], sStart = [start], sGrowth = [0];

  for (let y = 0; y < years; y++) {
    const yourC = Math.min(salary * pct, limitFor(age + y));
    if (salary * pct > limitFor(age + y)) capped = true;
    const empC = Math.min(yourC, salary * matchCap) * matchRate;
    // Contributions spread through the year earn about half a year of growth.
    bal = bal * (1 + ret) + (yourC + empC) * (1 + ret / 2);
    you += yourC; emp += empC;
    salary *= 1 + raise;
    xs.push(age + y + 1); sStart.push(start); sYou.push(you); sEmp.push(emp);
    sGrowth.push(Math.max(0, bal - start - you - emp));
  }
  const growth = bal - start - you - emp;
  set("atLabel", `Balance at age ${retire}`);
  set("final", money(bal));
  set("you", money(you + start));
  set("emp", money(emp));
  set("growth", money(growth));
  set("real", money(bal / Math.pow(1.025, years)));
  set("limitNote", capped
    ? "Your contribution hit the IRS annual limit in some years, so it was capped."
    : "Starting balance is counted with your contributions.");
  areaChart(document.getElementById("chart"), xs, [
    { values: sStart.map((v, i) => v + sYou[i]), color: "#5b8def" },
    { values: sEmp, color: "#e0a64a" },
    { values: sGrowth, color: "var(--accent)" },
  ]);
});
