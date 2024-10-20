
def loading_data_to_hive(file_path):
    """
    Function to load the personal data Json file into a Hive table

    :param file_path: The path to the json file example: file:///tmp/personal_data.json
    """
    df = spark.read.json(file_path)

    spark.sql("""
        CREATE TABLE personal_data (
            PERSONAL_NUMBER_ID STRING,
            FULL_NAME STRING,
            BIRTH_DATE STRING,
            SSN STRING,
            EVENT_DATE_RECORD STRING,
            PERSONAL_ADDRESS_STREET STRING,
            PERSONAL_ADDRESS_CITY STRING,
            PERSONAL_ADDRESS_STATE STRING,
            PERSONAL_ADDRESS_COUNTRY STRING,
            PERSONAL_ADDRESS_ZIP_CODE STRING
        )
        ROW FORMAT DELIMITED
        FIELDS TERMINATED BY ','
        STORED AS TEXTFILE
    """)

    df.write.mode("overwrite").insertInto("personal_data")

    hive_df = spark.sql("SELECT * FROM personal_data")

    hive_df.write.mode("overwrite").json("/tmp/personal_data2.json")

    return


loading_data_to_hive("file:///tmp/personal_data.json")