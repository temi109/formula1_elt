from datetime import datetime, timedelta
import csv
import logging

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.amazon.aws.hooks.s3 import S3Hook

default_args = {
    'owner': 'tem109',
    'retries': 5,
    'retry_delay' : timedelta(minutes=10)
}

S3_bucket_name = "temi-formula1"


def circuits_upload():
    # query data from postgres db and save into csv file
    
    hook = PostgresHook(postgres_conn_id="postgres_localhost")
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute("select * from circuits")

    with open(f"dags/get_circuits.csv", "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)
        f.flush()
    cursor.close()
    conn.close()
    logging.info("Saved circuits data")
    # then upload to s3
    s3_hook = S3Hook(aws_conn_id = "s3_conn")
    s3_hook.load_file(
        filename = "dags/get_circuits.csv",
        key = "circuits.csv",
        bucket_name = S3_bucket_name,
        replace = True     ## Replace file if already exists
    )

def constructors_upload():
    # query data from postgres db and save into txt file
    
    hook = PostgresHook(postgres_conn_id="postgres_localhost")
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute("select * from constructors")

    with open(f"dags/get_constructors.csv", "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)
        f.flush()
    cursor.close()
    conn.close()
    logging.info("Saved constructors data")
    # then upload to s3
    s3_hook = S3Hook(aws_conn_id = "s3_conn")
    s3_hook.load_file(
        filename = "dags/get_constructors.csv",
        key = "constructors.csv",
        bucket_name = S3_bucket_name,
        replace = True     ## Replace file if already exists
    )

def races_upload():
    hook = PostgresHook(postgres_conn_id="postgres_localhost")
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute("select * from races")

    with open(f"dags/get_races.csv", "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)
        f.flush()
    cursor.close()
    conn.close()
    logging.info("Saved races data")
    # then upload to s3
    s3_hook = S3Hook(aws_conn_id = "s3_conn")
    s3_hook.load_file(
        filename = "dags/get_races.csv",
        key = "races.csv",
        bucket_name = S3_bucket_name,
        replace = True     ## Replace file if already exists
    )

def results_upload(): 
    hook = PostgresHook(postgres_conn_id="postgres_localhost")
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute("select * from results")

    with open(f"dags/get_results.csv", "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)
        f.flush()
    cursor.close()
    conn.close()
    logging.info("Saved results data")
    # then upload to s3
    s3_hook = S3Hook(aws_conn_id = "s3_conn")
    s3_hook.load_file(
        filename = "dags/get_results.csv",
        key = "results.csv",
        bucket_name = S3_bucket_name,
        replace = True
    )

with DAG(
    dag_id="formula1_upload_to_s3",
    default_args=default_args,
    start_date=datetime(2023, 2, 27),
    catchup = False,
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id="circuits_upload",
        python_callable=circuits_upload
    )

    task2 = PythonOperator(
        task_id="constructors_upload",
        python_callable=constructors_upload
    )

    task3 = PythonOperator(
        task_id="races_upload",
        python_callable=races_upload
    )
    task4 = PythonOperator(
        task_id="results_upload",
        python_callable=results_upload
    )

    task1, task2, task3, task4