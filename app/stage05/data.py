import json
from pathlib import Path

PUBS_FILE = Path(__file__).resolve().parent.parent / "data" / "pubs.json"


def load_pubs():
    with open(PUBS_FILE, encoding="utf-8") as f:
        return json.load(f)["pubs"]
