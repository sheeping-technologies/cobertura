from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .widgets import CityPostalCodeForeignKeyWidget
from cities.models import City
from postalcodes.models import PostalCode
from states.models import State


class PostalCodeResource(resources.ModelResource):

    state = fields.Field(
        column_name='state',
        attribute='state',
        widget=ForeignKeyWidget(State, field='name')
    )

    city = fields.Field(
        column_name='city',
        attribute='city',
        widget=CityPostalCodeForeignKeyWidget(City, field='name')
    )

    class Meta:
        model = PostalCode
        fields = ('id', 'state', 'city', 'postal_code')
        export_order = ('id', 'state', 'city', 'postal_code')
        skip_unchanged = True
        report_skipped = True
