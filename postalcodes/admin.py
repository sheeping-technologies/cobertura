from django.contrib import admin
from postalcodes.models import PostalCode
from postalcodes.resources import PostalCodeResource
from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(PostalCode)
class PostalCodeAdmin(ImportExportModelAdmin):
    resource_class = PostalCodeResource
    list_display = (
        'id', 'created', 'modified', 'state', 'city', 'postal_code'
    )
    list_filter = ('state', 'city')
    search_fields = ('postal_code',)
