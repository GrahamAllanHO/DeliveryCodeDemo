# Step 1 – Start from the command-line baseline

**Goal:** Show the starting point: a small Python script that prints pub data to the terminal.

## Do
1. Open `app/stage03/main.py` and point out that it reads `app/data/pubs.json` and prints each pub.
2. Run it from the repo root:
   ```bash
   python -m app.stage03.main
   ```
3. Show the output: pub name, then indented properties (Location, Description, Real Ales Available, Review Rating).
4. Open `app/data/pubs.json` and point out the `lat` / `lng` fields. The script skips them today, but they are used later for the map.

## Say
"Right now the data only lives in the terminal. Let's turn it into something visual."

## Next
Step 2 – show the data in a web page.
