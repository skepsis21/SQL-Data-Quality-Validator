import sqlite3

conn = sqlite3.connect("database/sample_company.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(credit_data);")
print(cursor.fetchall())

conn.close()