from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

BASE_URL = "https://andmed.stat.ee/api/v1/et/stat/"
CRIME_BASE_URL = "https://www.kriminaalpoliitika.ee/kuritegevus2021/"


DATASETS = {
  "JSS01": {
    "type": "json",
    "url": f"{BASE_URL}JSS01",
    "category": "violence",
  },
  "JSS02": {
    "type": "json",
    "url": f"{BASE_URL}JSS02",
    "category": "violence",
  },
  "JSS21": {
    "type": "json",
    "url": f"{BASE_URL}JSS21",
    "category": "violence",
  },
  "JSS22": {
    "type": "json",
    "url": f"{BASE_URL}JSS22",
    "category": "violence",
  },
  "TS093": {
    "type": "json",
    "url": f"{BASE_URL}TS093",
    "category": "traffic"
  },
  "CRIME_OVERVIEW_2021":{
    "type": "xlsx",
    "url": f"{CRIME_BASE_URL}xlsx/1_Kuritegevuse%20%C3%BClevaade_veebi.xlsx",
    "category": "crime"
  },
}

JSON_REQUEST = {
  "query": [],
  "response": {
    "format": "json-stat2"
  }
}