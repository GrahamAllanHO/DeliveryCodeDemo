import { TILE_URL, REFERRER_POLICY } from "./config.js";
import { computeStats } from "./scale.js";
import { createMarker } from "./markers.js";
import { setupFilters } from "./filters.js";
import { addLegend } from "./legend.js";

async function loadPubs() {
  const response = await fetch("/api/pubs");
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return (await response.json()).pubs;
}

function createMap() {
  const map = L.map("map");
  L.tileLayer(TILE_URL, {
    maxZoom: 19,
    referrerPolicy: REFERRER_POLICY,
    attribution: "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors",
  }).addTo(map);
  return map;
}

async function init() {
  const map = createMap();
  let pubs;
  try {
    pubs = await loadPubs();
  } catch (err) {
    document.getElementById("count").textContent = `Could not load pubs (${err.message})`;
    return;
  }
  if (!pubs.length) {
    document.getElementById("count").textContent = "No pubs to show";
    map.setView([53.4, -3.0], 10);
    return;
  }

  const stats = computeStats(pubs);
  const layer = L.layerGroup().addTo(map);
  const entries = pubs.map(pub => ({ pub, marker: createMarker(pub, stats, map) }));

  setupFilters(entries, layer, stats);
  addLegend(map, stats);
  map.fitBounds(pubs.map(p => [p.lat, p.lng]), { padding: [60, 60] });
}

init();
