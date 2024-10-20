"""Loading data"""

df = spark.read.csv("file:///tmp/dangerous-driver.csv", header=True)
df2 = spark.read.csv("file:///tmp/extra-driver.csv", header=True)

"""These are some of the attempts I made to load the data into a Hbase table
but I couldnt make it work so the code also doesnt work!"""

hbase_conf = {
    "hbase.table.name": "dangerous_driving",
    "hbase.zookeeper.quorum": "localhost",
    "hbase.zookeeper.property.clientPort": "2181"
}

df.write.options(hbase_conf).format("hbase").save()