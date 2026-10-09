# Step 7 – Productionise: switch the server to Flask

**Goal:** Ask what production needs, then replace the standard-library server with Flask.

## Prompts to give Copilot (two prompts)
> What would we need to do to productionise this application?

Copilot lists priorities: a real web framework behind gunicorn, HTTPS via a reverse proxy, a database, self-hosted Leaflet, a paid tile provider, security headers, health checks, a Dockerfile, CI/CD and housekeeping. Then:
> Can you rewrite the server to use Flask?

## What to expect
- `server.py` becomes a Flask app factory, `create_app()`, with `/`, `/index.html` and `/api/pubs` routes. Flask serves `/static/*` and blocks path traversal itself.
- `X-Content-Type-Options: nosniff` is still set on every response.
- Host and port come from the `HOST` and `PORT` environment variables. The default is `127.0.0.1`, no longer all interfaces.
- `flask` is added to `requirements.txt`.
- The server fixture now runs the Flask app. The tests themselves are unchanged and still pass (40).
- In production, run it with `gunicorn "app.stage05.server:create_app()"`.

## Do
```bash
pip install -r requirements.txt
python -m app.stage05.main
python -m pytest
```

## Say
"Same app and same tests, but now on a framework we can run properly in production."

## Next
Step 8 – fix a real UI bug.
