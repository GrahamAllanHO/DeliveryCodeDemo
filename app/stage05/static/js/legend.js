import { MIN_SIZE, MAX_SIZE } from "./config.js";
import { pintSvg } from "./icons.js";

export function addLegend(map, { rMin, rMax, aMin, aMax }) {
  const legend = L.control({ position: "bottomright" });
  legend.onAdd = () => {
    const div = L.DomUtil.create("div", "legend");
    const glass = (size, text) => `<div>${pintSvg(size, "#888")}<br>${text}</div>`;
    div.innerHTML = `
      <h4>Colour = review rating</h4>
      <div class="bar"></div>
      <div class="ends"><span>${rMin}</span><span>${rMax}</span></div>
      <h4 class="spaced">Size = real ales</h4>
      <div class="sizes">${glass(MIN_SIZE, aMin)}${glass(MAX_SIZE, aMax)}</div>`;
    return div;
  };
  legend.addTo(map);
}
