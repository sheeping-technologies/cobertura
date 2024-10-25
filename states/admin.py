from django.contrib import admin
from states.models import State
from states.resources import StateResource
from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(State)
class StateAdmin(ImportExportModelAdmin):
    resource_class = StateResource
    list_display = (
        'id', 'created', 'modified', 'name', 'shipping_key'
    )
    search_fields = ('name',)

