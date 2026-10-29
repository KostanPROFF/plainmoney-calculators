Calc.bind("form", () => {
  const { num, money2, set, fmt } = Calc;
  const bill = num("bill"), pct = num("pct"), people = Math.max(1, Math.round(num("people")));
  const round = document.getElementById("round").value === "1";
  let total = bill * (1 + pct / 100);
  if (round) total = Math.ceil(total / people) * people;
  set("perPerson", money2(total / people));
  set("tip", money2(total - bill));
  set("total", money2(total));
  set("tipPer", money2((total - bill) / people));
  set("effPct", bill ? fmt((total - bill) / bill * 100, 1) + "%" : "-");
  document.getElementById("compare").innerHTML = [10, 15, 18, 20, 22, 25].map((p) =>
    `<tr><td>${p}%</td><td>${money2(bill * p / 100)}</td><td>${money2(bill * (1 + p / 100))}</td><td>${money2(bill * (1 + p / 100) / people)}</td></tr>`).join("");
});
