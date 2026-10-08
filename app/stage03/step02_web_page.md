# Step 2 – Show the output in a web page

**Goal:** Convert the CLI script into a tiny web server that renders the JSON data in a browser.

## Prompt to give Copilot
> Looking at stage03, I'd like to show the output in a web page. Convert the code so the data is read from the JSON file and shows in a browser.

## What to expect
- `main.py` now uses Python's standard library (`http.server`), so there is nothing to install.
- The JSON is read on each request, and each pub is rendered as a card with its properties.
- The hard-coded absolute path is replaced with a path relative to the script.

## Do
1. Run the server:
   ```bash
   python -m app.stage03.main
   ```
2. Open http://127.0.0.1:8000. In Codespaces, open the forwarded port 8000.
3. Show the cards, then stop the server with `Ctrl+C`.

## Say
"Same data, same JSON file, but now it's in a browser. No frameworks needed."

## Next
Step 3 – put the pubs on a map.
