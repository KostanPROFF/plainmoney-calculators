Calc.bind("form", () => {
  const { num, set, fmt } = Calc;
  const f = (v) => (Number.isFinite(v) ? fmt(v) : "-");
  set("r1", f(num("p1") / 100 * num("v1")));
  set("r2", num("b2") ? f(num("a2") / num("b2") * 100) + "%" : "-");
  const from = num("from"), to = num("to");
  set("r3", from ? (to >= from ? "+" : "") + f((to - from) / Math.abs(from) * 100) + "%" : "-");
  set("diff", f(to - from));
});
