# Baseia-se em uma imagem Python (ex: python:3.11-bullseye)
FROM python:3.11-bullseye 

# Atualiza os pacotes e instala OpenJDK 17
RUN apt-get update 
RUN apt-get install -y --no-install-recommends openjdk-17-jdk 
RUN apt-get clean && rm -rf /var/lib/apt/lists/* 

# Define variáveis de ambiente para Spark e Java
ENV SPARK_HOME="/home/sparkuser/spark"
ENV JAVA_HOME="/usr/lib/jvm/java-17-openjdk-amd64" 
ENV PATH="${JAVA_HOME}:${SPARK_HOME}/bin:${SPARK_HOME}/sbin:${PATH}" 

# Cria o diretório do Spark e define como diretório de trabalho
RUN mkdir -p ${SPARK_HOME} 
WORKDIR ${SPARK_HOME} 

# Baixa e extrai a distribuição do Apache Spark (versão 4.0.0 com Hadoop 3)
# Esta seção é para ter as ferramentas Spark (como spark-submit) e bibliotecas para construir JARs.
# Se precisar de uma versão mais recente, atualize o link.
RUN curl https://dlcdn.apache.org/spark/spark-4.0.0/spark-4.0.0-bin-hadoop3.tgz -o spark-4.0.0-bin-hadoop3.tgz \
    && tar xvzf spark-4.0.0-bin-hadoop3.tgz --directory ${SPARK_HOME} --strip-components 1 \
    && rm -rf spark-4.0.0-bin-hadoop3.tgz 

# Define portas e hostname para o Master (embora este Dockerfile seja mais para build, não para o cluster em si)
ENV SPARK_MASTER_PORT="7077" 
ENV SPARK_MASTER_HOST="spark-master" 



# Baixa drivers JDBC para PostgreSQL e bibliotecas AWS para Spark Jars
RUN wget -P ${SPARK_HOME}/jars/ https://jdbc.postgresql.org/download/postgresql-42.7.4.jar; 
RUN wget -P ${SPARK_HOME}/jars/ https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar; 
RUN wget -P ${SPARK_HOME}/jars/ https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar; 



# Cria um usuário sparkuser e ajusta permissões
RUN useradd -u 1000 -m -d /home/sparkuser sparkuser 
ENV HOME="/home/sparkuser" 
RUN chown -R 1000:1000 ${SPARK_HOME} 
USER sparkuser 


# Copia configurações customizadas do Spark
COPY ./spark-defaults.conf "${SPARK_HOME}/conf" 

ENTRYPOINT ["/bin/bash"]