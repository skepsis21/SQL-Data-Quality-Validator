# SQL-Data-Quality-Validator
Python-powered SQL data quality validator for automated database integrity checks.

## Overview

Poor data quality can lead to inaccurate reports, unreliable dashboards, and poor business decisions. This project provides an automated validation framework that runs SQL-based data quality checks against a database and generates a summary report of any issues found.

Instead of manually writing and executing validation queries, users can run the validator to perform multiple checks in a single command.

## Features

- Detect duplicate records
- Check for NULL values in required columns
- Validate numeric ranges
- Verify referential integrity (foreign keys)
- Identify unexpected values
- Generate validation reports
- Easily extend validation rules with additional SQL files

## Technologies

- Python
- SQL
- SQLite
- Git

## Project Structure

```text
SQL-Data-Quality-Validator/
│
├── config/
├── database/
├── reports/
├── sql/
├── src/
├── README.md
└── requirements.txt
```

## Planned Workflow

```text
Database
    │
    ▼
Python Validator
    │
    ├── Duplicate Check
    ├── NULL Check
    ├── Range Check
    ├── Foreign Key Check
    │
    ▼
Validation Report
```

## Future Improvements

- Configurable validation rules using JSON
- HTML report generation
- Logging system
- Support for PostgreSQL and SQL Server
- Command-line interface (CLI)
- Unit tests

## Learning Goals

This project is designed to strengthen practical skills in:

- SQL
- Python automation
- Database validation
- Project organization
- Git and GitHub
- Writing maintainable code

## Status

🚧 **Work in Progress**

This project is actively being developed as part of my data analytics portfolio.