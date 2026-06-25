import sqlite3
import os

def setup_database():
    # Ensure the directory exists
    os.makedirs('database', exist_ok=True)
    db_path = os.path.join('database', 'sample_company.db')
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create the table matching the structure of default_of_credit_card_clients.csv
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS default_of_credit (
            ID INTEGER PRIMARY KEY,
            LIMIT_BAL REAL,
            SEX INTEGER,
            EDUCATION INTEGER,
            MARRIAGE INTEGER,
            AGE INTEGER,
            PAY_0 INTEGER,
            PAY_2 INTEGER,
            PAY_3 INTEGER,
            PAY_4 INTEGER,
            PAY_5 INTEGER,
            PAY_6 INTEGER,
            BILL_AMT1 REAL,
            BILL_AMT2 REAL,
            BILL_AMT3 REAL,
            BILL_AMT4 REAL,
            BILL_AMT5 REAL,
            BILL_AMT6 REAL,
            PAY_AMT1 REAL,
            PAY_AMT2 REAL,
            PAY_AMT3 REAL,
            PAY_AMT4 REAL,
            PAY_AMT5 REAL,
            PAY_AMT6 REAL,
            default_payment_next_month INTEGER
        )
    ''')
    
    conn.commit()
    conn.close()
    print(f"✅ Table 'default_of_credit' initialized successfully in {db_path}")

if __name__ == "__main__":
    setup_database()