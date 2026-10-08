# Step 5 – Property-list tooltip and map-only page

**Goal:** Improve the hover tooltip's look and remove the pub cards so the page is just the map.

## Prompt to give Copilot
> Can you improve the formatting of the mouseover so it looks more like a list of properties, and there is no need to show all the pubs on the webpage. I'm only interested in the map.

## What to expect
- The pub cards are removed and the map fills the whole browser window.
- The tooltip is built in JavaScript: a blue header with the pub name, then a two-column table of property and value.
- Property labels are generated from the JSON keys (`real_ales_available` becomes "Real Ales Available"). New fields added to the JSON appear automatically.
- `lat`, `lng`, `id` and `name` are skipped in the table.

## Do
1. Restart the server and refresh the page.
2. Hover over several markers to show the table layout.

## Say
"The tooltip is driven by the data. If I add a field to the JSON, it shows up with no code change."

## Next
Step 6 – make the icons carry meaning.
