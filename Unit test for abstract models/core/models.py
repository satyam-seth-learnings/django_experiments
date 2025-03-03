from django.db import models

# Create your models here.



class BaseCreatedModifiedModel(models.Model):
    """
    Abstract base model that provides self-updating
    created_on and modified_on timestamp fields
    """

    modified_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
