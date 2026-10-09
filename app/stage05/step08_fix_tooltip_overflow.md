# Step 8 – Troubleshoot: tooltips running off the screen

**Goal:** Show Copilot fixing a real usability bug found by using the app.

## Symptom
On mouseover, the tooltip for pubs near the top of the map goes above the top of the screen.

## Prompts to give Copilot (two prompts)
> Sometimes when I mouse over the pub, the tooltip goes above the top of the screen. Can you fix that?

The first fix handles only the top edge. Then:
> One of the popups (The Gate Inn) is still off the screen.

## What to expect
- **Cause:** tooltips were always drawn above the icon, and the first fix guessed the tooltip height. The Gate Inn is on the east side, so its tooltip was cut off on the right.
- **Fix:** `static/js/tooltip.js` measures where the tooltip actually lands once open. If it is cut off at the top it flips below the icon, then it is nudged back in from any edge that still overflows.
- Tooltips are now a fixed 320px wide. They were narrow and tall (up to about 450px), which made them overflow more.
- Click popups already pan into view, so they are left alone.
- A regression test hovers every pub at 1200×800, 1000×600 and phone width 390×700, and checks the tooltip stays inside the map. It fails before the fix and passes after (43 tests).

## Do
1. Restart the server and hard-refresh (`Ctrl+Shift+R`).
2. Hover the northernmost pub and The Gate Inn.
3. Run `python -m pytest`.

## Say
"I found a real bug by using the app. Copilot fixed it, then fixed it properly when I showed it the case it missed, and a test now guards against it."

## Wrap-up
Recap: baseline map, ask for ideas, title/legend/filters/popups, unit tests, browser tests, refactor, Flask, tooltip bug fix. Each step was one plain-English prompt.

## Optional follow-ups
- Search box and pub list sidebar (from the step 2 list).
- Docker, CI/CD and a database (from step 7).
