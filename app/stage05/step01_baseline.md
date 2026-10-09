# Step 1 – Start from the working map app

**Goal:** Show the starting point: a single-file Python app that serves an interactive Leaflet map of Merseyside pubs.

## Do
1. Open `app/stage05/main.py` and point out the three parts in one file: the Python web server, the HTML/CSS page template, and the JavaScript that builds the map.
2. Run it from the repo root:
   ```bash
   python -m app.stage05.main
   ```
3. Open http://127.0.0.1:8000. In Codespaces, open the forwarded port 8000.
4. Hover over a pint glass. Colour is the review rating, size is the number of real ales.

## Say
"This works, but the page has no title, no explanation of the icons, and no way to filter. Let's ask Copilot how to improve it."

## Next
Step 2 – ask Copilot for UI improvement ideas.
