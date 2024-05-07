from django.db import models

# Create your models here.


class Student(models.Model):
    """Student Model"""

    name = models.CharField(max_length=128)
