from django.contrib import admin
from postalconnectedservices.models import PostalConnectedService
from postalconnectedservices.resources import PostalConnectedServiceResource
from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(PostalConnectedService)
class PostalConnectedServiceAdmin(ImportExportModelAdmin):
    resource_class = PostalConnectedServiceResource
    list_filter = ('service', 'postal_code__state', 'postal_code__city', 'delivery_type','extended_area')
    search_fields = ('postal_code__postal_code',)
    list_display = (
        'id', 'created',
        'modified', 'postal_code',
        'service', 'delivery_type',
        'coverage', 'extended_area',
    )
    