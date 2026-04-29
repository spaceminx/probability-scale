from src.process_violence_data import load_raw_json, json_to_df

def main():
    raw_jss01 = load_raw_json("jss01_raw.json")

    df_jss01 = json_to_df(raw_jss01)
    print(df_jss01.to_string())

if __name__ == "__main__":
    main()