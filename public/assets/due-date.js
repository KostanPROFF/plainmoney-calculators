// Naegele's rule: due date is 280 days after the first day of the last period, shifted for cycles other than 28 days.
const DAY = 864e5;
const lmpEl = document.getElementById("lmp");
if (!lmpEl.value) lmpEl.value = new Date(Date.now() - 70 * DAY).toISOString().slice(0, 10);
Calc.bind("form", () => {
  const { num, set, t, longDate } = Calc;
  const lmp = new Date(lmpEl.value + "T12:00:00");
  if (isNaN(lmp)) { set("due", "-"); return; }
  const shift = Math.round(num("cycle") || 28) - 28;
  const at = (days) => new Date(lmp.getTime() + (days + shift) * DAY);
  set("due", longDate(at(280)));
  set("conception", longDate(at(14)));
  set("tri2", longDate(at(13 * 7)));
  set("tri3", longDate(at(27 * 7)));
  const days = Math.floor((Date.now() - lmp.getTime()) / DAY) - shift;
  set("week", days < 0 ? "-" : days > 294 ? t("Past 42 weeks") : t("{w} weeks, {d} days", { w: Math.floor(days / 7), d: days % 7 }));
  set("trimester", days < 0 || days > 294 ? "-" : days < 13 * 7 ? t("First") : days < 27 * 7 ? t("Second") : t("Third"));
  set("left", days < 0 || days > 280 ? "-" : t("{n} days", { n: 280 - days }));
});
