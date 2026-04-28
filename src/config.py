from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

BASE_URL = "https://andmed.stat.ee/api/v1/et/stat/"

DATASET_URLS = {
  "JSS01": f"{BASE_URL}JSS01",
  "JSS02": f"{BASE_URL}JSS02",
  "JSS21": f"{BASE_URL}JSS21",
  "JSS22": f"{BASE_URL}JSS22",
}

JSON_REQUEST = {
  "query": [],
  "response": {
    "format": "json-stat2"
  }
}