from src.config import DATASETS, RAW_DIR
from src.fetch_data import fetch_data, save_raw_json

def main():
    for dataset_code, dataset_info in DATASETS.items():
        url = dataset_info['url']
        category = dataset_info['category']

        print(f'fetching {dataset_code}')

        data = fetch_data(url)

        category_dir = RAW_DIR / category

        filename = f'{dataset_code.lower()}_raw.json'
        output_path = category_dir / filename

        save_raw_json(data, output_path)

        print(f'saved {output_path}')

    print("complete")

if __name__ == "__main__":
    main()