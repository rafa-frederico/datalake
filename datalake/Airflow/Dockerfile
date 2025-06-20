# Use a imagem oficial do Airflow como base
# Airflow 3 ainda não existe, então usaremos a versão 2.x mais recente.
# Supondo que você esteja se referindo a uma versão futura ou a uma "ideia" de Airflow 3.
# Por enquanto, usaremos a imagem oficial do Airflow 2.8.1 (ou a mais recente que for estável)
FROM apache/airflow:2.8.1-python3.10

# Variáveis de ambiente para o Spark
ENV SPARK_VERSION=3.5.0
ENV HADOOP_VERSION=3
ENV SPARK_HOME=/opt/spark

# Instalar dependências para o Spark
# Java Development Kit (JDK) é essencial para o Spark
RUN apt-get update && \
    apt-get install -y --no-install-recommends openjdk-11-jdk wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Baixar e instalar o Apache Spark
RUN wget https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -O /tmp/spark.tgz && \
    tar -xvf /tmp/spark.tgz -C /opt && \
    mv /opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} ${SPARK_HOME} && \
    rm /tmp/spark.tgz

# Adicionar o Spark ao PATH
ENV PATH="${PATH}:${SPARK_HOME}/bin"

# Instalar PySpark (se você for usar APIs Python do Spark)
# É importante que a versão do PySpark corresponda à versão do Spark instalada.
RUN pip install pyspark==${SPARK_VERSION}

# Exemplo de instalação de pacotes Python adicionais para o Airflow/DAGs
RUN pip install pandas apache-airflow-providers-cncf-kubernetes

#  Copy your DAGs to the Airflow DAGs directory

COPY Airflow/dags/ /opt/airflow/dags/


COPY Airflow/plugins/ /opt/airflow/plugins/