import streamlit as st
import pandas as pd
import subprocess

st.title("Data Quality Dashboard")

if st.button("Run Data Validation"):
    # Trigger the validator script
    subprocess.run(["python", "src/validator.py"])
    st.success("Validation complete! Check the reports/ folder.")

# Display current results
if st.button("Load Report"):
    df = pd.read_csv("reports/validation_report.csv")
    st.table(df)