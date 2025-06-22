from datetime import datetime
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

with DAG(
    dag_id = "dag_teste",
    start_date = datetime(2025,1,1),
    schedule_interval = None,
    catchup = False,
    concurrency=2,
    default_args = {"retries" : 0}
) as dag:

    accumulator_metrics = SparkSubmitOperator(
        task_id = "AccumulatorMetricsClient",
        application = "/opt/bitnami/spark/examples/jars/spark-examples_2.13-4.0.0.jar",
        conn_id = "spark_standalone_client",
        java_class='org.apache.spark.examples.AccumulatorMetricsTest',
        executor_cores=2,
        total_executor_cores=2,
        verbose=True
    )