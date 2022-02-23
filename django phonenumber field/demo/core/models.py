from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class PhoneNumberDemoModel(models.Model):
    phone_number = PhoneNumberField()
