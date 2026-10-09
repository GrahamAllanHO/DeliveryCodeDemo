# Step 5 – Browser tests with Playwright

**Goal:** Test what the Python tests cannot: filters, tooltips, popups and the legend running in a real browser.

## Prompt to give Copilot
> Add the tests using Playwright.

## What to expect
- `pytest-playwright` is added to `requirements-dev.txt`. Chromium needs a one-off install:
  ```bash
  pip install -r requirements-dev.txt
  python -m playwright install chromium
  ```
- `tests/stage05/test_ui.py` adds 11 browser tests: title, one icon per pub, legend, varying icon size and colour, both filters, combined filters, hover tooltip, click popup, and no JavaScript errors.
- Map tiles are blocked in the tests, so they do not depend on the network.
- Gotcha: the server fixture was called `base_url`, which clashes with a `pytest-playwright` fixture of the same name. Copilot renames it to `live_server_url`.
- A `ui` marker is registered, so `-m "not ui"` skips the browser tests.

## Do
```bash
python -m pytest -v
python -m pytest -m "not ui"
```
Expect 30 tests passing.

## Say
"The tests click and hover exactly as a user would."

## Next
Step 6 – break the single file into modules.
