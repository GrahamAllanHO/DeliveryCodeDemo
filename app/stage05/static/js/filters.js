// entries: [{pub, marker}]; layer: the Leaflet layer group markers are shown in.
export function setupFilters(entries, layer, stats) {
  const minRating = document.getElementById("minRating");
  const minAles = document.getElementById("minAles");
  const ratingOut = document.getElementById("minRatingOut");
  const alesOut = document.getElementById("minAlesOut");
  const count = document.getElementById("count");

  Object.assign(minRating, { min: Math.floor(stats.rMin), max: Math.ceil(stats.rMax), step: 0.1, value: Math.floor(stats.rMin) });
  Object.assign(minAles, { min: stats.aMin, max: stats.aMax, step: 1, value: stats.aMin });

  function apply() {
    const r = parseFloat(minRating.value);
    const a = parseInt(minAles.value, 10);
    ratingOut.textContent = r.toFixed(1);
    alesOut.textContent = a;
    let shown = 0;
    entries.forEach(({ pub, marker }) => {
      const visible = pub.review_rating >= r && pub.real_ales_available >= a;
      if (visible) { layer.addLayer(marker); shown++; } else { layer.removeLayer(marker); }
    });
    count.textContent = `Showing ${shown} of ${entries.length} pubs`;
  }

  minRating.addEventListener("input", apply);
  minAles.addEventListener("input", apply);
  apply();
}
