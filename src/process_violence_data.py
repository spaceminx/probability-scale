import json

import pandas as pd
from src.config import RAW_DIR
from src.json_to_df import json_to_df


def load_violence_json(file_path):
    #path = RAW_DIR / "violence" / filename
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def clean_violence_df(df):
    df = df.rename(columns={
        "Näitaja": "indicator",
        "Isikute rühm": "group",
        "Vaatlusperiood": "year",
        "value": "percent",
    })

    df = df.dropna(subset=["percent"])

    return df

def add_probability_columns(df):
    df = df.copy()

    df["probability"] = (df["percent"] / 100).round(4)
    df["one_in"] = (1 / df["probability"]).round(2)

    return df

def process_violence_file(in_path, out_path):
    raw_data = load_violence_json(in_path)

    df = json_to_df(raw_data)
    df = clean_violence_df(df)
    df = add_probability_columns(df)

    df.to_csv(out_path, index=False)

