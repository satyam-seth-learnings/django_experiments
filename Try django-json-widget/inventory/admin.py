from django.contrib import admin
from .models import Item

# Register your models here.


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """Admin interface for Item model. without use of django-json-widget."""

    list_display = ("name", "metadata")
