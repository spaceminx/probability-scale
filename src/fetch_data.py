import requests
import json

from src.config import RAW_DIR, JSON_REQUEST

# --- JSON ---
def fetch_json_data(url):
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

def save_raw_json(data, output_path):
    """
    Save raw JSON to file.
    :param data: Raw JSON
    :param output_path: Output path
    """

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )

# --- XLSX ---

def fetch_xlsx_data(url):
    response = requests.get(url)
    response.raise_for_status()

    return response.content

def save_raw_xlsx(data, output_path):
    with open(output_path, "wb") as f:
        f.write(data)

