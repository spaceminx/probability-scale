from src.config import DATASETS, RAW_DIR
from src.fetch_data import fetch_json_data, save_raw_json, fetch_xlsx_data, save_raw_xlsx


def main():
    for dataset_code, dataset_info in DATASETS.items():
        data_type = dataset_info["type"]
        url = dataset_info['url']
        category = dataset_info['category']

        print(f'fetching {dataset_code}, {data_type}')

        category_dir = RAW_DIR / category

        if data_type == "json":
            data = fetch_json_data(url)

            filename = f'{dataset_code.lower()}_raw.json'
            output_path = category_dir / filename

            save_raw_json(data, output_path)

        elif data_type == "xlsx":
            data = fetch_xlsx_data(url)

            filename = f'{dataset_code.lower()}_raw.xlsx'
            output_path = category_dir / filename

            save_raw_xlsx(data, output_path)

        else:
            raise ValueError(f"Unknown data type: {data_type}")

        print(f'saved {output_path}')

    print("complete")

if __name__ == "__main__":
    main()