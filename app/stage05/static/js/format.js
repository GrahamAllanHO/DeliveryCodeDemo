import { SKIPPED_KEYS } from "./config.js";

const ESCAPES = {"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"};

export const esc = s => String(s).replace(/[&<>"']/g, c => ESCAPES[c]);

export const label = k => k.replace(/_/g, " ").replace(/\b\w/g, c => c.toUpperCase());

export function detailsHtml(pub) {
  const rows = Object.entries(pub)
    .filter(([k]) => !SKIPPED_KEYS.has(k))
    .map(([k, v]) => `<tr><th>${esc(label(k))}</th><td>${esc(v)}</td></tr>`)
    .join("");
  return `<div class="hdr">${esc(pub.name)}</div><table>${rows}</table>`;
}
