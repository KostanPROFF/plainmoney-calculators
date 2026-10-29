# PlainMoney Calculators

Static site with free US financial calculators (mortgage, auto loan, paycheck, 401(k), compound interest), monetized with Google AdSense.

- Edit pages in `build.py`, then run `python3 build.py` to regenerate the site in `public/`.
- Calculator logic lives in `public/assets/*.js`; styles in `public/assets/style.css`.
- Set `ADSENSE_CLIENT` in `build.py` after AdSense approval.
- `build.py` deletes any `public/**/*.html` it did not generate, so renamed pages do not linger.

## Analytics and consent

GA4 loads directly with `gtag.js` from `build.py` (`GA_ID`); no Tag Manager container is used.

AdSense and Analytics cookies must not be set before consent in the EEA and UK. Enable the GDPR message in AdSense (Privacy & messaging) so Google's certified CMP asks visitors first; the site itself needs no extra code for that.

## Deploy

Cloudflare Workers Builds deploys every push to `main` using `wrangler.jsonc` (static assets from `public/`, custom domains plainmoneycalc.com and www).
