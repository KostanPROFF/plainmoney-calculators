// Average tax rates by state, used to prefill the tax field when a state is picked.
// sales: state plus average local sales tax, % (Tax Foundation, 2025). Vehicle taxes differ in some states.
// property: average effective property tax on owner-occupied homes, % of value per year.
const STATE_TAX = {
  AL: [9.29, 0.38], AK: [1.82, 1.0], AZ: [8.52, 0.45], AR: [9.45, 0.57], CA: [8.85, 0.71], CO: [7.81, 0.49],
  CT: [6.35, 1.48], DE: [0, 0.5], DC: [6.0, 0.57], FL: [7.0, 0.79], GA: [7.38, 0.81], HI: [4.5, 0.27],
  ID: [6.03, 0.47], IL: [8.86, 1.95], IN: [7.0, 0.75], IA: [6.94, 1.43], KS: [8.65, 1.27], KY: [6.0, 0.77],
  LA: [10.11, 0.51], ME: [5.5, 0.98], MD: [6.0, 0.99], MA: [6.25, 1.04], MI: [6.0, 1.2], MN: [8.04, 1.02],
  MS: [7.06, 0.67], MO: [8.39, 0.9], MT: [0, 0.64], NE: [6.97, 1.5], NV: [8.24, 0.48], NH: [0, 1.61],
  NJ: [6.6, 2.08], NM: [7.62, 0.67], NY: [8.53, 1.4], NC: [7.0, 0.7], ND: [7.04, 0.92], OH: [7.24, 1.36],
  OK: [8.99, 0.82], OR: [0, 0.86], PA: [6.34, 1.35], RI: [7.0, 1.24], SC: [7.49, 0.51], SD: [6.11, 1.07],
  TN: [9.56, 0.56], TX: [8.2, 1.58], UT: [7.32, 0.52], VT: [6.36, 1.71], VA: [5.77, 0.82], WA: [9.43, 0.84],
  WV: [6.59, 0.55], WI: [5.72, 1.51], WY: [5.44, 0.55],
};

// Keeps `fieldId` in step with the #state select: kind 0 = sales tax, 1 = property tax.
function linkStateTax(fieldId, kind) {
  const sel = document.getElementById("state"), field = document.getElementById(fieldId);
  const fill = () => { if (STATE_TAX[sel.value]) field.value = STATE_TAX[sel.value][kind]; };
  sel.addEventListener("change", fill);
  fill();
}
