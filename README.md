# PlainMoney Calculators

Static site with free US financial calculators (mortgage, auto loan, paycheck, 401(k), compound interest), monetized with Google AdSense.

- Edit pages in `build.py`, then run `python3 build.py` to regenerate the site in `public/`.
- Calculator logic lives in `public/assets/*.js`; styles in `public/assets/style.css`.
- Set `ADSENSE_CLIENT` in `build.py` after AdSense approval.

## Deploy

Cloudflare Workers Builds deploys every push to `main` using `wrangler.jsonc` (static assets from `public/`, custom domains plainmoneycalc.com and www).
