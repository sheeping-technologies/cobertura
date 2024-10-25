
from django.db import models

from core.models import TimeStampedModel


class Carrier(TimeStampedModel):

    class Meta:
        verbose_name = 'Paqueteria'
        verbose_name_plural = 'Paqueterias'

    name = models.CharField(
        max_length=75,
        verbose_name = 'Nombre'
    )

    def __str__(self):
        return self.name
