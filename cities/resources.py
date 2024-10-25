from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from cities.models import City
from states.models import State


class CityResource(resources.ModelResource):

    state = fields.Field(
        column_name='state',
        attribute='state',
        widget=ForeignKeyWidget(State, field='name')
    )

    class Meta:
        model = City
        fields = ('id', 'state', 'name')
        export_order = ('id', 'state', 'name')
        skip_unchanged = True
        report_skipped = True
