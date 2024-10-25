from django.contrib import admin
from zonification.models import Group, Zone
from import_export.admin import ImportExportModelAdmin
from .resources import GroupResource, ZoneResource


# Register your models here.
class GroupAdmin(ImportExportModelAdmin):
    resource_class = GroupResource
    list_display = (
        'id', 'carrier', 'state', 'cp_from', 'cp_to', 'group'
    )
    list_filter = ('carrier', 'state')
    search_fields = ('group',)


# Register your models here.
class ZoneAdmin(ImportExportModelAdmin):
    resource_class = ZoneResource
    list_display = (
        'id', 'carrier', 'group_sender', 'group_receiver', 'zone',
    )
    list_filter = ('carrier', 'group_sender', 'group_receiver')
    search_fields = ('zone',)


admin.site.register(Group, GroupAdmin)
admin.site.register(Zone, ZoneAdmin)
