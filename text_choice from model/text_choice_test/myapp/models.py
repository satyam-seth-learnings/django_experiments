from django.db import models

# Create your models here.


TEST_CHOICES = [
    ('test1', 'test1'),
    ('test2', 'test2'),
    ('test3', 'test3'),
    ('test4', 'test4')
]


class My(models.Model):
    test = models.CharField(
        max_length=10, choices=TEST_CHOICES, help_text='test choices')
