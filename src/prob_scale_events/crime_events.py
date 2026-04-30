import pandas as pd

from src.config import PROCESSED_DIR

def load_crime_data():
    path = PROCESSED_DIR / "crime" / "crime_overview_2021_clean.csv"
    return pd.read_csv(path)

def build_crime_events():
    df = load_crime_data()

    theft = df[
        df["crime_type"] == "§ 199  Vargus"
    ].copy()

    crime_against_person = df[
        df["crime_type"] == "Isikuvastased kuriteod"
    ].copy()

    theft["event"] = "Experienced theft"
    crime_against_person["event"] = "Experienced crime against person"

    theft["category"] = "crime"
    crime_against_person["category"] = "crime"

    theft["source"] = "CRIME_OVERVIEW_2021"
    crime_against_person["source"] = "CRIME_OVERVIEW_2021"

    combined = pd.concat(
        [theft, crime_against_person],
        ignore_index=True
    )

    return combined[[
        "event",
        "category",
        "probability",
        "one_in",
        "year",
        "source",
    ]]