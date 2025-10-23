from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Product

@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name', 'description')
