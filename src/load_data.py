import sqlite3
import pandas as pd

file_path = "database/default_of_credit_card_clients.csv"

# ✅ FIX: correct delimiter is semicolon
df = pd.read_csv(file_path, sep=";", encoding="utf-8-sig")

# clean column names
df.columns = df.columns.str.strip()

# connect DB
conn = sqlite3.connect("database/sample_company.db")

# load table
df.to_sql("credit_data", conn, if_exists="replace", index=False)

conn.close()

print("Loaded successfully")
print("Columns:", df.columns.tolist())
print("Shape:", df.shape)