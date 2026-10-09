# Step 4 – Add tests following best practice

**Goal:** Prove the app works with an automated pytest suite.

## Prompt to give Copilot
> Can you add some tests to verify that the app is working – follow best practice for test setup and folder structure.

## What to expect
- `tests/stage05/` mirrors `app/stage05/`, with shared fixtures in `conftest.py`.
- `pytest.ini` sets the test path, and `requirements-dev.txt` lists the test dependencies.
- A fixture points the app at a small temporary data file. Another runs the real HTTP server on a free port, so tests never clash with port 8000.
- 19 tests cover three areas:
  - **Data:** every pub has the required fields and sensible values.
  - **Page:** pub data round-trips into the page, and a `</script>` in a pub name cannot break out of the script tag.
  - **Server:** `/` and `/index.html` return 200, unknown paths return 404, and the data file is re-read on every request.

## Do
```bash
python -m pytest -v
```

## Say
"Tests that run the real server catch problems a unit test would miss."

## Next
Step 5 – test the map in a real browser.
