from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from postalcodes.models import PostalCode
from postalconnectedservices.models import PostalConnectedService
from services.models import Service


class PostalConnectedServiceResource(resources.ModelResource):

    postal_code = fields.Field(
        column_name='postal_code',
        attribute='postal_code',
        widget=ForeignKeyWidget(PostalCode, field='postal_code')
    )

    service = fields.Field(
        column_name='service',
        attribute='service',
        widget=ForeignKeyWidget(Service, field='name')
    )

    class Meta:
        model = PostalConnectedService
        fields = ('id', 'postal_code', 'service', 'delivery_type', 'service_zone', 'coverage', 'extended_area')
        export_order = ('id', 'postal_code', 'service', 'delivery_type', 'service_zone', 'coverage', 'extended_area')
        skip_unchanged = True
        report_skipped = True
