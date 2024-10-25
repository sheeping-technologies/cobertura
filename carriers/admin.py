from django.contrib import admin
from carriers.models import Carrier
from carriers.resources import CarrierResource
from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(Carrier)
class CarrierAdmin(ImportExportModelAdmin):
    resource_class = CarrierResource
    list_display = (
        'id', 'created', 'modified', 'name'
    )
    search_fields = ('name',)
