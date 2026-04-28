from src.config import DATASET_URLS
from src.fetch_data import fetch_data, save_raw_json

def main():
    for dataset_code, url in DATASET_URLS.items():
        print(f'fetching {dataset_code}')

        data = fetch_data(url)
        filename = f'{dataset_code.lower()}_raw.json'

        save_raw_json(data, filename)

        print(f'saved {filename}')

    print("complete")

if __name__ == "__main__":
    main()