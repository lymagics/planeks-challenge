import os
import csv
from uuid import uuid4

from django.conf import settings

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


def generate_csv(dataset, total):
    """
    Generate csv file with number of rows equal to total.
    """

    csv_name = f'{uuid4()}.csv'
    csv_path = os.path.join(settings.MEDIA_ROOT, csv_name)
    header = ['id'] + [column.name for column in dataset.schema.columns.all()]

    with open(csv_path, 'wt') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(header)

        for count in range(1, total + 1):
            row = [str(count)] + [column.generate_fake_value() for column in dataset.schema.columns.all()]
            csv_writer.writerow(row)

    return csv_path
