const MARGIN = 8;

const overflow = (rect, bounds) => ({
  left: Math.max(0, bounds.left + MARGIN - rect.left),
  right: Math.max(0, rect.right - (bounds.right - MARGIN)),
  top: Math.max(0, bounds.top + MARGIN - rect.top),
  bottom: Math.max(0, rect.bottom - (bounds.bottom - MARGIN)),
});

function rects(tooltip, map) {
  return {
    rect: tooltip.getElement().getBoundingClientRect(),
    bounds: map.getContainer().getBoundingClientRect(),
  };
}

// Start every hover from the default placement (above the icon).
function resetTooltip(tooltip) {
  tooltip.options.direction = "top";
  tooltip.options.offset = L.point(0, 0);
  tooltip.update();
}

// Once open, keep the tooltip fully inside the map: flip below the icon if it
// is cut off at the top, then nudge it back in from any remaining edge.
export function fitTooltip(marker, map, iconSize) {
  const tooltip = marker.getTooltip();
  const el = tooltip.getElement();
  if (!el) return;

  resetTooltip(tooltip);
  let { rect, bounds } = rects(tooltip, map);
  let over = overflow(rect, bounds);
  if (over.top > 0 && over.bottom === 0) {
    // The icon's tooltip anchor sits at the top of the glass; cancel it for "below".
    tooltip.options.direction = "bottom";
    tooltip.options.offset = L.point(0, iconSize);
    tooltip.update();
    ({ rect, bounds } = rects(tooltip, map));
    over = overflow(rect, bounds);
    if (over.bottom > over.top) {
      resetTooltip(tooltip);
      ({ rect, bounds } = rects(tooltip, map));
      over = overflow(rect, bounds);
    }
  }

  const dx = over.left - over.right;
  const dy = over.top - over.bottom;
  if (dx || dy) {
    tooltip.options.offset = L.point(tooltip.options.offset.x + dx, tooltip.options.offset.y + dy);
    tooltip.update();
  }
}
