import streamlit as st

st.set_page_config(page_title="Smart DQA", layout="wide")
st.title("📊 Smart Data Quality Analyzer")

report = {
    "null_percentage": {"fare_amount": 2.5},
    "duplicate_count": 3,
    "row_count": 1000,
    "summary": "Fare amount has 2.5% nulls. No duplicates. Data is mostly clean."
}

st.json(report)
st.markdown("### 🧠 AI Summary")
st.info(report["summary"])
