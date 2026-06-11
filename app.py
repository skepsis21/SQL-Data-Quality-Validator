import streamlit as st
import subprocess
import pandas as pd

st.title("📊 SQL Data Quality Validator")

st.write("Run your data validation engine and view results in real time.")

# -------------------------
# RUN VALIDATOR BUTTON
# -------------------------
if st.button("Run Validation"):
    with st.spinner("Running validation..."):
        result = subprocess.run(
            ["python", "src/validator.py"],
            capture_output=True,
            text=True
        )

    st.subheader("📟 Console Output")
    st.text(result.stdout)

    if result.stderr:
        st.error(result.stderr)

# -------------------------
# LOAD REPORT
# -------------------------
st.subheader("📄 Latest CSV Report")

try:
    df = pd.read_csv("reports/validation_report.csv")
    st.dataframe(df)
except Exception as e:
    st.warning("No report found yet. Run validation first.")

# -------------------------
# SHOW HTML REPORT
# -------------------------
st.subheader("🌐 HTML Report")

try:
    with open("reports/validation_report.html", "r") as f:
        html_content = f.read()

    st.components.v1.html(html_content, height=600, scrolling=True)

except:
    st.warning("HTML report not found. Run validation first.")