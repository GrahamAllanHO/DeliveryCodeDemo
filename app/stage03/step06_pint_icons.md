# Step 6 – Pint-glass icons driven by the data

**Goal:** Replace the default markers with pint glasses whose colour and size encode data.

## Prompt to give Copilot
> Can you change the icons? Use a pint glass, base the colour on the review rating and the size on the number of real ales.

## What to expect
- Each marker is an inline SVG pint glass, so there are no image files.
- **Colour:** review rating, from red (lowest) through to green (highest).
- **Size:** number of real ales, from 28px (fewest) to 56px (most).
- Both are scaled between the lowest and highest values in the data, so the scale adapts if the data changes.
- The hover tooltip still works and now sits above the glass.

## Do
1. Restart the server and refresh the page.
2. Point out a large green glass (many ales, high rating) and a small red-ish one (few ales, lower rating).
3. Hover to confirm the numbers in the tooltip match what the icon shows.

## Say
"One glance tells you which pubs have the best ratings and the biggest selection."

## Optional follow-ups
- Add a legend explaining the colour and size scale.
- Add a filter for minimum rating.

## Wrap-up
Recap: CLI script, web page, map, troubleshooting, tooltip polish, data-driven icons. Each step was a single plain-English prompt.
