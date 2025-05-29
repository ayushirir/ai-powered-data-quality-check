from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.data_quality_checks import run_checks
from scripts.generate_summary import summarize

def check_data():
    return run_checks()

def summarize_data(ti):
    report = ti.xcom_pull(task_ids='check_data')
    print(summarize(report))

with DAG("dqa_dag", start_date=datetime(2023,1,1), schedule_interval="@daily", catchup=False) as dag:
    t1 = PythonOperator(task_id="check_data", python_callable=check_data)
    t2 = PythonOperator(task_id="summarize_data", python_callable=summarize_data)
    t1 >> t2
