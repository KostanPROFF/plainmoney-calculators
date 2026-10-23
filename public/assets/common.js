// Shared helpers for every calculator page.
const Calc = (() => {
  const lang = document.documentElement.lang || "en";
  const locale = { es: "es-US", ru: "ru-RU" }[lang] || "en-US";
  const usd = new Intl.NumberFormat(locale, { style: "currency", currency: "USD", maximumFractionDigits: 0 });
  const usd2 = new Intl.NumberFormat(locale, { style: "currency", currency: "USD", minimumFractionDigits: 2, maximumFractionDigits: 2 });

  function num(id) {
    const el = document.getElementById(id);
    const v = parseFloat(String(el.value).replace(/[^0-9.\-]/g, ""));
    return Number.isFinite(v) ? v : 0;
  }
  const money = (v) => usd.format(Math.round(v));
  const money2 = (v) => usd2.format(v);
  const set = (id, text) => { const el = document.getElementById(id); if (el) el.textContent = text; };

  // Standard amortized payment.
  function payment(principal, annualRatePct, months) {
    if (months <= 0) return 0;
    const r = annualRatePct / 100 / 12;
    if (r === 0) return principal / months;
    return (principal * r) / (1 - Math.pow(1 + r, -months));
  }

  // Re-run `fn` on every input change inside `form`, and once on load.
  function bind(form, fn) {
    const f = typeof form === "string" ? document.getElementById(form) : form;
    f.addEventListener("input", fn);
    f.addEventListener("change", fn);
    f.addEventListener("submit", (e) => { e.preventDefault(); fn(); });
    fn();
  }

  // Stacked-area chart. series: [{values:[], color:"css var or color", label}], x labels: []
  function areaChart(svg, xs, series) {
    const W = 640, H = 260, L = 64, R = 12, T = 12, B = 28;
    const n = xs.length;
    if (n < 2) { svg.innerHTML = ""; return; }
    const totals = xs.map((_, i) => series.reduce((s, ser) => s + ser.values[i], 0));
    const maxV = niceMax(Math.max(...totals, 1));
    const x = (i) => L + (i / (n - 1)) * (W - L - R);
    const y = (v) => T + (1 - v / maxV) * (H - T - B);
    let out = "";
    for (let k = 0; k <= 4; k++) {
      const v = (maxV / 4) * k;
      out += `<line class="grid" x1="${L}" x2="${W - R}" y1="${y(v)}" y2="${y(v)}"/>`;
      out += `<text x="${L - 8}" y="${y(v) + 4}" text-anchor="end">${short(v)}</text>`;
    }
    const step = Math.max(1, Math.ceil(n / 8));
    for (let i = 0; i < n; i += step) out += `<text x="${x(i)}" y="${H - 8}" text-anchor="middle">${xs[i]}</text>`;
    const base = new Array(n).fill(0);
    series.forEach((ser) => {
      const top = base.map((b, i) => b + ser.values[i]);
      let d = `M${x(0)},${y(top[0])}`;
      for (let i = 1; i < n; i++) d += `L${x(i)},${y(top[i])}`;
      for (let i = n - 1; i >= 0; i--) d += `L${x(i)},${y(base[i])}`;
      out += `<path d="${d}Z" style="fill:${ser.color};fill-opacity:.85"/>`;
      top.forEach((v, i) => (base[i] = v));
    });
    out += `<circle cx="${x(n - 1)}" cy="${y(totals[n - 1])}" r="4" style="fill:var(--fg)"/>`;
    svg.setAttribute("viewBox", `0 0 ${W} ${H}`);
    svg.innerHTML = out;
  }
  function niceMax(v) {
    const p = Math.pow(10, Math.floor(Math.log10(v)));
    for (const m of [1, 2, 2.5, 5, 10]) if (m * p >= v) return m * p;
    return 10 * p;
  }
  function short(v) {
    if (v >= 1e6) return "$" + (v / 1e6).toFixed(v % 1e6 ? 1 : 0) + "M";
    if (v >= 1e3) return "$" + (v / 1e3).toFixed(0) + "K";
    return "$" + v.toFixed(0);
  }

  // Translate an English template from window.I18N (translated pages load it) and fill {placeholders}.
  // A translation can be {one, few, many, other} plural forms, picked by the first numeric placeholder.
  const plural = new Intl.PluralRules(locale);
  function t(text, vars = {}) {
    let out = (window.I18N && window.I18N[text]) || text;
    if (typeof out === "object") {
      const n = Object.values(vars).find((v) => typeof v === "number");
      out = out[plural.select(n)] || out.other;
    }
    return out.replace(/\{(\w+)\}/g, (m, k) => (k in vars ? (typeof vars[k] === "number" ? vars[k].toLocaleString(locale) : vars[k]) : m));
  }
  const date = (d) => d.toLocaleDateString(locale, { month: "short", year: "numeric" });

  return { num, money, money2, set, payment, bind, areaChart, t, date };
})();
