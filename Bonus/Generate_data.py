import pandas as pd
from faker import Faker
import json

fake = Faker()


def generate_data(num_records):
    """
    Creating an empty list so the generated records can be stored in there
    using a for loop. Also adding a timestamp in Event_Date_Records so it is
    suitable for Kafka

    :param num_records: The amount of record there need to be generated
    """
    data = []

    for i in range(num_records):
        record = {
            'PERSONAL_NUMBER_ID': i + 1,
            'FULL_NAME': fake.name(),
            'BIRTH_DATE': fake.date_of_birth(minimum_age=18, maximum_age=90).isoformat(),
            'SSN': fake.ssn(),
            'EVENT_DATE_RECORD': fake.iso8601(),
            'PERSONAL_ADDRESS_STREET': fake.street_address(),
            'PERSONAL_ADDRESS_CITY': fake.city(),
            'PERSONAL_ADDRESS_STATE': fake.state(),
            'PERSONAL_ADDRESS_COUNTRY': fake.country(),
            'PERSONAL_ADDRESS_ZIP_CODE': fake.zipcode()
        }

        data.append(record)

    df = pd.DataFrame(data)

    return df


# Verify serialization
def validate(df):
    """Making sure that the data is suitable for Kafka """
    sample_record = df.iloc[0].to_dict()
    json_record = json.dumps(sample_record)

    print("Sample Kafka Message (in JSON format):")
    print(json_record)

    # Making sure message is under 1MB
    message_size = len(json_record.encode('utf-8'))
    print(f"\nSize of the message in bytes: {message_size} bytes")

    return


def to_json(df):
    """Exporting data to a JSON file"""
    df.to_json('personal_data.json', orient='records', lines=True)

    return


df = generate_data(10000)

validate(df)

to_json(df)

