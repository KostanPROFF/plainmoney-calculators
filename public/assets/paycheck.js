// 2026 federal figures (IRS Rev. Proc. 2025-32, SSA 2026 COLA release).
const FED_2026 = {
  single: { std: 16100, brackets: [[12400, .10], [50400, .12], [105700, .22], [201775, .24], [256225, .32], [640600, .35], [Infinity, .37]], addlMed: 200000 },
  mfj:    { std: 32200, brackets: [[24800, .10], [100800, .12], [211400, .22], [403550, .24], [512450, .32], [768700, .35], [Infinity, .37]], addlMed: 250000 },
  hoh:    { std: 24150, brackets: [[17700, .10], [67450, .12], [105700, .22], [201750, .24], [256200, .32], [640600, .35], [Infinity, .37]], addlMed: 200000 },
};
const SS_WAGE_BASE = 184500;
const NO_TAX = ["AK", "FL", "NV", "NH", "SD", "TN", "TX", "WA", "WY"];
// 2026 state income tax on wages (Tax Foundation, State Individual Income Tax Rates and Brackets, 2026).
// s / m: single and married-joint brackets as [income over, rate %] (m defaults to s). d: standard deduction and
// e: personal exemption, as [single, joint]; c: personal credit [single, joint]. ep: income range [from, to] over
// which the exemption phases out, [single, joint]. pre401k: false where 401(k) deferrals are still state-taxed.
// Head of household uses the single brackets. Local and city income taxes are left out.
const STATE_2026 = {
  AL: { s: [[0, 2], [500, 4], [3000, 5]], m: [[0, 2], [1000, 4], [6000, 5]], d: [3000, 8500], e: [1500, 3000] },
  AZ: { s: [[0, 2.5]], d: [8350, 16700] },
  AR: { s: [[0, 2], [4600, 3.9]], d: [2470, 4940], c: [29, 58] },
  CA: { s: [[0, 1], [11079, 2], [26264, 4], [41452, 6], [57542, 8], [72724, 9.3], [371479, 10.3], [445771, 11.3], [742953, 12.3], [1000000, 13.3]],
        m: [[0, 1], [22158, 2], [52528, 4], [82904, 6], [115084, 8], [145448, 9.3], [742958, 10.3], [891542, 11.3], [1000000, 12.3], [1485906, 13.3]],
        d: [5540, 11080], c: [153, 306] },
  CO: { s: [[0, 4.4]], d: [16100, 32200] },
  CT: { s: [[0, 2], [10000, 4.5], [50000, 5.5], [100000, 6], [200000, 6.5], [250000, 6.9], [500000, 6.99]],
        m: [[0, 2], [20000, 4.5], [100000, 5.5], [200000, 6], [400000, 6.5], [500000, 6.9], [1000000, 6.99]],
        e: [15000, 24000], ep: [[30000, 45000], [48000, 72000]] },
  DE: { s: [[2000, 2.2], [5000, 3.9], [10000, 4.8], [20000, 5.2], [25000, 5.55], [60000, 6.6]], d: [3250, 6500], c: [110, 220] },
  DC: { s: [[0, 4], [10000, 6], [40000, 6.5], [60000, 8.5], [250000, 9.25], [500000, 9.75], [1000000, 10.75]], d: [16100, 32200] },
  GA: { s: [[0, 5.19]], d: [12000, 24000] },
  HI: { s: [[0, 1.4], [9600, 3.2], [14400, 5.5], [19200, 6.4], [24000, 6.8], [36000, 7.2], [48000, 7.6], [125000, 7.9], [175000, 8.25], [225000, 9], [275000, 10], [325000, 11]],
        m: [[0, 1.4], [19200, 3.2], [28800, 5.5], [38400, 6.4], [48000, 6.8], [72000, 7.2], [96000, 7.6], [250000, 7.9], [350000, 8.25], [450000, 9], [550000, 10], [650000, 11]],
        d: [4400, 8800], e: [1144, 2288] },
  ID: { s: [[4811, 5.3]], m: [[9622, 5.3]], d: [16100, 32200] },
  IL: { s: [[0, 4.95]], e: [2925, 5850] },
  IN: { s: [[0, 2.95]], e: [1000, 2000] },
  IA: { s: [[0, 3.8]], d: [16100, 32200], c: [40, 80] },
  KS: { s: [[0, 5.2], [23000, 5.58]], m: [[0, 5.2], [46000, 5.58]], d: [3605, 8240], e: [9160, 18320] },
  KY: { s: [[0, 3.5]], d: [3360, 3360] },
  LA: { s: [[0, 3]], d: [12875, 25750] },
  ME: { s: [[0, 5.8], [27399, 6.75], [64849, 7.15]], m: [[0, 5.8], [54849, 6.75], [129749, 7.15]], d: [8350, 16700], e: [5300, 10600] },
  MD: { s: [[0, 2], [1000, 3], [2000, 4], [3000, 4.75], [100000, 5], [125000, 5.25], [150000, 5.5], [250000, 5.75], [500000, 6.25], [1000000, 6.5]],
        m: [[0, 2], [1000, 3], [2000, 4], [3000, 4.75], [150000, 5], [175000, 5.25], [225000, 5.5], [300000, 5.75], [600000, 6.25], [1200000, 6.5]],
        d: [3350, 6700], e: [3200, 6400] },
  MA: { s: [[0, 5], [1083150, 9]], e: [4400, 8800] },
  MI: { s: [[0, 4.25]], e: [5900, 11800] },
  MN: { s: [[0, 5.35], [33310, 6.8], [109430, 7.85], [203150, 9.85]], m: [[0, 5.35], [48700, 6.8], [193480, 7.85], [337930, 9.85]], d: [15300, 30600] },
  MS: { s: [[10000, 4]], d: [2300, 4600], e: [6000, 12000] },
  MO: { s: [[1348, 2], [2696, 2.5], [4044, 3], [5392, 3.5], [6740, 4], [8088, 4.5], [9436, 4.7]], d: [16100, 32200] },
  MT: { s: [[0, 4.7], [47500, 5.65]], m: [[0, 4.7], [95000, 5.65]], d: [16100, 32200] },
  NE: { s: [[0, 2.46], [4130, 3.51], [24760, 4.55]], m: [[0, 2.46], [8250, 3.51], [49530, 4.55]], d: [8850, 17700], c: [176, 352] },
  NJ: { s: [[0, 1.4], [20000, 1.75], [35000, 3.5], [40000, 5.53], [75000, 6.37], [500000, 8.97], [1000000, 10.75]],
        m: [[0, 1.4], [20000, 1.75], [50000, 2.45], [70000, 3.5], [80000, 5.53], [150000, 6.37], [500000, 8.97], [1000000, 10.75]],
        e: [1000, 2000], pre401k: false },
  NM: { s: [[0, 1.5], [5500, 3.2], [16500, 4.3], [33500, 4.7], [66500, 4.9], [210000, 5.9]], m: [[0, 1.5], [8000, 3.2], [25000, 4.3], [50000, 4.7], [100000, 4.9], [315000, 5.9]], d: [16100, 32200] },
  NY: { s: [[0, 3.9], [8500, 4.4], [11700, 5.15], [13900, 5.4], [80650, 5.9], [215400, 6.85], [1077550, 9.65], [5000000, 10.3], [25000000, 10.9]],
        m: [[0, 3.9], [17150, 4.4], [23600, 5.15], [27900, 5.4], [161550, 5.9], [323200, 6.85], [2155350, 9.65], [5000000, 10.3], [25000000, 10.9]],
        d: [8000, 16050] },
  NC: { s: [[0, 3.99]], d: [12750, 25500] },
  ND: { s: [[48475, 1.95], [244825, 2.5]], m: [[80975, 1.95], [298075, 2.5]], d: [16100, 32200] },
  OH: { s: [[26050, 2.75]], e: [2400, 4800] },
  OK: { s: [[3750, 2.5], [4900, 3.5], [7200, 4.5]], m: [[7500, 2.5], [9800, 3.5], [14400, 4.5]], d: [6350, 12700], e: [1000, 2000] },
  OR: { s: [[0, 4.75], [4550, 6.75], [11400, 8.75], [125000, 9.9]], m: [[0, 4.75], [9100, 6.75], [22800, 8.75], [250000, 9.9]], d: [2910, 5820], c: [256, 512] },
  PA: { s: [[0, 3.07]], pre401k: false },
  RI: { s: [[0, 3.75], [82050, 4.75], [186450, 5.99]], d: [11200, 22400], e: [5250, 10500] },
  SC: { s: [[3640, 3], [18230, 6]], d: [8350, 16700] },
  UT: { s: [[0, 4.5]] },
  VT: { s: [[0, 3.35], [49400, 6.6], [119700, 7.6], [249700, 8.75]], m: [[0, 3.35], [82500, 6.6], [199450, 7.6], [304000, 8.75]], d: [7650, 15300], e: [5300, 10600] },
  VA: { s: [[0, 2], [3000, 3], [5000, 5], [17000, 5.75]], d: [8750, 17500], e: [930, 1860] },
  WV: { s: [[0, 2.22], [10000, 2.96], [25000, 3.33], [40000, 4.44], [60000, 4.82]], e: [2000, 4000] },
  WI: { s: [[0, 3.5], [15110, 4.4], [51950, 5.3], [332720, 7.65]], m: [[0, 3.5], [20150, 4.4], [69260, 5.3], [443630, 7.65]], d: [13960, 25840], e: [700, 1400] },
};

