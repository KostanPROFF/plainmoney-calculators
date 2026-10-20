Calc.bind("form", () => {
  const { num, money, money2, set, areaChart } = Calc;
  const goal = num("goal"), current = num("current");
  const n = Math.max(1, Math.round(num("years") * 12));
  const r = Math.pow(1 + num("rate") / 100, 1 / 12) - 1; // APY to monthly rate
  const grow = Math.pow(1 + r, n);
  const needed = goal - current * grow;
  const pmt = needed <= 0 ? 0 : r === 0 ? needed / n : needed * r / (grow - 1);
  const deposits = current + pmt * n;
  set("monthly", money2(pmt));
  set("dep", money(deposits));
  set("int", money(Math.max(0, (needed <= 0 ? current * grow : goal) - deposits)));
  set("noInt", money2(Math.max(0, (goal - current) / n)) + "/mo");
  set("note", needed <= 0 ? "Your current savings will reach the goal on their own with interest." : "");
  // Monthly series, sampled to at most ~60 points for the chart.
  const xs = [], sDep = [], sInt = [];
  let bal = current, dep = current;
  const step = Math.max(1, Math.ceil(n / 60));
  for (let m = 0; m <= n; m++) {
    if (m > 0) { bal = bal * (1 + r) + pmt; dep += pmt; }
    if (m % step === 0 || m === n) { xs.push(m < 12 ? `${m}m` : `${(m / 12).toFixed(m % 12 ? 1 : 0)}y`); sDep.push(dep); sInt.push(bal - dep); }
  }
  areaChart(document.getElementById("chart"), xs, [
    { values: sDep, color: "#5b8def" },
    { values: sInt, color: "var(--accent)" },
  ]);
});
