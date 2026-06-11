import os
import sqlite3
import json
import csv
from datetime import datetime

# -------------------------
# SETUP
# -------------------------
os.makedirs("config", exist_ok=True)
os.makedirs("database", exist_ok=True)
os.makedirs("reports", exist_ok=True)

print("\n==============================")
print(" DATA QUALITY VALIDATOR RUN ")
print("==============================\n")

# -------------------------
# LOAD RULES
# -------------------------
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

    severity = rule.get("severity", "WARNING")

    if results:
        print(f"{severity} - {rule['name']} issues found:")
        for r in results[:5]:
            print("  - Issue:", r)

        print(f"  Total issues found: {len(results)}")

        results_summary.append((rule["name"], "FAIL", severity))
    else:
        print(f"PASS - {rule['name']}")
        results_summary.append((rule["name"], "PASS", severity))


# -------------------------
# DB CONNECTION
# -------------------------
conn = sqlite3.connect("database/sample_company.db")
cursor = conn.cursor()

# -------------------------
# RUN RULES
# -------------------------
for key, rule in rules.items():
    run_check(cursor, rule)

conn.close()

# -------------------------
# METRICS
# -------------------------
total = len(results_summary)
failed = sum(1 for r in results_summary if r[1] == "FAIL")
critical = sum(1 for r in results_summary if r[1] == "FAIL" and r[2] == "CRITICAL")
passed = total - failed

score = max(0, 100 - (critical * 25 + failed * 10))

print("\n===== METRICS =====")
print(f"Total Checks: {total}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Critical Issues: {critical}")

print("\n===== DATA QUALITY SCORE =====")
print(f"Score: {score}/100")

# -------------------------
# FINAL SUMMARY
# -------------------------
print("\n===== VALIDATION SUMMARY =====")

for name, status, severity in results_summary:
    print(f"{name} → {status} ({severity})")

print("\n----------------------------")

if critical > 0:
    print("OVERALL STATUS: CRITICAL FAILURE ❌")
elif failed > 0:
    print("OVERALL STATUS: FAILED ⚠️")
else:
    print("OVERALL STATUS: PASSED ✅")

# -------------------------
# CSV REPORT
# -------------------------
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("reports/validation_report.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Validation Report"])
    writer.writerow([f"Generated at: {timestamp}"])
    writer.writerow([])
    writer.writerow(["Rule", "Status", "Severity"])

    for name, status, severity in results_summary:
        writer.writerow([name, status, severity])

print("\nCSV report saved to reports/validation_report.csv")

# -------------------------
# HTML REPORT
# -------------------------
def generate_html_report(results_summary):
    total = len(results_summary)
    failed = sum(1 for r in results_summary if r[1] == "FAIL")
    critical = sum(1 for r in results_summary if r[1] == "FAIL" and r[2] == "CRITICAL")

    score = max(0, 100 - (critical * 25 + failed * 10))

    html = f"""
    <html>
    <head>
        <title>Data Quality Report</title>
        <style>
            body {{
                font-family: Arial;
                margin: 30px;
                background-color: #f4f6f8;
            }}
            .container {{
                background: white;
                padding: 20px;
                border-radius: 10px;
            }}
            .score {{
                font-size: 22px;
                font-weight: bold;
                margin-bottom: 20px;
            }}
            .good {{ color: green; }}
            .bad {{ color: red; }}

            table {{
                border-collapse: collapse;
                width: 100%;
                margin-top: 20px;
            }}

            th, td {{
                border: 1px solid #ddd;
                padding: 10px;
                text-align: left;
            }}

            th {{
                background-color: #333;
                color: white;
            }}

            .PASS {{ color: green; font-weight: bold; }}
            .FAIL {{ color: red; font-weight: bold; }}
        </style>
    </head>

    <body>
        <div class="container">

        <h1>Data Quality Validation Report</h1>

        <div class="score {'good' if score >= 80 else 'bad'}">
            Data Quality Score: {score}/100
        </div>

        <p>Total Checks: {total}</p>
        <p>Failed: {failed}</p>
        <p>Critical Issues: {critical}</p>

        <table>
            <tr>
                <th>Rule</th>
                <th>Status</th>
                <th>Severity</th>
            </tr>
    """

    for name, status, severity in results_summary:
        html += f"""
        <tr>
            <td>{name}</td>
            <td class="{status}">{status}</td>
            <td>{severity}</td>
        </tr>
        """

    html += """
        </table>
        </div>
    </body>
    </html>
    """

    with open("reports/validation_report.html", "w") as f:
        f.write(html)

    print("\nHTML report saved to reports/validation_report.html")


# -------------------------
# RUN HTML REPORT
# -------------------------
generate_html_report(results_summary)