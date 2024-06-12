from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin, ImportExportMixin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(ImportExportActionModelAdmin, ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'is_active', 'created_at')