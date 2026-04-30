import json

from src.json_to_df import json_to_df

def load_traffic_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def clean_traffic_df(df):
    df = df.rename(columns={
        "Näitaja": "indicator",
        "Kuu": "month",
        "Aasta": "year",
    })

    df = df.dropna(subset=["value"])
    df["year"] = df["year"].astype(int)

    return df

def get_latest_annual_total(df):
    latest_year = df["year"].max()

    return df[
        (df["year"] == latest_year) &
        (df["month"] == "Kasvavalt kokku")
    ].copy()

def process_traffic_file(in_path, out_path):
    raw_data = load_traffic_json(in_path)

    df = json_to_df(raw_data)
    df = clean_traffic_df(df)
    df = get_latest_annual_total(df)

    df.to_csv(out_path, index=False)