def test_read_csv_to_hive():
    # Test inputs
    path_file = "hdfs:///user/hadoop/drivers.csv"
    table_name = "drivers"

    # Call the function
    read_csv_to_hive(path_file, table_name)

    # Assert that the CSV was read correctly
    read.csv.assert_called_once_with(path_file, header=True, inferSchema=True)

    # Assert that the DataFrame's write.saveAsTable method was called
    df = read.csv.return_value
    df.write.saveAsTable.assert_called_once_with(table_name, format="hive", mode="overwrite")

    # Assert that the SQL command to show tables was executed
    sql.assert_called_once_with("SHOW TABLES")