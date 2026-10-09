import os
from pathlib import Path

from flask import Flask, jsonify, send_from_directory

from . import data

STATIC_DIR = Path(__file__).resolve().parent / "static"


def create_app():
    app = Flask(__name__, static_folder=str(STATIC_DIR), static_url_path="/static")

    @app.get("/")
    @app.get("/index.html")
    def index():
        return send_from_directory(STATIC_DIR, "index.html")

    @app.get("/api/pubs")
    def pubs():
        return jsonify({"pubs": data.load_pubs()})

    @app.after_request
    def security_headers(response):
        response.headers["X-Content-Type-Options"] = "nosniff"
        return response

    return app


def run(host=None, port=None):
    host = host or os.environ.get("HOST", "127.0.0.1")
    port = port or int(os.environ.get("PORT", "8000"))
    print(f"Serving on http://{host}:{port} (Ctrl+C to stop)")
    create_app().run(host=host, port=port)
