import sqlite3
import pandas as pd
import os

# Ensure the database directory exists
os.makedirs("database", exist_ok=True)

file_path = "database/default_of_credit_card_clients.csv"
db_path = "database/sample_company.db"

# ✅ FIX: Use skiprows=1 to ignore the 'X1;X2...' row
# ✅ FIX: Use sep=";" for semicolon delimiter
df = pd.read_csv(file_path, sep=";", encoding="utf-8-sig", skiprows=1)

# Clean column names (strip whitespace)
df.columns = df.columns.str.strip()

# Connect to DB
conn = sqlite3.connect(db_path)

# Load into the specific table 'default_of_credit'
# Using if_exists="replace" ensures a fresh, clean load every time
df.to_sql("default_of_credit", conn, if_exists="replace", index=False)

conn.close()

print("✅ Data loaded successfully.")
print("Columns:", df.columns.tolist())
print("Shape:", df.shape)