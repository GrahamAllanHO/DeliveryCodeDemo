import { createPintIcon } from "./icons.js";
import { detailsHtml } from "./format.js";
import { fitTooltip } from "./tooltip.js";

export function createMarker(pub, stats, map) {
  const { icon, size } = createPintIcon(pub, stats);
  const html = detailsHtml(pub);

  const marker = L.marker([pub.lat, pub.lng], { icon })
    .bindTooltip(html, { direction: "top", className: "pub-tooltip" })
    .bindPopup(`<div class="pub-tooltip">${html}</div>`,
               { offset: [0, -size + 8], minWidth: 340 });
  marker.on("tooltipopen", () => fitTooltip(marker, map, size));
  // Close the hover tooltip once the pinned popup is open.
  marker.on("click", () => marker.closeTooltip());
  return marker;
}
