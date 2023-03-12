import os
import csv
from io import StringIO
from uuid import uuid4

from django.core.files.base import ContentFile

from faker import Faker


def generate_fake_data(datatype: str):
    """
    Generate fake data based on datatype.
    """
    fake = Faker()

    data_generators = {
        'name': fake.name,
        'job': fake.job,
        'email': fake.email,
        'phone': fake.phone_number,
        'date': fake.date_time_this_year,
    }

    if datatype not in data_generators:
        error = f'Invalid datatype: {datatype}.'
        raise ValueError(error)

    return data_generators[datatype]()


def generate_csv(dataset, total) -> ContentFile:
    """
    Generate csv file with number of rows equal to total.
    """

    header = ['id'] + [column.name for column in dataset.schema.columns.all()]

    csv_buffer = StringIO()
    csv_writer = csv.writer(csv_buffer)

    header = ['id'] + [column.name for column in dataset.schema.columns.all()]
    csv_writer.writerow(header)

    for count in range(1, total + 1):
        row = [str(count)] + [column.generate_fake_value() for column in dataset.schema.columns.all()]
        csv_writer.writerow(row)

    csv_file = ContentFile(csv_buffer.getvalue().encode())

    return csv_file


def get_random_name(prefix) -> str:
    """
    Generate random file name.
    """

    csv_name = f'{uuid4()}.csv'
    return os.path.join(prefix, csv_name)
