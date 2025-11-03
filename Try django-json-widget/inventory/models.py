from django.db import models

# Create your models here.


class Item(models.Model):
    """Model representing an item with a name and metadata."""

    name = models.CharField(max_length=100)
    metadata = models.JSONField(default=dict, blank=True)

    def __str__(self):
        """Return the string representation of the item."""

        return self.name


class Product(models.Model):
    """Model representing a product with a name, description, price, and attributes."""

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    attributes = models.JSONField(default=dict, blank=True)

    def __str__(self):
        """Return the string representation of the product."""

        return self.name
