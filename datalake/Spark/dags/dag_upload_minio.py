from airflow import DAG
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.operators.python import PythonOperator
from datetime import datetime
from pyspark.sql import SparkSession

def upload_file_to_minio():
    # Caminho de saída no MinIO
    # O formato é s3a://<nome_do_bucket>/<caminho_no_bucket>
    output_path = "s3a://localhost:9001/bronze"
    # Caminho de saída no MinIO






def leApi():
    import requests
    import json

    url = "https://api.openbrewerydb.org/v1/breweries"  # Substitua pela URL da sua API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        

    spark = SparkSession.builder \
        .appName("leApi") \
        .getOrCreate()
    df = spark.read.json(spark.sparkContext.parallelize(data))
    df.show()
    return df 


def gravarBronze():
    # Cria uma sessão Spark
    spark = SparkSession.builder \
        .appName("Upload to MinIO") \
        .getOrCreate()

    # Lê o DataFrame do arquivo JSON
    df = leApi()

    # Grava o DataFrame no MinIO
    df.write.mode("overwrite").parquet("s3a://localhost:9000/bronze")

    # Fecha a sessão Spark
    spark.stop()

def gravarSilver():
    # Cria uma sessão Spark
    spark = SparkSession.builder \
        .appName("Upload to MinIO") \
        .getOrCreate()

    # Lê o DataFrame do arquivo JSON
    df = leApi()

    # Grava o DataFrame no MinIO
    df.write.mode("overwrite").parquet("s3a://localhost:9000/silver")

    # Fecha a sessão Spark
    spark.stop()

def gravarGold():
    # Cria uma sessão Spark
    spark = SparkSession.builder \
        .appName("Upload to MinIO") \
        .getOrCreate()

    # Lê o DataFrame do arquivo JSON
    df = leApi()

    # Grava o DataFrame no MinIO
    df.write.mode("overwrite").parquet("s3a://localhost:9000/gold")

    # Fecha a sessão Spark
    spark.stop()

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
    gravarBronze = PythonOperator( task_id='gravarBronze',
        python_callable=gravarBronze
    )
    gravarSilver = PythonOperator( task_id='gravarSilver',
        python_callable=gravarSilver
    )
    gravarGold = PythonOperator( task_id='gravarGold',
        python_callable=gravarGold
    )


    gravarBronze >> gravarSilver >> gravarGold 