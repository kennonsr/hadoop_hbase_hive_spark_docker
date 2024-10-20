from Generate_data import generate_data

def test_generate_data():
    df = generate_data(10)  # Generate 10 records for testing
    assert len(df) == 10  # Check if the number of records is correct
    assert 'PERSONAL_NUMBER_ID' in df.columns  # Check for expected columns
    assert df['PERSONAL_NUMBER_ID'].iloc[0] == 1  # Check first ID

    # Validate data types
    assert isinstance(df['FULL_NAME'].iloc[0], str)
    assert isinstance(df['BIRTH_DATE'].iloc[0], str)
    assert isinstance(df['SSN'].iloc[0], str)

