from import_export import resources
from states.models import State


class StateResource(resources.ModelResource):

    class Meta:
        model = State
        fields = ('id', 'name', 'shipping_key')
        export_order = ('id', 'name', 'shipping_key')
        skip_unchanged = True
        report_skipped = True
