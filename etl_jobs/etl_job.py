import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO, format= '%(asctime)s - %(levelname)s - %(message)s')

# Absolute project path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # This gets the project root (cloud-ETL)

# Input and Output paths (absolute)
input_path = os.path.join(project_root, 'data/raw/sales_data.csv')
output_path = os.path.join(project_root, 'data/processed/cleaned_sales_data.csv')

os.makedirs(os.path.dirname(output_path), exist_ok= True)

try:
    df = pd.read_csv(input_path)
    logging.info(f"File loaded successfully {input_path}")
except Exception as e:
    logging.error(f"File Not loaded successfully {input_path}")
    exit(1)

df = df.dropna()

# Changing the date format to dd/mm/yyyy
df["Date"] = pd.to_datetime(df["Date"])
df["Date"] = df["Date"].dt.strftime("%d/%m/%Y")

# Sorting data based on date
sorted_df = df.sort_values(by= "Date", ascending= True)

sorted_df["Sale_ID"] = [f"S{i:03}" for i in range (1, len(sorted_df)+1)]

sorted_df.to_csv(output_path, index=False)

logging.info(f"ETL Completed. Cleaned data written to: {output_path}")


