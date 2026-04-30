import pandas as pd
from config import RAW_DIR
file_path = f"{RAW_DIR}/crime/crime_overview_2021_raw.xlsx"

excel_file = pd.ExcelFile(file_path)
print(excel_file.sheet_names)