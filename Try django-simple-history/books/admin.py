from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Book

@admin.register(Book)
class BookModelAdmin(SimpleHistoryAdmin):
    list_display = ('title', 'author', 'published_date')

    # If you want to include change history in the admin
    history_list_display = ('history_user', 'history_change_reason', 'history_date')
