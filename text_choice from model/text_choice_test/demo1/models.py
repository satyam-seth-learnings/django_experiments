from django.db import models
from .validators import validate_demo_choice

# Create your models here.


TEST_CHOICES = [
    ('test1', 'test1'),
    ('test2', 'test2'),
    ('test3', 'test3'),
    ('test4', 'test4')
]


class Demo(models.Model):
    my_field = models.CharField(
        max_length=10, choices=TEST_CHOICES, help_text='test choices', validators=[validate_demo_choice])
