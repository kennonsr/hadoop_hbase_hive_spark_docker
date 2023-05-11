## Simple test on top of the cluster to check if it is working.

**Tests Done with Hive**

1. Copy file from local to nodemaster container : **docker cp test_data.csv nodemaster:/tmp/**

2. Enter nodemaster : **docker exec -u hadoop -it nodemaster /bin/bash**

3. Create directory in HDFS : hadoop@nodemaster:/$ **hdfs dfs -mkdir -p /user/hadoop/test**

4. Get file from container local to HDFS : hadoop@nodemaster:/$ **hdfs dfs -put /tmp/test_data.csv /user/hadoop/test/**

5. execute Hive by : hadoop@nodemaster:/$ **beeline -u "jdbc:hive2://nodemaster:10000/"** 
or hadoop@nodemaster:/$ **hive**

6. In hive terminal : hive>**create schema if not exists test;**

7. In hive terminal : 

```sql
hive> create external table if not exists test.test_data (row1 int, row2 int, row3 decimal(10,3), row4 int) row format delimited fields terminated by ',' stored as textfile location 'hdfs://172.20.1.1:9000/user/hadoop/test/';
```

8. **Results**
```sql
hive> select * from test.test_data where row3 > 2.499;
OK
1	122	5.000	838985046
1	185	4.500	838983525
1	231	4.000	838983392
1	292	3.500	838983421
1	316	3.000	838983392
1	329	2.500	838983392
1	377	3.500	838983834
1	420	5.000	838983834
1	466	4.000	838984679
1	480	5.000	838983653
1	520	2.500	838984679
1	539	5.000	838984068
1	586	3.500	838984068
1	588	5.000	838983339
Time taken: 0.175 seconds, Fetched: 14 row(s)
```

**Testing Spark Hive Integration - spark-shell on EDGE or Nodemaster Spark > 2.4.x with table created above**

hadoop@nodemaster:/$ **spark-shell --driver-java-options "-Dhive.metastore.uris=thrift://nodemaster:9083"**

import org.apache.spark.sql.SparkSession
val spark = SparkSession.builder().master("spark://nodemaster:7077")
    .appName("kennon.test.nl")
    .config("spark.sql.warehouse.dir","/users/hive/warehouse")
    .enableHiveSupport()
    .getOrCreate()

val df = sql("select * from test.test_data limit 10")
df.show()

**Testing HBASE with PyBase on EDGE Node**

You can run a test with this python code -> configs/py-base-test-2.py. Just copy it in the edge node and run with Python 3.

