from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from postalcodes.models import PostalCode
from neighborhoods.models import Neighborhood


class NeighborhoodResource(resources.ModelResource):

    postal_code = fields.Field(
        column_name='postal_code',
        attribute='postal_code',
        widget=ForeignKeyWidget(PostalCode, field='postal_code')
    )

    class Meta:
        model = Neighborhood
        fields = ('id', 'postal_code', 'name')
        export_order = ('id', 'postal_code', 'name')
        skip_unchanged = True
        report_skipped = True
