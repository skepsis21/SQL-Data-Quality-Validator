
import sqlite3
import json

# Load config
with open("config/validation_rules.json", "r") as f:
    rules = json.load(f)

results_summary = []

def run_check(cursor, rule_key, rule):
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


conn = sqlite3.connect("database/sample_company.db")
cursor = conn.cursor()

# Run all rules from config
for key, rule in rules.items():
    run_check(cursor, key, rule)

conn.close()

# FINAL SUMMARY
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