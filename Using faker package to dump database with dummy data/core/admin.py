from django.contrib import admin
from core.models import DemoModel

# Register your models here.


@admin.register(DemoModel)
class DemoAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "address", "phone_number")
