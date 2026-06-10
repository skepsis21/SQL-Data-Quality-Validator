import os
import sqlite3
import json
import csv
from datetime import datetime

# -------------------------
# SETUP (safe folders)
# -------------------------
os.makedirs("config", exist_ok=True)
os.makedirs("database", exist_ok=True)
os.makedirs("reports", exist_ok=True)

print("\n==============================")
print(" DATA QUALITY VALIDATOR RUN ")
print("==============================\n")

# Load validation rules
with open("config/validation_rules.json", "r") as f:
    rules = json.load(f)

results_summary = []

# -------------------------
# CORE FUNCTION
# -------------------------
def run_check(cursor, rule):
    print(f"\nRunning {rule['name']}...")

    cursor.execute(rule["query"])
    results = cursor.fetchall()

    if results:
        print(f"FAIL - {rule['name']} issues found:")
        for r in results:
            print(r)
        results_summary.append((rule["name"], "FAIL"))
    else:
        print(f"PASS - {rule['name']}")
        results_summary.append((rule["name"], "PASS"))


# -------------------------
# DATABASE CONNECTION
# -------------------------
conn = sqlite3.connect("database/sample_company.db")
cursor = conn.cursor()

# -------------------------
# RUN ALL RULES
# -------------------------
for key, rule in rules.items():
    run_check(cursor, rule)

conn.close()

# -------------------------
# FINAL SUMMARY
# -------------------------
print("\n\n===== VALIDATION SUMMARY =====")

failed = False

for name, status in results_summary:
    print(f"{name} → {status}")
    if status == "FAIL":
        failed = True

if failed:
    print("\nOVERALL STATUS: FAILED ❌")
else:
    print("\nOVERALL STATUS: PASSED ✅")

# -------------------------
# CSV REPORT EXPORT
# -------------------------
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("reports/validation_report.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Validation Report"])
    writer.writerow([f"Generated at: {timestamp}"])
    writer.writerow([])

    writer.writerow(["Rule", "Status"])

    for name, status in results_summary:
        writer.writerow([name, status])

print("\nReport saved to reports/validation_report.csv")