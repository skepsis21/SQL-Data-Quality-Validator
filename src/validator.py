import os
import sqlite3
import json
import csv
from datetime import datetime

# Path constants
DB_PATH = "database/sample_company.db"
RULES_PATH = "config/validation_rules.json"

def run_validation():
    # Ensure environment is ready
    os.makedirs("reports", exist_ok=True)
    
    # Load Rules
    with open(RULES_PATH, "r") as f:
        rules = json.load(f)

    results_summary = []
    
    # DB Connection
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Execution Loop
    for key, rule in rules.items():
        cursor.execute(rule["query"])
        results = cursor.fetchall()
        status = "FAIL" if results else "PASS"
        results_summary.append((rule["name"], status, rule.get("severity", "WARNING")))
        
        print(f"{status} - {rule['name']}")

    conn.close()
    return results_summary

def save_reports(results_summary):
    # CSV Export
    with open("reports/validation_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Rule", "Status", "Severity"])
        writer.writerows(results_summary)
    
    # HTML Export (Simplified structure for better rendering)
    # [Insert the generate_html_report logic here...]
    print("✅ Reports generated in /reports directory")

if __name__ == "__main__":
    summary = run_validation()
    save_reports(summary)