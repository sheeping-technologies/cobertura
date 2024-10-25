from django.contrib import admin
from services.models import Service
from services.resources import ServiceResource
from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin):
    resource_class = ServiceResource
    list_display = (
        'id', 'created', 'modified', 'carrier', 'name'
    )
    list_filter = ('carrier',)
    search_fields = ('name',)
