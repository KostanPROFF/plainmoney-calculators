// Shared helpers for every calculator page.
const Calc = (() => {
  const lang = document.documentElement.lang || "en";
  const locale = {
    es: "es-US", ru: "ru-RU", "zh-Hans": "zh-CN", ko: "ko-KR", vi: "vi-VN", "pt-BR": "pt-BR",
    ar: "ar-u-nu-latn", tl: "fil-PH", uk: "uk-UA",
  }[lang] || "en-US";
  const usd = new Intl.NumberFormat(locale, { style: "currency", currency: "USD", currencyDisplay: "narrowSymbol", maximumFractionDigits: 0 });
  const usd2 = new Intl.NumberFormat(locale, { style: "currency", currency: "USD", currencyDisplay: "narrowSymbol", minimumFractionDigits: 2, maximumFractionDigits: 2 });

  // Parse a typed amount. Accepts "425,000" and "6,5": a comma is a decimal separator unless it
  // groups thousands, so visitors on es/ru keyboards get the number they meant.
  // Text that is not a number comes back as NaN rather than as zero. A calculator that answers
  // "0" for a mistyped amount shows a wrong figure that looks right, so the caller is told.
  function toNumber(text) {
    let s = String(text).replace(/\s|[\u00a0\u202f]/g, "").replace(/[$\u20ac\u00a3\u00a5%]/g, "");
    if (s.includes(",")) {
      if (s.includes(".")) s = s.replace(/,/g, "");
      else s = /^[+-]?\d{1,3}(,\d{3})+$/.test(s) ? s.replace(/,/g, "") : s.replace(",", ".");
    }
    if (!/^[+-]?(\d+(\.\d*)?|\.\d+)$/.test(s)) return NaN;
    const v = parseFloat(s);
    return Number.isFinite(v) ? v : NaN;
  }
  function num(id) {
    const el = document.getElementById(id);
    const v = toNumber(el.value);
    // Money, rates and years are never below zero. A calculator that answers with a negative
    // payment looks broken rather than wrong, so the figure is treated as unreadable.
    if (Number.isFinite(v) && v < 0) return NaN;
    // A field that says how fine its figure may be (a whole year for an age) rounds to it.
    const step = Number(el.dataset.step);
    return Number.isFinite(step) && step > 0 ? Math.round(v / step) * step : v;
  }
  const money = (v) => (Number.isFinite(v) ? usd.format(Math.round(v)) : "-");
  const money2 = (v) => (Number.isFinite(v) ? usd2.format(v) : "-");
  // Plain number in the page language, with exactly `digits` decimals when given (up to 4 otherwise).
  const fmt = (v, digits) => (Number.isFinite(v)
    ? v.toLocaleString(locale, digits === undefined ? { maximumFractionDigits: 4 } : { minimumFractionDigits: digits, maximumFractionDigits: digits })
    : "-");
  const set = (id, text) => { const el = document.getElementById(id); if (el) el.textContent = text; };

  // Standard amortized payment.
  function payment(principal, annualRatePct, months) {
    if (months <= 0) return 0;
    const r = annualRatePct / 100 / 12;
    if (r === 0) return principal / months;
    return (principal * r) / (1 - Math.pow(1 + r, -months));
  }

  // Mark a field as unreadable and say why underneath it.
  function markField(input, message) {
    const field = input.closest(".field");
    if (!field) return;
    let error = field.querySelector(".field__error");
    if (message) {
      if (!error) {
        error = document.createElement("span");
        error.className = "field__error";
        error.id = input.id + "-error";
        const wrap = field.querySelector(".input-wrap");
        if (wrap) wrap.insertAdjacentElement("afterend", error);
        else field.appendChild(error);
      }
      error.textContent = message;
      input.setAttribute("aria-invalid", "true");
      input.setAttribute("aria-describedby", error.id);
      input.classList.add("input--invalid");
    } else if (error) {
      error.remove();
      input.removeAttribute("aria-invalid");
      input.removeAttribute("aria-describedby");
      input.classList.remove("input--invalid");
    }
  }

  // Check every numeric field on each change. A field that cannot be read as a number is marked
  // and says so underneath itself, and the figures it feeds show a dash rather than a wrong
  // number. A field that started empty is optional: leaving it blank is a choice, not a mistake.
  function validate(form) {
    form.querySelectorAll('input[inputmode="decimal"]').forEach((input) => {
      const raw = input.value.trim();
      const optional = input.defaultValue.trim() === "";
      const value = toNumber(raw);
      if (raw === "" && optional) markField(input, null);
      else if (!Number.isFinite(value)) markField(input, t("Enter a number"));
      else if (value < 0) markField(input, t("Enter a positive number"));
      else markField(input, null);
    });
  }

  // Re-run `fn` on every input change inside `form`, and once on load.
  function bind(form, fn) {
    const f = typeof form === "string" ? document.getElementById(form) : form;
    const run = () => { validate(f); fn(); };
    f.addEventListener("input", run);
    f.addEventListener("change", run);
    f.addEventListener("submit", (e) => { e.preventDefault(); run(); });
    run();
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
  const longDate = (d) => d.toLocaleDateString(locale, { month: "long", day: "numeric", year: "numeric" });

  // Preselect the visitor's US state in #state from /api/geo (Cloudflare IP geolocation), unless they
  // already picked one. The lookup is cached for the session; any failure just keeps the default.
  async function detectState() {
    const sel = document.getElementById("state");
    if (!sel) return;
    let touched = false;
    sel.addEventListener("change", (e) => { if (e.isTrusted) touched = true; });
    let geo = null;
    try { geo = JSON.parse(sessionStorage.getItem("geo")); } catch (e) {}
    if (!geo) {
      try {
        const r = await fetch("/api/geo");
        if (r.ok) {
          geo = await r.json();
          try { sessionStorage.setItem("geo", JSON.stringify(geo)); } catch (e) {}
        }
      } catch (e) { return; }
    }
    const code = geo && geo.region;
    if (touched || !code || !sel.querySelector(`option[value="${code}"]`)) return;
    sel.value = code;
    sel.dispatchEvent(new Event("change", { bubbles: true }));
    let hint = sel.parentElement.querySelector(".hint");
    if (!hint) { hint = document.createElement("span"); hint.className = "hint"; sel.parentElement.append(hint); }
    hint.textContent = t("Detected from your location");
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", detectState);
  else setTimeout(detectState);

  return { num, money, money2, fmt, set, payment, bind, areaChart, t, date, longDate, locale };
})();

// A result panel holds a dozen figures. Announcing all of them on every keystroke buries the one
// that matters, so the live region moves to the headline figure and the panel goes quiet.
document.querySelectorAll('section.panel[aria-live="polite"]').forEach((panel) => {
  panel.removeAttribute("aria-live");
  const headline = panel.querySelector(".headline .big");
  if (headline) {
    headline.setAttribute("aria-live", "polite");
    headline.setAttribute("aria-atomic", "true");
  }
});

// Header button flips between light and dark and remembers the choice; with no choice the system
// setting wins. The button shows the theme it switches to, and its name says the same thing.
const themeButton = document.querySelector(".theme-toggle");

function currentTheme() {
  const stored = document.documentElement.dataset.theme;
  if (stored === "light" || stored === "dark") return stored;
  return matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark";
}

function nameThemeButton() {
  if (!themeButton) return;
  const label = currentTheme() === "dark" ? Calc.t("Switch to light theme") : Calc.t("Switch to dark theme");
  themeButton.setAttribute("aria-label", label);
  themeButton.setAttribute("title", label);
}

themeButton?.addEventListener("click", () => {
  const next = currentTheme() === "dark" ? "light" : "dark";
  document.documentElement.dataset.theme = next;
  try { localStorage.setItem("theme", next); } catch (e) {}
  nameThemeButton();
});

// The system setting can change while the page is open, and the button has to keep naming the
// theme it switches to.
matchMedia("(prefers-color-scheme: light)").addEventListener("change", nameThemeButton);
if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", nameThemeButton);
else nameThemeButton();

// The language menu closes when the visitor clicks anywhere else.
document.addEventListener("click", (e) => {
  const menu = document.querySelector(".lang-menu[open]");
  if (menu && !menu.contains(e.target)) menu.open = false;
});
