// Serves the static site from public/, redirects www to the bare domain, and one small endpoint: /api/geo reports the visitor's
// country and US state from Cloudflare's IP geolocation, so calculators can preselect a state.
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    // One host for search engines: www.plainmoneycalc.com used to serve the same pages as the bare domain,
    // so Google crawled both copies. Send it to the bare domain with a permanent redirect.
    if (url.hostname.startsWith("www.")) {
      url.hostname = url.hostname.slice(4);
      url.protocol = "https:";
      return Response.redirect(url.toString(), 301);
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
