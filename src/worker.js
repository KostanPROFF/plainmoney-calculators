// Serves the static site from public/, redirects www to the bare domain, and one small endpoint: /api/geo reports the visitor's
// country and US state from Cloudflare's IP geolocation, so calculators can preselect a state.
const CANONICAL_ORIGIN = "https://plainmoneycalc.com";
const WWW_HOST = "www.plainmoneycalc.com";

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    // One host for search engines: www.plainmoneycalc.com used to serve the same pages as the bare domain,
    // so Google crawled both copies. Send it to the bare domain with a permanent redirect.
    // The target is built from a fixed origin, never from the request's Host header, so the redirect can only
    // ever point at our own site. Leading slashes are collapsed so a path like "//evil.com" stays a path.
    if (url.hostname === WWW_HOST) {
      const path = url.pathname.replace(/^\/+/, "/");
      return Response.redirect(CANONICAL_ORIGIN + path + url.search, 301);
    }
    if (url.pathname === "/api/geo") {
      const cf = request.cf || {};
      return Response.json(
        { country: cf.country || null, region: cf.country === "US" ? cf.regionCode || null : null },
        { headers: { "cache-control": "private, no-store" } },
      );
    }
    // /.well-known/ai.txt is a static file too; this only answers if a deploy ever leaves the dot folder out.
    if (url.pathname === "/.well-known/ai.txt") {
      return env.ASSETS.fetch(new Request(new URL("/ai.txt", url), request));
    }
    return env.ASSETS.fetch(request);
  },
};
