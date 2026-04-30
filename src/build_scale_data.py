import pandas as pd

from src.prob_scale_events.violence_events import build_violent_events
from src.prob_scale_events.traffic_events import build_traffic_events
from src.prob_scale_events.crime_events import build_crime_events

def build_probability_scale():
    df_violence = build_violent_events()
    df_traffic = build_traffic_events()
    df_crime = build_crime_events()

    df = pd.concat([
        df_violence,
        df_traffic,
        df_crime,
    ], ignore_index=True)

    print(df.to_string())

    return df.sort_values("probability", ascending=False)