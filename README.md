# PlainMoney Calculators

Static site with free US financial calculators (mortgage, auto loan, paycheck, 401(k), compound interest), monetized with Google AdSense.

- Edit pages in `build.py`, then run `python3 build.py` to regenerate the `*.html` files.
- Calculator logic lives in `assets/*.js`; styles in `assets/style.css`.
- Before launch set `SITE_URL` and `ADSENSE_CLIENT` in `build.py`.

## Deploy (Cloudflare Pages)

Connect this repo in Cloudflare → Workers & Pages → Create → Pages → Connect to Git.
Framework preset: None. Build command: empty. Build output directory: `/`.
