from django.contrib import admin
from .models import Item, Product

# Register your models here.


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """Admin interface for Item model. without use of django-json-widget."""

    list_display = ("id", "name", "metadata")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin interface for Product model. without use of django-json-widget."""

    list_display = ("id", "name", "description", "price", "attributes")
