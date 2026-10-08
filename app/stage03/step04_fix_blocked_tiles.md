# Step 4 – Troubleshoot: "Access blocked" map tiles

**Goal:** Show Copilot diagnosing and fixing a real problem found while running the app.

## Symptom
The map area shows an "Access blocked" message from OpenStreetMap instead of map tiles.

## Prompt to give Copilot
> That's showing access blocked from OpenStreetMap.

## Cause and fix
- OpenStreetMap's tile policy blocks requests that arrive without a `Referer` header.
- Copilot adds `<meta name="referrer" content="strict-origin-when-cross-origin">` and sets `referrerPolicy` on the Leaflet tile layer.
- Restart the server and hard-refresh the page (`Ctrl+Shift+R`).

## Fallback
If tiles are still blocked (some hosted environments are), ask Copilot to switch to another tile provider, for example CARTO.

## Say
"Real-world integrations break. This is a good example of iterating with Copilot to fix it."

## Next
Step 5 – tidy up the tooltip and simplify the page.
