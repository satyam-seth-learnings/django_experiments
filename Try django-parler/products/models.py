from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Product(TranslatableModel):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Translated fields
    translations = TranslatedFields(
        name=models.CharField(max_length=255),
        description=models.TextField(),
    )

    def __str__(self):
        return self.name
