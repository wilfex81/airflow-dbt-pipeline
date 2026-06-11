from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="dbt_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    run_dbt = BashOperator(
        task_id="run_dbt",
        bash_command="cd /home/thecollective/Data_E/dbt_project/analytics && dbt run"
    )

    test_dbt = BashOperator(
        task_id="test_dbt",
        bash_command="cd /home/thecollective/Data_E/dbt_project/analytics && dbt test"
    )

    run_dbt >> test_dbt