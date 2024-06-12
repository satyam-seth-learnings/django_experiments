from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportActionModelAdmin, ImportExportMixin
from .models import Post

# Register your models here.


class PostResource(resources.ModelResource):

    is_active = fields.Field()
    created_at = fields.Field()

    class Meta:
        model=Post
        fields = ('id', 'title', 'description', 'is_active', 'created_at')    
        export_order = ('id', 'title', 'description', 'created_at', 'is_active')    
    
    def dehydrate_is_active(self, obj):
        if obj.is_active:
            return "yes"
        return "no"
    
    def dehydrate_created_at(self, obj):
        return obj.created_at.strftime("%d—%m—%Y %H:%M:%S")


@admin.register(Post)
class PostAdmin(ImportExportActionModelAdmin, ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'is_active', 'created_at')