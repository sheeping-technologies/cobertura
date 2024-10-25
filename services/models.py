from django.db import models

from carriers.models import Carrier
from core.models import TimeStampedModel


class Service(TimeStampedModel):

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    carrier = models.ForeignKey(
        Carrier,
        on_delete=models.CASCADE,
        verbose_name = 'Paqueteria'
    )

    name = models.CharField(
        max_length=75,
        verbose_name = 'Nombre'
    )

    def __str__(self):
        return self.name
