from django.contrib import admin
from neighborhoods.models import Neighborhood
from neighborhoods.resources import NeighborhoodResource
from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(Neighborhood)
class NeighborhoodAdmin(ImportExportModelAdmin):
    resource_class = NeighborhoodResource
    list_display = (
        'id', 'created', 'modified', 'postal_code', 'name'
    )
    list_filter = ('postal_code__state','postal_code__city')
    search_fields = ('postal_code__postal_code', 'name')
