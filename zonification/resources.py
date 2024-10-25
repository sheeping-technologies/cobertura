from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from carriers.models import Carrier
from zonification.models import Group, Zone
from states.models import State


class GroupResource(resources.ModelResource):

    carrier = fields.Field(
        column_name='carrier',
        attribute='carrier',
        widget=ForeignKeyWidget(Carrier, field='name')
    )

    state = fields.Field(
        column_name='state',
        attribute='state',
        widget=ForeignKeyWidget(State, field='name')
    )

    class Meta:
        model = Group
        fields = ('id', 'carrier', 'state', 'cp_from', 'cp_to', 'group')
        export_order = ('id', 'carrier', 'state', 'cp_from', 'cp_to', 'group')
        skip_unchanged = True
        report_skipped = True


class ZoneResource(resources.ModelResource):

    carrier = fields.Field(
        column_name='carrier',
        attribute='carrier',
        widget=ForeignKeyWidget(Carrier, field='name')
    )

    class Meta:
        model = Zone
        fields = ('id', 'carrier', 'group_sender', 'group_receiver', 'zone')
        export_order = ('id', 'carrier', 'group_sender', 'group_receiver', 'zone')
        skip_unchanged = True
        report_skipped = True
