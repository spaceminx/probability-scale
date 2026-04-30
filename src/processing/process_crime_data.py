import pandas as pd


def clean_crime_df(df):
    df = df.dropna(how='all').dropna(axis=1, how='all')

    header_row = df[df.apply(lambda row : row.astype(str).str.contains("Aasta").any(), axis=1)].index[0]

    headers = df.loc[header_row].to_list()
    df = df.loc[header_row + 1:].copy()
    df.columns = headers

    first_col = df.columns[0]
    df = df.rename(columns={first_col : "crime_type"})

    df["crime_type"] = df["crime_type"].ffill()

    df = df[["crime_type", "Aasta", "EESTI"]]

    df = df.rename(columns={
        "Aasta" : "year",
        "EESTI" : "rate_per_10000"
    })

    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df["rate_per_10000"] = pd.to_numeric(df["rate_per_10000"], errors="coerce")

    df = df.dropna(subset=["year", "rate_per_10000"])
    df["year"] = df["year"].astype(int)

    return df


def get_latest_year(df):
    latest_year = df["year"].max()
    df = df[df["year"] == latest_year].copy()
    return df


def add_probability_columns(df):
    df = df.copy()

    df["probability"] = (df["rate_per_10000"] / 10000).round(4)
    df["one_in"] = (1 / df["probability"]).round(2)

    return df

def process_crime_data(in_path, out_path):
    df = pd.read_excel(
        in_path,
        sheet_name="10 000 el mk"
    )
    df = clean_crime_df(df)
    df = get_latest_year(df)
    df = add_probability_columns(df)

    df.to_csv(out_path, index=False)