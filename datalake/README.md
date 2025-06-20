## Instalação do Ambiente


1) Download do Github
git clone https://github.com/rafa-frederico/datalake.git

2) Docker - configuração do ambiente
 Dentro da pasta datalake do seu ambiente execute o comando para criar o docker. O primeiro comando irá instalar as bibliotecas necessárias e o segundo permite fazer o download dos softwares necessários para configuração do ambiente do Datalake .
  docker-compose build 
  docker compose up airflow-init
  docker compose up -d

3) Instalar JAVA_HOME para o Airflow no MAC
brew install --cask temurin

4) Identificar o JAVA_HOME no MAC
/usr/libexec/java_home
<</Library/Java/JavaVirtualMachines/temurin-24.jdk/Contents/Home>>

5) criar ambiente virtual python

6) instalar minio
pip install minio

7) instalar pyspark
pip install pyspark








3) Inicializar o ambiente 
MinIO - Bucket 



