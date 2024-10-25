from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from services.models import Service
from carriers.models import Carrier


class ServiceResource(resources.ModelResource):

    carrier = fields.Field(
        column_name='carrier',
        attribute='carrier',
        widget=ForeignKeyWidget(Carrier, field='name')
    )

    class Meta:
        model = Service
        fields = ('id', 'carrier', 'name')
        export_order = ('id', 'carrier', 'name')
        skip_unchanged = True
        report_skipped = True
