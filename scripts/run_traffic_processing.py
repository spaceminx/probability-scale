import os

from src.config import RAW_DIR, PROCESSED_DIR
from src.processing.process_traffic_data import process_traffic_file


def main():
    input_dir = RAW_DIR / "traffic"
    out_dir = PROCESSED_DIR / "traffic"

    for filename in os.listdir(input_dir):
        if not(filename.endswith(".json")):
            continue

        input_path = input_dir / filename

        out_filename = filename.replace("_raw.json", "_clean.csv")
        out_path = out_dir / out_filename

        process_traffic_file(input_path, out_path)

        print(f"saved {out_filename}")

    print("complete")

if __name__ == "__main__":
    main()