from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

def test():
    print("DAG works")

with DAG(
    dag_id="test_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    PythonOperator(
        task_id="t1",
        python_callable=test
    )