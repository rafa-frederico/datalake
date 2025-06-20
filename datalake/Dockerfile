# Usa a imagem base oficial do Apache Airflow
FROM apache/airflow:2.3.4

# Define o usuário para root temporariamente para instalar pacotes extras
# Isso é necessário porque a imagem do Airflow por padrão executa como usuário `airflow`
USER airflow

# Instala o provedor do Microsoft Azure
# É uma boa prática usar `pip install --no-cache-dir` para evitar que o cache do pip
# infle o tamanho da imagem final.
# Use `apache-airflow-providers-microsoft-azure` para a versão mais recente compatível,
# ou especifique uma versão exata, como `apache-airflow-providers-microsoft-azure==<versao_desejada>`
RUN pip install --no-cache-dir apache-airflow-providers-microsoft-azure


# --- Adição para o Spark ---
# Instala o PySpark e, opcionalmente, findspark
# A versão do PySpark deve ser compatível com a versão do Spark que você vai rodar
# (Ex: PySpark 3.3.x para Spark 3.3.x)
RUN pip install --no-cache-dir pyspark==3.3.2 # Ou a versão que você for usar
# RUN pip install --no-cache-dir findspark # Opcional, se precisar do findspark em suas DAGs


# (Opcional) Instale quaisquer outras dependências Python que suas DAGs possam precisar
# Exemplo:
# RUN pip install --no-cache-dir pandas requests

# (Opcional) Copie seus DAGs para o diretório de DAGs do Airflow
# Certifique-se de que o diretório `dags` exista no mesmo nível do seu Dockerfile
# COPY dags/ /opt/airflow/dags/

# (Opcional) Copie quaisquer plugins personalizados para o diretório de plugins do Airflow
# COPY plugins/ /opt/airflow/plugins/

# Volta para o usuário padrão do Airflow.
# É uma boa prática de segurança para evitar que o contêiner execute como root.
USER airflow

# O ENTRYPOINT e CMD da imagem base do Airflow já estão configurados para iniciar
# os componentes do Airflow (scheduler, webserver, etc.) com base nas variáveis
# de ambiente e argumentos passados. Não é necessário redefinir aqui,
# a menos que você tenha uma necessidade muito específica.