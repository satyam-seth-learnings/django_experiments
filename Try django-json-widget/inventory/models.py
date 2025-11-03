from django.db import models

# Create your models here.


class Item(models.Model):
    """Model representing an item with a name and metadata."""

    name = models.CharField(max_length=100)
    metadata = models.JSONField(default=dict, blank=True)

    def __str__(self):
        """Return the string representation of the item."""

        return self.name
