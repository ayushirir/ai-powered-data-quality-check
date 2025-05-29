from google.cloud import bigquery
import pandas as pd

def run_checks():
    client = bigquery.Client()
    query = "SELECT * FROM `your_project.dqa_dataset.sample_data`"
    df = client.query(query).to_dataframe()

    null_report = df.isnull().sum() / len(df) * 100
    duplicate_count = df.duplicated().sum()

    return {
        "null_percentage": null_report.to_dict(),
        "duplicate_count": duplicate_count,
        "row_count": len(df)
    }

if __name__ == "__main__":
    print(run_checks())
