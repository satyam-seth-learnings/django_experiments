from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Book

# Register your models here.


# Register the Book model with SimpleHistoryAdmin for easy tracking in the admin panel
admin.site.register(Book, SimpleHistoryAdmin)
