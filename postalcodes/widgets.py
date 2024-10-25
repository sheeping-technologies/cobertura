from import_export.widgets import ForeignKeyWidget

class CityPostalCodeForeignKeyWidget(ForeignKeyWidget):
    def get_queryset(self, value, row, *args, **kwargs):
        return self.model.objects.filter(
            state__name=row["state"],
            name=value
        )