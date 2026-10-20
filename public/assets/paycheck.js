// 2026 federal figures (IRS Rev. Proc. 2025-32, SSA 2026 COLA release).
const FED_2026 = {
  single: { std: 16100, brackets: [[12400, .10], [50400, .12], [105700, .22], [201775, .24], [256225, .32], [640600, .35], [Infinity, .37]], addlMed: 200000 },
  mfj:    { std: 32200, brackets: [[24800, .10], [100800, .12], [211400, .22], [403550, .24], [512450, .32], [768700, .35], [Infinity, .37]], addlMed: 250000 },
  hoh:    { std: 24150, brackets: [[17700, .10], [67450, .12], [105700, .22], [201750, .24], [256200, .32], [640600, .35], [Infinity, .37]], addlMed: 200000 },
};
const SS_WAGE_BASE = 184500;
const NO_TAX = ["AK", "FL", "NV", "NH", "SD", "TN", "TX", "WA", "WY"];
// Flat-rate states (approximate 2026 rates; verify before launch).
const FLAT = { AZ: 2.5, CO: 4.4, GA: 5.19, ID: 5.3, IL: 4.95, IN: 2.95, IA: 3.8, KY: 3.5, LA: 3.0, MI: 4.25, MS: 4.0, NC: 3.99, PA: 3.07, UT: 4.5 };
// Graduated-bracket states: rough effective rate for a middle income, to be replaced by real brackets.
const APPROX = { AL: 4.0, AR: 3.5, CA: 5.0, CT: 4.5, DE: 4.8, DC: 5.5, HI: 6.0, KS: 4.5, ME: 5.0, MD: 4.7, MA: 5.0, MN: 5.5, MO: 4.0, MT: 4.5, NE: 4.5, NJ: 3.5, NM: 3.5, NY: 5.0, ND: 1.5, OH: 2.5, OK: 3.8, OR: 7.5, RI: 4.0, SC: 4.5, VT: 4.5, VA: 4.8, WV: 4.0, WI: 4.8 };

function stateDefault(st) {
  if (NO_TAX.includes(st)) return [0, "This state has no income tax on wages."];
  if (st in FLAT) return [FLAT[st], "Flat-rate state: one rate applies to all taxable income."];
  return [APPROX[st] ?? 4.5, "This state uses graduated brackets. The rate shown is an approximate effective rate; edit it if you know yours."];
}

const stateSel = document.getElementById("state");
stateSel.addEventListener("change", () => {
  document.getElementById("stateRate").value = stateDefault(stateSel.value)[0];
});
document.getElementById("stateRate").value = stateDefault(stateSel.value)[0];

Calc.bind("form", () => {
  const { num, money, money2, set } = Calc;
  const salary = num("salary"), freq = num("freq");
  const cfg = FED_2026[document.getElementById("status").value];
  const k401 = Math.min(salary * num("k401") / 100, 24500);
  const health = num("health") * freq;
  const fedTaxable = Math.max(0, salary - k401 - health - cfg.std);
  let fed = 0, prev = 0, marg = .10;
  for (const [top, rate] of cfg.brackets) {
    if (fedTaxable > prev) { fed += (Math.min(fedTaxable, top) - prev) * rate; marg = rate; }
    prev = top;
  }
  const ficaWages = Math.max(0, salary - health); // 401(k) deferrals are still subject to FICA
  const ss = Math.min(ficaWages, SS_WAGE_BASE) * .062;
  const med = ficaWages * .0145 + Math.max(0, ficaWages - cfg.addlMed) * .009;
  const st = Math.max(0, salary - k401 - health) * num("stateRate") / 100;
  const pre = k401 + health;
  const net = salary - fed - ss - med - st - pre;
  const per = (v) => money2(v / freq);

  set("net", per(net)); set("net2", per(net));
  set("gross", per(salary)); set("fed", per(fed)); set("ss", per(ss)); set("med", per(med));
  set("st", per(st)); set("pre", per(pre));
  set("annualNet", money(net));
  set("eff", salary > 0 ? ((fed + ss + med + st) / salary * 100).toFixed(1) + "%" : "-");
  set("marg", (marg * 100).toFixed(0) + "%");
  set("stateNote", stateDefault(stateSel.value)[1] + " Local taxes are not included.");
  const parts = [[net, "var(--accent)"], [fed, "#5b8def"], [ss, "#e0a64a"], [med, "#c46b9a"], [st, "#8a6fd1"], [pre, "#8a8f8c"]];
  document.getElementById("bar").innerHTML = salary > 0
    ? parts.map(([v, c]) => `<span style="width:${Math.max(v, 0) / salary * 100}%;background:${c}"></span>`).join("") : "";
});
