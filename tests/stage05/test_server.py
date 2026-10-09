import json
import urllib.error
import urllib.request

import pytest

from app.stage05 import server


def fetch(url):
    with urllib.request.urlopen(url) as resp:
        return resp.status, resp.headers, resp.read()


def status_of(url):
    try:
        return fetch(url)[0]
    except urllib.error.HTTPError as err:
        return err.code


class TestIndex:
    @pytest.mark.parametrize("path", ["/", "/index.html", "/?x=1"])
    def test_serves_html(self, live_server_url, path):
        status, headers, body = fetch(live_server_url + path)
        assert status == 200
        assert headers["Content-Type"].startswith("text/html")
        assert b"<title>Merseyside Real Ale Pubs</title>" in body

    @pytest.mark.parametrize("fragment", [
        "Merseyside Real Ale Pubs",
        'id="minRating"',
        'id="minAles"',
        'id="count"',
        'name="referrer"',
        "/static/css/styles.css",
        "/static/js/app.js",
    ])
    def test_ui_elements_present(self, live_server_url, fragment):
        assert fragment in fetch(live_server_url + "/")[2].decode()

    def test_content_length_matches_body(self, live_server_url):
        _, headers, body = fetch(live_server_url + "/")
        assert int(headers["Content-Length"]) == len(body)


class TestApi:
    def test_returns_json_pubs(self, live_server_url, pubs_file):
        status, headers, body = fetch(live_server_url + "/api/pubs")
        assert status == 200
        assert headers["Content-Type"].startswith("application/json")
        pubs = json.loads(body)["pubs"]
        assert pubs[0]["name"] == "Test </script> Arms"

    def test_data_is_reread_on_each_request(self, live_server_url, pubs_file):
        fetch(live_server_url + "/api/pubs")
        pubs_file.write_text('{"pubs": []}', encoding="utf-8")
        assert json.loads(fetch(live_server_url + "/api/pubs")[2]) == {"pubs": []}


class TestStatic:
    @pytest.mark.parametrize("path, content_type", [
        ("/static/css/styles.css", "text/css"),
        ("/static/js/app.js", "text/javascript"),
    ])
    def test_serves_assets_with_content_type(self, live_server_url, path, content_type):
        status, headers, body = fetch(live_server_url + path)
        assert status == 200
        assert headers["Content-Type"].startswith(content_type)
        assert headers["X-Content-Type-Options"] == "nosniff"
        assert body

    def test_every_js_module_is_served(self, live_server_url):
        for js in (server.STATIC_DIR / "js").glob("*.js"):
            assert status_of(f"{live_server_url}/static/js/{js.name}") == 200

    def test_every_local_import_resolves(self, live_server_url):
        for js in (server.STATIC_DIR / "js").glob("*.js"):
            for line in js.read_text().splitlines():
                if line.startswith("import ") and '"./' in line:
                    name = line.split('"./')[1].split('"')[0]
                    assert (server.STATIC_DIR / "js" / name).is_file(), f"{js.name} -> {name}"


class TestNotFound:
    @pytest.mark.parametrize("path", [
        "/nope",
        "/static/missing.js",
        "/static/",
        "/static/js",
        "/static/../server.py",
        "/static/%2e%2e/server.py",
        "/static/js/../../data.py",
    ])
    def test_returns_404(self, live_server_url, path):
        assert status_of(live_server_url + path) == 404
