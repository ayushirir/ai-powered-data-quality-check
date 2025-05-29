# 🧠 Smart Data Quality Analyzer – Project Documentation

## 🎯 Project Goal

To build a real-world, AI-powered, cloud-ready tool that:
- ✅ Analyzes datasets for common data quality issues
- ✅ Uses a Large Language Model (LLM) to generate plain-English summaries
- ✅ Shows results in a professional, interactive dashboard (Streamlit)
- ✅ Can optionally be automated with Airflow and cloud services like BigQuery

---

## 🗂️ Project Structure

```
smart_data_quality_analyzer/
├── streamlit_app.py              # Main dashboard script
├── scripts/
│   ├── data_quality_checks.py    # Quality check logic
│   └── generate_summary.py       # LLM summary logic
├── requirements.txt              # Python dependencies
├── .gitignore                    # Ignore temp files
```

---

## ✅ Step-by-Step Breakdown

### 🔹 STEP 1: Create Data Quality Checks

**File:** `scripts/data_quality_checks.py`

**What It Does:**
- Analyzes a dataset for:
  - % of null values
  - Number of duplicate rows
  - Total row count

**Why:**
- These are the first and most essential checks in any real-world data pipeline.

**Tech Used:** `pandas`

**Code:**
```python
import pandas as pd

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
```

---

### 🔹 STEP 2: Generate a Natural-Language Summary

**File:** `scripts/generate_summary.py`

**What It Does:** Uses LLM (e.g., GPT via OpenRouter) to summarize results.

**Tech Used:** `streamlit.secrets`, `requests`, `OpenRouter API`

**Code:**
```python
import streamlit as st
import requests, json

OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]

def summarize(report):
    prompt = f"Summarize this data quality report: {json.dumps(report)}"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistralai/mixtral-8x7b-instruct",
        "messages": [{"role": "user", "content": prompt}]
    }
    r = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    return r.json()["choices"][0]["message"]["content"]
```

---

### 🔹 STEP 3: Display in Streamlit Dashboard

**File:** `streamlit_app.py`

**What It Does:** Displays quality checks and LLM summary in an interactive UI

**Tech Used:** `Streamlit`

**Code:**
```python
import streamlit as st
from scripts.data_quality_checks import run_checks
from scripts.generate_summary import summarize

st.set_page_config(page_title="Smart DQA", layout="wide")
st.title("📊 Smart Data Quality Analyzer")

report = run_checks()
report["summary"] = summarize(report)

st.json(report)
st.markdown("### 🧠 AI Summary")
st.info(report["summary"])
```

---

## 🔐 Streamlit Secret Management

**File:** `.streamlit/secrets.toml`

```toml
OPENROUTER_API_KEY = "your_openrouter_api_key_here"
```

---

## 🚀 Deployment Steps

1. Push to GitHub
2. Deploy on Streamlit Cloud
3. Set main file: `streamlit_app.py`
4. Add secret in app → Settings → Secrets

Live Demo: [Visit App](https://ai-powered-data-quality-check-35rurwi7wvhfk58khqv9h4.streamlit.app/)

---

## ✅ What This Project Demonstrates

| Skill                      | Demonstrated? |
|----------------------------|---------------|
| Python (pandas, requests)  | ✅ Yes         |
| Streamlit dashboards       | ✅ Yes         |
| LLM integration (OpenRouter)| ✅ Yes        |
| Secure secret management   | ✅ Yes         |
| Cloud deployment           | ✅ Yes         |
| Clean code + documentation | ✅ Yes         |

---

## 🧭 Future Enhancements

| Feature                   | Reason to Add                              |
|---------------------------|---------------------------------------------|
| BigQuery integration      | For real-time analysis of cloud data        |
| Airflow DAG               | Scheduled, production-ready automation      |
| Table selector in UI      | Let users analyze any dataset               |

