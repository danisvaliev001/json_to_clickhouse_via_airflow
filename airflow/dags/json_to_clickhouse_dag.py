from airflow import DAG
from airflow.hooks.clickhouse_hook import ClickHouseHook
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import os

ch_hook = ClickHouseHook()

file_data_json = '/var/lib/raw/event-data.json'

with open('/usr/local/airflow/scripts/create_table_01.sql', 'r') as file:
  query_create_table_01 = file.read().replace('\n', '')
  file.close()
with open('/usr/local/airflow/scripts/fill_table_01.sql', 'r') as file:
  query_fill_table_01 = file.read().replace('\n', '')
  file.close()
with open('/usr/local/airflow/scripts/create_table_02.sql', 'r') as file:
  query_create_table_02 = file.read().replace('\n', '')
  file.close()

def raw_to_table():
  ch_hook.run('CREATE DATABASE IF NOT EXISTS USERS')
  ch_hook.run('DROP TABLE IF EXISTS USERS.sessions_raw')
  ch_hook.run(query_create_table_01)
  ch_hook.run(query_fill_table_01)

def preprocess_table():
  # ch_hook.run('DROP TABLE IF EXISTS USERS.sessions')        # this is useful only for debugging
  ch_hook.run(query_create_table_02)
  ch_hook.run('INSERT INTO USERS.sessions SELECT * FROM USERS.sessions_raw')

def delete_json_file():
  if os.path.exists(file_data_json):
    os.remove(file_data_json)
  else:
    print("The file does not exist") 

with DAG(
  dag_id='json_to_clickhouse_dag',
  start_date=days_ago(1),
) as dag:

  t1 = PythonOperator(
    task_id='raw_to_table',
    python_callable=raw_to_table,
    )

  t2 = PythonOperator(
    task_id='preprocess_table',
    python_callable=preprocess_table,
    )

  t3 = PythonOperator(
    task_id='delete_json_file',
    python_callable=delete_json_file,
    )

  t1 >> t2 >> t3
