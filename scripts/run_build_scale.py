from src.build_scale_data import build_probability_scale
from src.config import RESULTS_DIR


def main():
    df = build_probability_scale()

    output_path = RESULTS_DIR / "probability_scale.csv"

    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    main()