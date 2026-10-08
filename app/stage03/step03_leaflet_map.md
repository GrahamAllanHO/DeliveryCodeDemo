# Step 3 – Add a Leaflet map with hover descriptions

**Goal:** Plot every pub on a single interactive map and show its description on mouseover.

## Prompt to give Copilot
> Let's add a map to the browser using Leaflet. I want to see a single map with all the locations shown, and when I mouse over the icon I can see the description.

## What to expect
- Leaflet is loaded from a CDN (no install). OpenStreetMap supplies the tiles.
- The pub list is embedded in the page as JSON. Each pub's `lat` / `lng` becomes a marker.
- The map auto-zooms to fit all markers.
- The data is escaped before it goes into the page so it cannot break out of the script tag.

## Do
1. Restart the server (it must be restarted whenever `main.py` changes):
   ```bash
   python -m app.stage03.main
   ```
2. Refresh the browser and hover over a marker to see the description.

## Say
"Lat/long were already in the JSON. We just needed to use them."

## Next
Step 4 – fix the blocked map tiles (if you hit this).
