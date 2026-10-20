Calc.bind("form", () => {
  const { num, money2, set } = Calc;
  const amount = num("amount"), hours = num("hours"), days = num("days"), weeks = num("weeks");
  const per = document.getElementById("per").value;
  const perYear = { hour: hours * weeks, day: days * weeks, week: weeks, biweek: weeks / 2, semimonth: 24, month: 12, year: 1 };
  const yearly = amount * perYear[per];
  const div = (n) => (n > 0 ? money2(yearly / n) : "-");
  set("hourly", div(hours * weeks));
  set("daily", div(days * weeks));
  set("weekly", div(weeks));
  set("biweekly", div(weeks / 2));
  set("semimonthly", div(24));
  set("monthly", div(12));
  set("yearly", money2(yearly));
});
