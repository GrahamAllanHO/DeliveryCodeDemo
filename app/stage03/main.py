import json

PUBS_FILE = "/workspaces/DeliveryCodeDemo/app/data/pubs.json"
SKIPPED_KEYS = {"id", "name", "lat", "lng"}

def main():
    with open(PUBS_FILE, encoding="utf-8") as f:
        data = json.load(f)

    for pub in data["pubs"]:
        print(pub["name"])
        for key, value in pub.items():
            if key in SKIPPED_KEYS:
                continue
            label = key.replace("_", " ").title()
            print(f"\t{label}: {value}")


if __name__ == "__main__":
    main()
