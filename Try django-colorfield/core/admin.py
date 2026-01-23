from django.contrib import admin
from .models import ExampleModel

# Register your models here.

@admin.register(ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "image",
        "color",
        "hex_color",
        "hexa_color",
        "rgb_color",
        "rgba_color",
        "restrictive_color",
        "non_restrictive_color",
    )