# SQL Data Quality Validator

A Python and SQL-based data validation framework that automatically checks database integrity and generates structured reports before data is used for analysis or reporting.

---

## 📊 Overview

In real-world analytics workflows, data must be validated before it is used for dashboards, reporting, or decision-making.

Poor data quality can lead to incorrect insights, broken dashboards, and unreliable business decisions.

This tool simulates a real data validation layer by running automated SQL-based checks on a database and producing a structured report of data quality issues.

It acts as a **pre-analysis validation step** commonly found in analytics engineering workflows.

---

## ⚙️ What This Tool Does

This validator automatically:

- Detects duplicate records in key fields  
- Identifies missing (NULL) values in critical columns  
- Validates numeric ranges and constraints  
- Checks referential integrity between tables  
- Flags unexpected or inconsistent values  
- Generates a structured validation report (CSV)

---

## 🧠 Key Concept

This project is based on a simple principle:

> “Data should be validated before it is analyzed.”

It demonstrates how analysts ensure data reliability before building dashboards or reports.

---

## 🛠️ Technologies Used

- Python (automation & orchestration)
- SQL (data validation queries)
- SQLite (database engine)
- JSON (configuration-driven rules)
- Git & GitHub (version control)

---

## 📁 Project Structure

```text
SQL-Data-Quality-Validator/
│
├── config/                 # Validation rules (JSON)
├── database/               # Sample SQLite database
├── reports/                # Generated validation reports
├── sql/                    # SQL validation queries
├── src/                    # Python validator engine
├── README.md