// BMI categories from the CDC adult ranges. The scale shows BMI 15 to 40.
Calc.bind("form", () => {
  const { num, set, t, fmt } = Calc;
  const inches = num("ft") * 12 + num("in"), lb = num("lb");
  if (inches <= 0 || lb <= 0) { set("bmi", "-"); return; }
  const bmi = 703 * lb / (inches * inches);
  const lo = 18.5 * inches * inches / 703, hi = 24.9 * inches * inches / 703;
  set("bmi", fmt(bmi, 1));
  set("range", t("{lo} to {hi} lb", { lo: Math.round(lo), hi: Math.round(hi) }));
  set("metric", t("{cm} cm, {kg} kg", { cm: Math.round(inches * 2.54), kg: fmt(lb * 0.4536, 1) }));
  const diff = lb > hi ? lb - hi : lb < lo ? lb - lo : 0;
  set("toRange", diff === 0 ? t("You are in the healthy range")
    : diff > 0 ? t("Lose {n} lb", { n: Math.ceil(diff) }) : t("Gain {n} lb", { n: Math.ceil(-diff) }));
  const v = document.getElementById("verdict");
  const [text, cls] = bmi < 18.5 ? [t("Underweight"), "mid"]
    : bmi < 25 ? [t("Healthy weight"), ""]
    : bmi < 30 ? [t("Overweight"), "mid"]
    : [t("Obesity"), "bad"];
  v.textContent = text; v.className = "verdict " + cls;
  document.getElementById("marker").style.left = (Math.min(Math.max(bmi, 15), 40) - 15) / 25 * 100 + "%";
});
