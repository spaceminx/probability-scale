import os

from src.config import RAW_DIR, PROCESSED_DIR
from src.process_crime_data import process_crime_data


def main():
    input_dir = RAW_DIR / "crime"
    out_dir = PROCESSED_DIR / "crime"

    for filename in os.listdir(input_dir):
        if not filename.endswith(".xlsx"):
            continue

        in_path = input_dir / filename

        out_filename = filename.replace("_raw.xlsx", "_clean.csv")
        out_path = out_dir / out_filename

        process_crime_data(in_path, out_path)

        print(f"saved {out_filename}")

    print("complete")

if __name__ == "__main__":
    main()