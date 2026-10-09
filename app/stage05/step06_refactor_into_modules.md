# Step 6 – Refactor the single file into modules

**Goal:** Break a 220-line file mixing Python, HTML, CSS and JavaScript into small single-purpose files.

## Prompt to give Copilot (two prompts)
> Looking at just the stage05 application, how is it structured? Is this a bit big for a single file? How would you break it up into smaller files?

Review the proposal, then:
> Go ahead with the refactor.

## What to expect
```
app/stage05/
├── main.py        # entry point (same command)
├── server.py      # HTTP handler, routing, static files
├── data.py        # load_pubs()
└── static/
    ├── index.html
    ├── css/styles.css
    └── js/        # app, config, format, scale, icons, markers, filters, legend
```
- The pub data is now served as JSON from `/api/pubs` and fetched by the page. This replaces injecting JSON into the HTML and removes the script-escaping workaround.
- `/static/*` is served with a path-traversal guard, so `../` paths return 404.
- The tests are split to match: `test_data.py`, `test_server.py`, `test_ui.py`. There are now 40.

## Do
```bash
python -m app.stage05.main
python -m pytest
```
The behaviour is identical to before. The tests prove it.

## Say
"The tests let us restructure with confidence: same behaviour, much easier to maintain."

## Next
Step 7 – move to Flask.
