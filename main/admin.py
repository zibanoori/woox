from django.contrib import admin
from .models import Core

class MoDeleteAdminMixin:
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin, MoDeleteAdminMixin):
    def has_add_permission(self, request):
        return not MyModel.objects.exists()
class CoreAdmin(admin.ModelAdmin):
    list_display = ['title', 'website_title', 'logo', 'copyright']
    list_display_links = ['title']     
    list_editable = ['website_title']  
    
admin.site.register(Core)