// Tax on `taxable` for brackets given as [income over, rate %]; also returns the top rate reached.
function bracketTax(taxable, brackets) {
  let tax = 0, top = 0;
  brackets.forEach(([from, rate], i) => {
    const to = i + 1 < brackets.length ? brackets[i + 1][0] : Infinity;
    if (taxable > from) { tax += (Math.min(taxable, to) - from) * rate / 100; top = rate; }
  });
  return [tax, top];
}

// State income tax for a year of wages. `pre401k` and `health` are this year's pre-tax deductions.
function stateTax(st, status, wages, pre401k, health) {
  const c = STATE_2026[st];
  if (!c) return 0;
  const j = status === "mfj" ? 1 : 0;
  const agi = Math.max(0, wages - health - (c.pre401k === false ? 0 : pre401k));
  let exempt = c.e ? c.e[j] : 0;
  if (c.ep) {
    const [from, to] = c.ep[j];
    exempt *= Math.min(1, Math.max(0, (to - agi) / (to - from)));
  }
  const taxable = Math.max(0, agi - (c.d ? c.d[j] : 0) - exempt);
  const [tax] = bracketTax(taxable, (j && c.m) || c.s);
  return Math.max(0, tax - (c.c ? c.c[j] : 0));
}

function stateNote(st, status) {
  if (NO_TAX.includes(st)) return Calc.t("This state has no income tax on wages.");
  if (document.getElementById("stateRate").value.trim() !== "") return Calc.t("Using the state tax rate you entered.");
  const c = STATE_2026[st];
  const kind = c.s.length === 1 ? Calc.t("Flat-rate state: one rate applies to all taxable income.") : Calc.t("Uses this state's 2026 tax brackets, standard deduction and exemptions.");
  return kind + (status === "hoh" && c.m ? " " + Calc.t("Head of household is estimated with the single-filer brackets.") : "");
}

