from django.db import models

from .utils import generate_fake_data


class ProcessingStatus(models.Model):
    """
    Model representing the processing status of a schema generation.
    """
    state = models.CharField(max_length=10)


class Schema(models.Model):
    """
    Model representing a schema.
    """

    name = models.CharField(max_length=50)


class Column(models.Model):
    """
    Model representing columns of a schema.
    """

    DATATYPE_CHOICES = (
        ('name', 'Full name'),
        ('job', 'Job'),
        ('email', 'Email'),
        ('phone', 'Phone number'),
        ('date', 'Date'),
    )

    name = models.CharField(max_length=50)
    datatype = models.CharField(max_length=5, choices=DATATYPE_CHOICES)
    order = models.IntegerField()

    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, related_name='columns')

    def generate_fake_value(self):
        return generate_fake_data(self.datatype)

    class Meta:
        ordering = ('order',)


class DataSet(models.Model):
    """
    Model representing dataset.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=255, null=True)

    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, related_name='datasets')
    status = models.ForeignKey(ProcessingStatus, on_delete=models.CASCADE)
