# Generated by Django 4.1.7 on 2023-03-04 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0003_alter_column_options_dataset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='path',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
