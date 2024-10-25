from import_export import resources
from carriers.models import Carrier


class CarrierResource(resources.ModelResource):

    class Meta:
        model = Carrier
        fields = ('id', 'name')
        export_order = ('id', 'name')
        skip_unchanged = True
        report_skipped = True
