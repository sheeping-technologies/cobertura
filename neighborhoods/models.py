
from django.db import models
from postalcodes.models import PostalCode

from core.models import TimeStampedModel


class Neighborhood(TimeStampedModel):

    class Meta:
        verbose_name = 'Colonia'
        verbose_name_plural = 'Colonias'

    postal_code = models.ForeignKey(
        PostalCode,
        related_name='neighborhoods',
        on_delete=models.CASCADE,
        verbose_name = 'Codigo Postal'
    )

    name = models.CharField(
        max_length=75,
        verbose_name = 'Nombre'
    )

    def __str__(self):
        return self.name
