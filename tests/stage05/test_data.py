import json

from app.stage05 import data

REQUIRED_FIELDS = {"id", "name", "location", "lat", "lng", "description",
                   "real_ales_available", "review_rating"}


def test_real_data_file_exists_and_has_pubs():
    assert data.PUBS_FILE.is_file()
    assert len(data.load_pubs()) > 0


def test_every_pub_has_required_fields_and_valid_values():
    for pub in data.load_pubs():
        assert REQUIRED_FIELDS <= pub.keys(), pub.get("name")
        assert -90 <= pub["lat"] <= 90
        assert -180 <= pub["lng"] <= 180
        assert pub["real_ales_available"] >= 0
        assert 0 <= pub["review_rating"] <= 10


def test_pub_ids_are_unique():
    ids = [p["id"] for p in data.load_pubs()]
    assert len(ids) == len(set(ids))


def test_load_pubs_reads_configured_file(pubs_file):
    assert [p["id"] for p in data.load_pubs()] == [1]


def test_load_pubs_rereads_file_each_call(pubs_file):
    data.load_pubs()
    pubs_file.write_text(json.dumps({"pubs": []}), encoding="utf-8")
    assert data.load_pubs() == []
