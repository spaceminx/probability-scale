from itertools import product

import pandas as pd


def get_labels(json_file, dimension):
    category = json_file["dimension"][dimension]["category"]
    labels = category["label"]
    index = category["index"]

    return [
        labels[code] for code in sorted(index, key=index.get)
    ]

def json_to_df(json_file):
    dimension_names = json_file["id"]
    values = json_file["value"]

    labels_by_dimension = []

    for dimension in dimension_names:
        labels = get_labels(json_file, dimension)
        labels_by_dimension.append(labels)

    rows = []
    for combination, value in zip(product(*labels_by_dimension), values):
        row = {}

        for i in range(len(dimension_names)):
            row[dimension_names[i]] = combination[i]

        row["value"] = value
        rows.append(row)

    return pd.DataFrame(rows)