from airflow import DAG
from airflow.decorators import dag, task
import logging
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.providers.snowflake.transfers.s3_to_snowflake import S3ToSnowflakeOperator


from datetime import datetime, timedelta
import os
import requests

SNOWFLAKE_CONN_ID = 'snowflake_conn'
SNOWFLAKE_SCHEMA = 'PUBLIC'
SNOWFLAKE_STAGE ='formula_1_stage'
SNOWFLAKE_WAREHOUSE = 'my_wh'
SNOWFLAKE_DATABASE = 'ANALYTICS'
SNOWFLAKE_ROLE = 'ACCOUNTADMIN'
S3_BASE_PATH = 'temi-formula1/'
CIRCUITS_FILE = 'circuits.csv'
CONSTRUCTORS_FILE = 'constructors.csv'
RACES_FILE = 'races.csv'
RESULTS_FILE = 'results.csv'
FILE_FORMAT = "generic_csv"


# create_orders_table = """
#     CREATE OR REPLACE TRANSIENT TABLE {{ params.table_name }}
#         (
#             order_id VARCHAR,
#             date VARCHAR,
#             product_name VARCHAR,
#             quantity INT
#         );
# """

# start_warehouse = """
#     CREATE OR REPLACE WAREHOUSE my_wh WAREHOUSE_SIZE=XSMALL INITIALLY_SUSPENDED=FALSE
#     AUTO_SUSPEND = 300;
# """

# drop_warehouse = """
#     DROP WAREHOUSE my_wh;
# """


create_circuits_table_sql = """
    CREATE OR REPLACE TRANSIENT TABLE {{ params.table_name }}
        (
            circuitId VARCHAR,
            circuitRef VARCHAR,
            name VARCHAR,
            location VARCHAR,
            country VARCHAR,
            lat int,
            lng int,
            alt int,
            url VARCHAR
        );
"""

create_races_table_sql = """
    CREATE OR REPLACE TRANSIENT TABLE {{ params.table_name }}
        (
            raceId VARCHAR ,
            year int,
            round int,
            circuitId int,
            name VARCHAR,
            date date,
            time VARCHAR,
            url VARCHAR

            );
"""

create_constructors_table_sql = """
    CREATE OR REPLACE TRANSIENT TABLE {{ params.table_name }}
    (
    constructorId VARCHAR ,
    constructorRef VARCHAR,
    name VARCHAR,
    nationality VARCHAR,
    url VARCHAR
    );

"""


create_results_table_sql = """
    CREATE OR REPLACE TRANSIENT TABLE {{ params.table_name }}
    (
        resultid VARCHAR,
        raceid VARCHAR,
        driverid VARCHAR,
        constructorid VARCHAR,
        number int,
        grid int,
        position int,
        positiontext int,
        positionorder int,
        points int,
        laps int,
        time VARCHAR,
        milliseconds int,
        rank int
    );
"""



start_warehouse_sql = """
    CREATE OR REPLACE WAREHOUSE my_wh WAREHOUSE_SIZE=XSMALL INITIALLY_SUSPENDED=FALSE
    AUTO_SUSPEND = 300;
"""

drop_warehouse_sql = """
    DROP WAREHOUSE my_wh;
"""


default_args = {
    "owner": "airflow",
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(dag_id = "Ingest_to_Snowflake",
    default_args = default_args,
    start_date = datetime(2023,3,4),
    schedule_interval = '@daily',
    catchup = False)

create_circuits_table = SnowflakeOperator(
    task_id = "create_circuits_table",
    sql = [create_circuits_table_sql, start_warehouse_sql],
    params = {"table_name": "circuits"},
    snowflake_conn_id = SNOWFLAKE_CONN_ID,
    dag=dag)

create_races_table = SnowflakeOperator(
    task_id = "create_races_table",
    sql = create_races_table_sql,
    params = {"table_name": "races"},
    snowflake_conn_id = SNOWFLAKE_CONN_ID,
    dag=dag)

create_constructors_table = SnowflakeOperator(
    task_id = "create_constructors_table",
    sql = create_constructors_table_sql,
    params = {"table_name": "constructors"},
    snowflake_conn_id = SNOWFLAKE_CONN_ID,
    dag=dag)

create_results_table = SnowflakeOperator(
    task_id = "create_results_table",
    sql = create_results_table_sql,
    params = {"table_name": "results"},
    snowflake_conn_id = SNOWFLAKE_CONN_ID,
    dag=dag)

copy_into_circuits_table = S3ToSnowflakeOperator(
    task_id = 'copy_into_circuits_table',
    # prefix = S3_BASE_PATH,
    s3_keys = [CIRCUITS_FILE],
    snowflake_conn_id = SNOWFLAKE_CONN_ID,
    table = "circuits",
    schema = SNOWFLAKE_SCHEMA,
    stage = SNOWFLAKE_STAGE,
    role = SNOWFLAKE_ROLE,
    file_format = FILE_FORMAT,
    warehouse = SNOWFLAKE_WAREHOUSE,
    dag=dag
    )

copy_into_races_table = S3ToSnowflakeOperator(
    task_id = 'copy_into_races_table',
    # prefix = S3_BASE_PATH,
    s3_keys = [RACES_FILE],
    snowflake_conn_id = SNOWFLAKE_CONN_ID,
    table = "races",
    schema = SNOWFLAKE_SCHEMA,
    stage = SNOWFLAKE_STAGE,
    role = SNOWFLAKE_ROLE,
    file_format = FILE_FORMAT,
    warehouse = SNOWFLAKE_WAREHOUSE,
    dag=dag
    )

copy_into_constructors_table = S3ToSnowflakeOperator(
    task_id = 'copy_into_constructors_table',
    # prefix = S3_BASE_PATH,
    s3_keys = [CONSTRUCTORS_FILE],
    snowflake_conn_id = SNOWFLAKE_CONN_ID,
    table = "constructors",
    schema = SNOWFLAKE_SCHEMA,
    stage = SNOWFLAKE_STAGE,
    role = SNOWFLAKE_ROLE,
    file_format = FILE_FORMAT,
    warehouse = SNOWFLAKE_WAREHOUSE,
    dag=dag
    )


copy_into_results_table = S3ToSnowflakeOperator(
    task_id = 'copy_into_results_table',
    # prefix = S3_BASE_PATH,
    s3_keys = [RESULTS_FILE],
    snowflake_conn_id = SNOWFLAKE_CONN_ID,
    table = "results",
    schema = SNOWFLAKE_SCHEMA,
    stage = SNOWFLAKE_STAGE,
    role = SNOWFLAKE_ROLE,
    file_format = FILE_FORMAT,
    warehouse = SNOWFLAKE_WAREHOUSE,
    dag=dag
    )

drop_warehouse = SnowflakeOperator(
    task_id = "drop_warehouse",
    sql = [drop_warehouse_sql],
    snowflake_conn_id = SNOWFLAKE_CONN_ID,
    dag=dag)


create_circuits_table >> [create_constructors_table, create_races_table, create_results_table]
create_circuits_table >> copy_into_circuits_table
create_constructors_table >> copy_into_constructors_table
create_races_table >> copy_into_races_table
create_results_table >> copy_into_results_table
[copy_into_circuits_table,copy_into_constructors_table, copy_into_races_table,
  copy_into_results_table] >> drop_warehouse