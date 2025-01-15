from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from scripts.etl import extract, transform, load

default_args = {
    'owner': 'Ahmed Nasri',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'start_date': datetime(2025, 1, 1),
}

dag = DAG(
    'etl_pipeline',
    default_args=default_args,
    description='ETL pipeline with Airflow and Pandas',
    schedule_interval='@daily',
)

extract_task = PythonOperator(
    task_id='extract',
    python_callable=extract,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform',
    python_callable=transform,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load',
    python_callable=load,
    dag=dag,
)

extract_task >> transform_task >> load_task
