👉 clone it
👉 install dependencies
👉 run it
👉 immediately see results

No confusion, no missing steps.

📊 SQL Data Quality Validator

A Python and SQL-based data validation framework that automatically checks database integrity and generates structured reports before data is used for analysis or reporting.

🚀 What This Project Does

This tool simulates a real-world data quality validation pipeline used in analytics and data engineering workflows.

It:

Loads a CSV dataset into SQLite
Runs SQL-based validation rules (JSON-driven)
Detects data quality issues
Generates structured reports (CSV + HTML)
Computes a data quality score
Provides an interactive Streamlit dashboard
⚙️ Features
✔ Duplicate detection
✔ Null value validation
✔ Outlier detection
✔ Target variable validation
✔ Configurable JSON-based rule engine
✔ Automated scoring system (0–100)
✔ HTML + CSV reporting
✔ Streamlit dashboard UI
🧠 Key Concept

“Data must be validated before it is analyzed.”

This project demonstrates how raw datasets are transformed into validated, analysis-ready data.

📁 Project Structure
SQL-Data-Quality-Validator/
│
├── config/
│   └── validation_rules.json      # Validation rules (SQL-based)
│
├── database/
│   ├── sample_company.db          # SQLite database
│   └── default_of_credit_card_clients.csv
│
├── reports/
│   ├── validation_report.csv
│   └── validation_report.html
│
├── src/
│   ├── load_data.py               # Loads CSV → SQLite
│   ├── validator.py              # Core validation engine
│
├── app.py                         # Streamlit dashboard
├── run.py                         # One-command runner (optional)
├── README.md
⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/SQL-Data-Quality-Validator.git
cd SQL-Data-Quality-Validator
2. Create virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
3. Install dependencies
pip install -r requirements.txt
📦 Requirements

Create a requirements.txt file with:

pandas
streamlit

(SQLite is built into Python)

🚀 How to Run the Project
Step 1 — Load Data
python src/load_data.py
Step 2 — Run Validation Engine
python src/validator.py

This generates:

CSV report → reports/validation_report.csv
HTML report → reports/validation_report.html
Step 3 — Launch Dashboard
streamlit run app.py
🌐 Streamlit Dashboard

The dashboard allows you to:

Run validation interactively
View data quality score
Inspect failed rules
View full results table
Render HTML report inside browser
📊 Example Output
Terminal Output
Duplicate Row Check → FAIL (CRITICAL)
Null Check → PASS (WARNING)
Outlier Check → FAIL (WARNING)

OVERALL STATUS: CRITICAL FAILURE ❌
📈 Data Quality Score
Score = 100 - (Critical Issues × 25 + Failed Checks × 10)

Example:

Data Quality Score: 72 / 100
Critical Issues: 2
Failed Checks: 4
🌐 HTML Report

Generated automatically:

📄 reports/validation_report.html

Includes:

Score summary
PASS / FAIL breakdown
Severity labels
Full rule results table
🧾 Validation Rule Schema

Rules are fully configurable via JSON:

{
  "rule_name": {
    "name": "Human readable rule name",
    "severity": "CRITICAL | WARNING",
    "query": "SQL query executed on dataset"
  }
}
🧪 Example Rule Types
Duplicate detection (GROUP BY + HAVING COUNT)
Null checks (IS NULL)
Outlier detection (range filters)
Target variable validation
▶️ One-Command Run (Optional)

If using run.py:

python run.py

This will:

Load data
Run validation
Launch Streamlit dashboard
🎯 Why This Project Matters

This project simulates a real-world data quality layer used in:

Data engineering pipelines
Analytics workflows
BI systems
Data warehousing validation layers

It ensures data is validated before analysis, improving reliability and trust.

🚀 Key Takeaways
Rule-based validation system (config-driven)
SQL used as validation engine
Automated reporting pipeline
Interactive dashboard (Streamlit)
Real-world data engineering workflow simulation
🧠 Future Improvements
PostgreSQL support
Docker containerization
Auto schema detection
Data profiling module
Anomaly detection (ML-based)
Cloud deployment (Render / Railway)
📌 Status

🚧 Work in Progress — actively evolving as a data engineering portfolio project.