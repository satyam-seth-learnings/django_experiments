from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    # Attach historical records to the model
    history = HistoricalRecords()

    def __str__(self):
        return self.title