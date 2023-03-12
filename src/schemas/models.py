from django.db import models
from django.urls import reverse

from .utils import generate_fake_data, generate_csv, get_random_name


class Schema(models.Model):
    """
    Model representing a schema.
    """

    name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('schemas:detail', kwargs={'pk': self.pk})
    
    def delete(self, *args, **kwargs):
        for dataset in self.datasets.all():
            dataset.delete()
        super().delete(*args, **kwargs)


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
    csv_file = models.FileField(null=True)

    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, related_name='datasets')

    def generate(self, total: int):
        csv_file = generate_csv(self, total)
        csv_name = get_random_name(prefix='datasets/')
        self.csv_file.save(csv_name, csv_file)

    def delete(self, *args, **kwargs):
        self.csv_file.delete(save=False)
        super().delete(*args, **kwargs)
