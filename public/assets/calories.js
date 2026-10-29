// Daily calories from the Mifflin-St Jeor equation times an activity factor.
Calc.bind("form", () => {
  const { num, set, t } = Calc;
  const kg = num("lb") * 0.4536, cm = (num("ft") * 12 + num("in")) * 2.54, age = num("age");
  const male = document.getElementById("sex").value === "m";
  const bmr = 10 * kg + 6.25 * cm - 5 * age + (male ? 5 : -161);
  const tdee = bmr * parseFloat(document.getElementById("activity").value);
  const floor = male ? 1500 : 1200;
  const fmt = (v) => t("{n} cal", { n: Math.round(v / 10) * 10 });
  const ok = kg > 0 && cm > 0 && age > 0;
  set("tdee", ok ? fmt(tdee) : "-");
  set("bmr", ok ? fmt(bmr) : "-");
  set("lose1", ok ? fmt(Math.max(floor, tdee - 500)) : "-");
  set("lose05", ok ? fmt(Math.max(floor, tdee - 250)) : "-");
  set("gain05", ok ? fmt(tdee + 250) : "-");
  set("gain1", ok ? fmt(tdee + 500) : "-");
  set("note", ok && tdee - 500 < floor ? t("Weight-loss targets are held at {n} calories a day, a common minimum without medical supervision.", { n: floor }) : "");
});
