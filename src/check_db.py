import sqlite3

conn = sqlite3.connect("database/sample_company.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

cursor.execute("SELECT * FROM credit_data LIMIT 5;")
print(cursor.fetchall())

conn.close()