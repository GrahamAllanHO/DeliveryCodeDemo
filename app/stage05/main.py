import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

PUBS_FILE = Path(__file__).resolve().parent.parent / "data" / "pubs.json"
HOST = "0.0.0.0"
PORT = 8000

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="strict-origin-when-cross-origin">
<title>Merseyside Pubs</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
<style>
  html, body, #map { height: 100%; margin: 0; }
  .pub-tooltip { padding: 0; border: 0; overflow: hidden; font-family: system-ui, sans-serif; }
  .pub-tooltip .hdr { background: #1d4ed8; color: #fff; padding: 6px 10px; font-weight: 600; }
  .pub-tooltip table { border-collapse: collapse; font-size: 12px; }
  .pub-tooltip th { text-align: left; padding: 3px 10px; color: #555; vertical-align: top; white-space: nowrap; }
  .pub-tooltip td { padding: 3px 10px; max-width: 280px; white-space: normal; }
  .pub-tooltip tr:nth-child(even) { background: #f3f4f6; }
  .pint-icon { background: none; border: 0; }
</style>
</head>
<body>
<div id="map"></div>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
const PUBS = __PUBS_JSON__;
const SKIPPED = new Set(["id", "name", "lat", "lng"]);
const MIN_SIZE = 28, MAX_SIZE = 56;

const map = L.map("map");
L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  referrerPolicy: "strict-origin-when-cross-origin",
  attribution: "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors"
}).addTo(map);

const esc = s => String(s).replace(/[&<>"']/g, c =>
  ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"}[c]));
const label = k => k.replace(/_/g, " ").replace(/\\b\\w/g, c => c.toUpperCase());

const ratings = PUBS.map(p => p.review_rating);
const ales = PUBS.map(p => p.real_ales_available);
const rMin = Math.min(...ratings), rMax = Math.max(...ratings);
const aMin = Math.min(...ales), aMax = Math.max(...ales);
const scale = (v, lo, hi) => hi === lo ? 1 : (v - lo) / (hi - lo);

// 0 = red, 1 = green
const ratingColour = t => `hsl(${Math.round(t * 120)}, 75%, 42%)`;

function pintSvg(size, colour) {
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 24 24">
    <path d="M5 3h14l-2 18a1 1 0 0 1-1 1H8a1 1 0 0 1-1-1z" fill="#fff" stroke="#333" stroke-width="1.2"/>
    <path d="M6.2 8h11.6l-1.4 12.6a.6.6 0 0 1-.6.4H8.2a.6.6 0 0 1-.6-.4z" fill="${colour}"/>
    <path d="M5.3 3h13.4l-.4 3.5H5.7z" fill="#fff" stroke="#333" stroke-width="1.2"/>
  </svg>`;
}

function tooltipHtml(pub) {
  const rows = Object.entries(pub)
    .filter(([k]) => !SKIPPED.has(k))
    .map(([k, v]) => `<tr><th>${esc(label(k))}</th><td>${esc(v)}</td></tr>`)
    .join("");
  return `<div class="hdr">${esc(pub.name)}</div><table>${rows}</table>`;
}

const bounds = [];
PUBS.forEach(pub => {
  const size = Math.round(MIN_SIZE + scale(pub.real_ales_available, aMin, aMax) * (MAX_SIZE - MIN_SIZE));
  const colour = ratingColour(scale(pub.review_rating, rMin, rMax));
  const icon = L.divIcon({
    className: "pint-icon",
    html: pintSvg(size, colour),
    iconSize: [size, size],
    iconAnchor: [size / 2, size],
    tooltipAnchor: [0, -size]
  });
  L.marker([pub.lat, pub.lng], {icon})
    .bindTooltip(tooltipHtml(pub), {direction: "top", className: "pub-tooltip"})
    .addTo(map);
  bounds.push([pub.lat, pub.lng]);
});
if (bounds.length) map.fitBounds(bounds, {padding: [60, 60]});
</script>
</body>
</html>
"""


def load_pubs():
    with open(PUBS_FILE, encoding="utf-8") as f:
        return json.load(f)["pubs"]


def render_page():
    # Escape characters that could close the script tag or break the JS literal.
    data = (
        json.dumps(load_pubs())
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("&", "\\u0026")
    )
    return PAGE.replace("__PUBS_JSON__", data)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.split("?")[0] not in ("/", "/index.html"):
            self.send_error(404)
            return
        body = render_page().encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main():
    server = HTTPServer((HOST, PORT), Handler)
    print(f"Serving on http://127.0.0.1:{PORT} (Ctrl+C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
