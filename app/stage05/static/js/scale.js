import { MIN_SIZE, MAX_SIZE } from "./config.js";

export function computeStats(pubs) {
  const ratings = pubs.map(p => p.review_rating);
  const ales = pubs.map(p => p.real_ales_available);
  return {
    rMin: Math.min(...ratings), rMax: Math.max(...ratings),
    aMin: Math.min(...ales), aMax: Math.max(...ales),
  };
}

const scale = (v, lo, hi) => hi === lo ? 1 : (v - lo) / (hi - lo);

// 0 = red, 1 = green
export const ratingColour = (rating, { rMin, rMax }) =>
  `hsl(${Math.round(scale(rating, rMin, rMax) * 120)}, 75%, 42%)`;

export const iconSize = (ales, { aMin, aMax }) =>
  Math.round(MIN_SIZE + scale(ales, aMin, aMax) * (MAX_SIZE - MIN_SIZE));
