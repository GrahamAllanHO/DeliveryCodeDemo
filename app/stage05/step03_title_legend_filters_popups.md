# Step 3 – Title, legend, filters and click popups

**Goal:** Implement the four chosen improvements in one prompt.

## Prompt to give Copilot
> Can you implement (1, 2, 3 and 5)?

## What to expect
- **Title bar:** a blue header reading "Merseyside Real Ale Pubs" with the subtitle "Best pubs from CAMRA's Good Beer Guide". The map fills the space below it.
- **Legend:** a panel at the bottom right showing the colour gradient (rating) and two glass sizes (number of ales).
- **Filters:** "Min rating" and "Min real ales" sliders in the header, with a "Showing X of Y pubs" counter. Slider ranges come from the data.
- **Click popup:** clicking a glass pins the same details table as the hover tooltip.
- Colours and sizes are scaled against the full data set, so filtering never changes how a pub looks.
- Copilot checks the result in a headless browser: filtering to rating 9+ leaves 3 of 10 pubs.

## Do
1. Restart the server (it must be restarted whenever `main.py` changes):
   ```bash
   python -m app.stage05.main
   ```
2. Move the sliders and watch the counter and glasses change.
3. Click a glass to pin its popup, then close it.

## Say
"One sentence picked four features from the list, and the data drives every one of them."

## Next
Step 4 – add automated tests.
