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
        (df_women["group"] == "Koges viimase 12 kuu jooksul")
    ].copy()

    women["event"] = "Experienced intimate partner violence (women, last 12 months)"
    women["category"] = "violence"
    women["source"] = "JSS01"

    men = df_men[
        (df_men["indicator"] == men_indicator_name) &
        (df_men["group"] == "Koges viimase 12 kuu jooksul")
        ].copy()

    men["event"] = "Experienced intimate partner violence (men, last 12 months)"
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