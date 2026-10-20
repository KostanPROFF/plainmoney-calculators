Calc.bind("form", () => {
  const { num, money, set, areaChart } = Calc;
  const initial = num("initial"), monthly = num("monthly"), rate = num("rate") / 100;
  const years = Math.max(0, Math.min(100, Math.round(num("years"))));
  const n = num("comp");
  // Convert the nominal rate to an equivalent monthly growth factor for the chosen compounding.
  const monthlyFactor = Math.pow(1 + rate / n, n / 12);
  let bal = initial, dep = initial, rows = "";
  const xs = [0], sDep = [initial], sInt = [0];
  for (let y = 1; y <= years; y++) {
    const startBal = bal, startDep = dep;
    for (let m = 0; m < 12; m++) { bal = bal * monthlyFactor + monthly; dep += monthly; }
    const yInt = bal - startBal - (dep - startDep);
    rows += `<tr><td>${y}</td><td>${money(dep)}</td><td>${money(yInt)}</td><td>${money(bal)}</td></tr>`;
    xs.push(y); sDep.push(dep); sInt.push(bal - dep);
  }
  set("final", money(bal));
  set("dep", money(dep));
  set("int", money(bal - dep));
  document.getElementById("sched").innerHTML = rows;
  areaChart(document.getElementById("chart"), xs, [
    { values: sDep, color: "#5b8def" },
    { values: sInt, color: "var(--accent)" },
  ]);
});
