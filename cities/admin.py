from django.contrib import admin
from cities.models import City
from cities.resources import CityResource
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class CityAdmin(ImportExportModelAdmin):
    resource_class = CityResource
    list_display = (
        'id', 'created', 'modified', 'state', 'name'
    )
    list_filter = ('state',)
    search_fields = ('name',)


admin.site.register(City, CityAdmin)
