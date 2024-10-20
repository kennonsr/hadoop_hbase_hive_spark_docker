
def read_csv_to_hive(path_file, table_name):
    """
    Reads a CSV file from HDFS and writes it to a Hive table.

    :param path_file: Path to the CSV file in HDFS example: "hdfs:///user/hadoop/drivers.csv"
    :param table_name: Name of the Hive table to write to
    """
    # Read the CSV file from HDFS
    df = spark.read.csv(path_file, header=True, inferSchema=True)

    # Write the DataFrame to a Hive table
    df.write.saveAsTable(table_name, format="hive", mode="overwrite")

    spark.sql("SHOW TABLES").show()

    return


"""Creating a Dataframe that contains the asked columns for aggregated information"""

df1 = spark.sql("SELECT driverId, name FROM drivers")
df2 = spark.sql("SELECT driverId, `hours-logged`, `miles-logged` FROM timesheet")

joined_df = df1.join(df2, on="DRIVERID", how="inner")

joined_df.show()