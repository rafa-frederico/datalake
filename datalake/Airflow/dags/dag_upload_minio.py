from airflow import DAG
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.operators.python import PythonOperator
from datetime import datetime

def upload_file_to_minio():
    s3_hook = S3Hook(aws_conn_id='minio_s3_conn') # Usa a conexão que você configurou
    bucket_name = 'silver'
    key = 'data/example.txt'
    file_content = 'Hello from Airflow to MinIO!'

    # Cria o bucket se ele não existir
    if not s3_hook.check_for_bucket(bucket_name):
        s3_hook.create_bucket(bucket_name)

    # Carrega o arquivo
    s3_hook.load_string(string_data=file_content, key=key, bucket_name=bucket_name, replace=True)
    print(f"File '{key}' uploaded to bucket '{bucket_name}' in MinIO.")

def download_file_from_minio():
    s3_hook = S3Hook(aws_conn_id='minio_s3_conn')
    bucket_name = 'bronze'
    key = 'data/example.txt'

    file_content = s3_hook.read_key(key=key, bucket_name=bucket_name)
    print(f"Content of '{key}':\n{file_content}")

with DAG(
    dag_id='dag_upload_minio',
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:
    upload_task = PythonOperator(
        task_id='upload_file',
        python_callable=upload_file_to_minio,
    )

    download_task = PythonOperator(
        task_id='download_file',
        python_callable=download_file_from_minio,
    )

    upload_task >> download_task