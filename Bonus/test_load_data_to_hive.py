from Load_data_to_hive import loading_data_to_hive


def test_loading_data_to_hive():

    # Define file paths (adjust these paths according to your setup)
    input_path = "file:///tmp/personal_data.json"
    output_path = "/tmp/personal_data2.json"

    # Call the function with the real file path
    loading_data_to_hive(input_path)

    # Verify that the table was created and contains data
    hive_df = spark.sql("SELECT * FROM personal_data")
    assert hive_df.count() > 0, "The personal_data Hive table should contain data."

    # Verify that the output JSON file was written
    written_df = spark.read.json(output_path)
    assert written_df.count() > 0, "The output JSON file should contain data."