const stateSel = document.getElementById("state");

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
  const status = document.getElementById("status").value;
  const override = document.getElementById("stateRate").value.trim() !== "";
  const st = override ? Math.max(0, salary - k401 - health) * num("stateRate") / 100 : stateTax(stateSel.value, status, salary, k401, health);
  const pre = k401 + health;
  const net = salary - fed - ss - med - st - pre;
  const per = (v) => money2(v / freq);

  set("net", per(net)); set("net2", per(net));
  set("gross", per(salary)); set("fed", per(fed)); set("ss", per(ss)); set("med", per(med));
  set("st", per(st)); set("pre", per(pre));
  set("annualNet", money(net));
  set("eff", salary > 0 ? ((fed + ss + med + st) / salary * 100).toFixed(1) + "%" : "-");
  set("marg", (marg * 100).toFixed(0) + "%");
  set("stateNote", stateNote(stateSel.value, status) + " " + Calc.t("Local taxes are not included."));
  const parts = [[net, "var(--accent)"], [fed, "#5b8def"], [ss, "#e0a64a"], [med, "#c46b9a"], [st, "#8a6fd1"], [pre, "#8a8f8c"]];
  document.getElementById("bar").innerHTML = salary > 0
    ? parts.map(([v, c]) => `<span style="width:${Math.max(v, 0) / salary * 100}%;background:${c}"></span>`).join("") : "";
});
