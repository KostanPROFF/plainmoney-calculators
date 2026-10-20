Calc.bind("form", () => {
  const { num, money, set, t } = Calc;
  const income = num("income"), housing = num("housing");
  const total = housing + num("car") + num("student") + num("cards") + num("other");
  const dti = income > 0 ? total / income * 100 : 0;
  set("dti", income > 0 ? dti.toFixed(1) + "%" : "-");
  set("total", money(total));
  set("front", income > 0 ? (housing / income * 100).toFixed(1) + "%" : "-");
  set("room", money(Math.max(0, income * 0.36 - total)));
  const v = document.getElementById("verdict");
  const [text, cls] = dti <= 36 ? [t("Healthy: qualifies for most loans"), ""]
    : dti <= 43 ? [t("Manageable: within most mortgage limits"), "mid"]
    : dti < 50 ? [t("High: only some loan programs allow this"), "mid"]
    : [t("Very high: most lenders will decline"), "bad"];
  v.textContent = text; v.className = "verdict " + cls;
  document.getElementById("marker").style.left = Math.min(dti, 60) / 60 * 100 + "%";
});
