import sqlite3

conn = sqlite3.connect("database/sample_company.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(credit_data);")
columns = cursor.fetchall()

print("\nTABLE SCHEMA:")
for col in columns:
    print(col)

conn.close()