import pandas as pd

from src.config import PROCESSED_DIR

def load_violence_data():
    women_path = PROCESSED_DIR / "violence" / "jss01_clean.csv"
    men_path = PROCESSED_DIR / "violence" / "jss21_clean.csv"

    df_women = pd.read_csv(women_path)
    df_men = pd.read_csv(men_path)

    return df_women, df_men

def build_violent_events():
    df_women, df_men = load_violence_data()

    women_indicator_name = "Paarisuhtes olnud 18-74-aastaste naiste osatähtsus, kes on elu jooksul kogenud intiimpartneri vaimset, füüsilist (sh ähvardamine) või seksuaalset vägivalda, %"
    men_indicator_name = "Paarisuhtes olnud 18-74-aastaste meeste osatähtsus, kes on elu jooksul kogenud intiimpartneri vaimset, füüsilist (sh ähvardamine) või seksuaalset vägivalda, %"

    women = df_women[
        (df_women["indicator"] == women_indicator_name) &
        (df_women["group"] == "Kokku")
    ].copy()

    women["event"] = "Experienced intimate partner violence (women, lifetime)"
    women["category"] = "violence"
    women["source"] = "JSS01"

    men = df_men[
        (df_men["indicator"] == men_indicator_name) &
        (df_men["group"] == "Kokku")
        ].copy()

    men["event"] = "Experienced intimate partner violence (men, lifetime)"
    men["category"] = "violence"
    men["source"] = "JSS21"

    combined = pd.concat([women, men], ignore_index=True)

    return combined[[
        "event",
        "category",
        "probability",
        "one_in",
        "year",
        "source"
    ]]


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


def main():
    df_violence = build_violent_events()
    df_traffic = build_traffic_events()
    df_crime = build_crime_events()
    df = pd.concat([
        df_violence,
        df_traffic,
        df_crime,
    ], ignore_index=True)

    print(df.to_string())

if __name__ == "__main__":
    main()