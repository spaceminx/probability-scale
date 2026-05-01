import pandas as pd

from src.config import RESULTS_DIR
from src.plotting import plot_probability_scale

def main():
    in_path = RESULTS_DIR / "probability_scale.csv"
    out_path = RESULTS_DIR / "probability_scale.png"

    df = pd.read_csv(in_path)

    plot_probability_scale(df, out_path)

if __name__ == "__main__":
    main()