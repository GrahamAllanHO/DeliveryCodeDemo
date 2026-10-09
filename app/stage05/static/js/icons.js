import { ratingColour, iconSize } from "./scale.js";

export function pintSvg(size, colour) {
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 24 24">
    <path d="M5 3h14l-2 18a1 1 0 0 1-1 1H8a1 1 0 0 1-1-1z" fill="#fff" stroke="#333" stroke-width="1.2"/>
    <path d="M6.2 8h11.6l-1.4 12.6a.6.6 0 0 1-.6.4H8.2a.6.6 0 0 1-.6-.4z" fill="${colour}"/>
    <path d="M5.3 3h13.4l-.4 3.5H5.7z" fill="#fff" stroke="#333" stroke-width="1.2"/>
  </svg>`;
}

// Returns the icon and its size (callers need the size to position popups).
export function createPintIcon(pub, stats) {
  const size = iconSize(pub.real_ales_available, stats);
  const icon = L.divIcon({
    className: "pint-icon",
    html: pintSvg(size, ratingColour(pub.review_rating, stats)),
    iconSize: [size, size],
    iconAnchor: [size / 2, size],
    tooltipAnchor: [0, -size],
  });
  return { icon, size };
}
