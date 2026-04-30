import pandas as pd

from src.config import PROCESSED_DIR

def load_traffic_data():
    path = PROCESSED_DIR / "traffic" / "ts093_clean.csv"
    return pd.read_csv(path)


def build_traffic_events():
    df = load_traffic_data()

    deaths = df.loc[
        df["indicator"] == "Hukkunud",
        "value"
    ].iloc[0]

    injured = df.loc[
        df["indicator"] == "Vigasaanud",
        "value"
    ].iloc[0]

    probability = deaths / (deaths + injured)
    year = df["year"].max()

    traffic = pd.DataFrame([{
        "event": "Death among injured participants in traffic accidents",
        "category": "traffic",
        "probability": probability.round(4),
        "one_in": (1 / probability).round(2),
        "year": year,
        "source": "TS093"
    }])

    return traffic