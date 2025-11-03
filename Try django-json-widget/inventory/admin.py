from django.contrib import admin
from django.db import models
from django_json_widget.widgets import JSONEditorWidget
from .models import Item, Product

# Register your models here.


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """Admin interface for Item model. without use of django-json-widget."""

    list_display = ("id", "name", "metadata")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin interface for Product model. with use of django-json-widget."""

    list_display = ("id", "name", "description", "price", "attributes")
    formfield_overrides = {
        models.JSONField: {"widget": JSONEditorWidget},
    }
