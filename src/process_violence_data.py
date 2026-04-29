import json

import pandas as pd
from config import RAW_DIR

def load_raw_json(filename):
    path = RAW_DIR / filename
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def json_to_df(json_file):
    dimension_names = json_file["id"]
    values = json_file["value"]

    categories = []

    for dimension in dimension_names:
        category = json_file["dimension"][dimension]["category"]
        labels = category["label"]

        categories.append(labels)

    indicators = categories[0]
    groups = categories[1]
    years = categories[2]

    indicators = list(indicators.values())
    groups = list(groups.values())
    years = list(years.values())

    rows = []

    for i in range(len(values)):
        indicator_index = i // len(groups)
        group_index = i % len(groups)

        row = {
            "indicator": indicators[indicator_index],
            "group": groups[group_index],
            "year": years[0],
            "percent": values[i],
        }
        rows.append(row)

    df = pd.DataFrame(rows)

    return df

