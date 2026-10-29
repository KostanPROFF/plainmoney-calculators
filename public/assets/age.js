// Calendar age: whole years, then months, then days, the way birthdays are counted.
const today = new Date().toISOString().slice(0, 10);
const asOfEl = document.getElementById("asof");
if (!asOfEl.value) asOfEl.value = today;
Calc.bind("form", () => {
  const { set, t, fmt, locale } = Calc;
  const b = new Date(document.getElementById("birth").value + "T12:00:00"), d = new Date(asOfEl.value + "T12:00:00");
  if (isNaN(b) || isNaN(d) || d < b) { set("age", "-"); return; }
  let y = d.getFullYear() - b.getFullYear(), m = d.getMonth() - b.getMonth(), dd = d.getDate() - b.getDate();
  if (dd < 0) { m--; dd += new Date(d.getFullYear(), d.getMonth(), 0).getDate(); }
  if (m < 0) { y--; m += 12; }
  const n = fmt;
  const days = Math.round((d - b) / 864e5);
  set("age", t("{n} years", { n: y }));
  set("ymd", t("{y} years, {m} months, {d} days", { y, m, d: dd }));
  set("months", n(y * 12 + m));
  set("weeks", n(Math.floor(days / 7)));
  set("days", n(days));
  set("born", b.toLocaleDateString(locale, { weekday: "long" }));
  let next = new Date(d.getFullYear(), b.getMonth(), b.getDate(), 12);
  if (next < d) next = new Date(d.getFullYear() + 1, b.getMonth(), b.getDate(), 12);
  const left = Math.round((next - d) / 864e5);
  set("next", left === 0 ? t("Today") : t("{n} days", { n: left }));
});
