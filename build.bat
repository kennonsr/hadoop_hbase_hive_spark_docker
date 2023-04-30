@echo off

REM Hadoop build
docker build -f ./hadoop/Dockerfile . -t sciencepal/hadoop_cluster:hadoop

REM Spark
docker build -f ./spark/Dockerfile . -t sciencepal/hadoop_cluster:spark

REM PostgreSQL Hive Metastore Server
docker build -f ./postgresql-hms/Dockerfile . -t sciencepal/hadoop_cluster:postgresql-hms

REM Hive
docker build -f ./hive/Dockerfile . -t sciencepal/hadoop_cluster:hive

REM Hive
docker build -f ./hbase/Dockerfile . -t sciencepal/hadoop_cluster:hbase

REM Edge
docker build -f ./edge/Dockerfile . -t sciencepal/hadoop_cluster:edge

::REM hue
::docker build -f ./hue/Dockerfile . -t sciencepal/hadoop_cluster:hue
