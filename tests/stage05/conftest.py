import threading

import pytest
from werkzeug.serving import make_server

from app.stage05 import data, server


@pytest.fixture
def pubs_file(tmp_path, monkeypatch):
    """Point the app at a small, known data file."""
    path = tmp_path / "pubs.json"
    path.write_text(
        '{"pubs": [{"id": 1, "name": "Test </script> Arms", "location": "Wirral",'
        ' "lat": 53.4, "lng": -3.0, "description": "A & B",'
        ' "real_ales_available": 5, "review_rating": 8.0}]}',
        encoding="utf-8",
    )
    monkeypatch.setattr(data, "PUBS_FILE", path)
    return path


@pytest.fixture
def live_server_url():
    """Run the real HTTP server on a free port for the duration of a test."""
    httpd = make_server("127.0.0.1", 0, server.create_app(), threaded=True)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{httpd.server_address[1]}"
    httpd.shutdown()
    httpd.server_close()
    thread.join()
