import requests
import json

from src.config import RAW_DIR, JSON_REQUEST

def fetch_data(url):
    """
    Fetch dataset from Statistics Estonia API.
    :param url: API endpoint URL
    :return: raw JSON response
    """
    response = requests.post(
        url,
        json=JSON_REQUEST
    )
    response.raise_for_status()

    return response.json()

def save_raw_json(data, filename):
    """
    Save raw JSON to file.
    :param data: Raw JSON
    :param filename: Output filename
    """
    output_path = RAW_DIR / filename

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )



