from django.contrib import admin
from .models import Demo

# Register your models here.


@admin.register(Demo)
class Demo(admin.ModelAdmin):
    list_display = ('id', 'my_field')
