from django.contrib import admin
from .models import My

# Register your models here.


@admin.register(My)
class My(admin.ModelAdmin):
    list_display = ('id', 'test')
