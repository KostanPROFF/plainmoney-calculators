// Serves the static site from public/ and one small endpoint: /api/geo reports the visitor's
// country and US state from Cloudflare's IP geolocation, so calculators can preselect a state.
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === "/api/geo") {
      const cf = request.cf || {};
      return Response.json(
        { country: cf.country || null, region: cf.country === "US" ? cf.regionCode || null : null },
        { headers: { "cache-control": "private, no-store" } },
      );
    }
    return env.ASSETS.fetch(request);
  },
};
