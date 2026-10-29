// Standard 4.0 scale; A+ counts as 4.0, as at most US colleges.
Calc.bind("form", () => {
  const { num, set, fmt } = Calc;
  let points = 0, credits = 0;
  for (let i = 1; document.getElementById("g" + i); i++) {
    const g = document.getElementById("g" + i).value, c = num("c" + i);
    if (g === "" || c <= 0) continue;
    points += parseFloat(g) * c; credits += c;
  }
  const prevC = num("prevCredits"), prevG = num("prevGpa");
  set("gpa", credits ? fmt(points / credits, 2) : "-");
  set("credits", fmt(credits));
  set("points", fmt(points, 1));
  const allC = credits + prevC;
  set("cum", allC && (credits || prevC) ? fmt((points + prevG * prevC) / allC, 2) : "-");
});
