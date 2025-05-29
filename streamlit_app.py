import streamlit as st
import pandas as pd

# Mocked data quality check
def run_checks():
    df = pd.DataFrame({
        "fare_amount": [10.5, None, 12.0, None, 15.0, 20.0]
    })

    null_report = df.isnull().sum() / len(df) * 100
    duplicate_count = df.duplicated().sum()
    row_count = len(df)

    return {
        "null_percentage": null_report.to_dict(),
        "duplicate_count": duplicate_count,
        "row_count": row_count
    }

# Mocked LLM summary
def summarize(report):
    return f"Fare amount has {report['null_percentage'].get('fare_amount', 0):.1f}% nulls. "            f"{report['duplicate_count']} duplicates. Data is mostly clean."

st.set_page_config(page_title="Smart DQA", layout="wide")
st.title("📊 Smart Data Quality Analyzer")

report = run_checks()
report["summary"] = summarize(report)

st.json(report)
st.markdown("### 🧠 AI Summary")
st.info(report["summary"])
