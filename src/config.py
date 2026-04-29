from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

BASE_URL = "https://andmed.stat.ee/api/v1/et/stat/"

DATASETS = {
  "JSS01": {
    "url": f"{BASE_URL}JSS01",
    "category": "violence",
  },
  "JSS02": {
    "url": f"{BASE_URL}JSS02",
    "category": "violence",
  },
  "JSS21": {
    "url": f"{BASE_URL}JSS21",
    "category": "violence",
  },
  "JSS22": {
    "url": f"{BASE_URL}JSS22",
    "category": "violence",
  },
  "TS093": {
    "url": f"{BASE_URL}TS093",
    "category": "traffic"
  },
}

JSON_REQUEST = {
  "query": [],
  "response": {
    "format": "json-stat2"
  }
}