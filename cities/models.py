
from django.db import models

from states.models import State
from core.models import TimeStampedModel


class City(TimeStampedModel):

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

    state = models.ForeignKey(
        State,
        verbose_name = 'Estado',
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=75,
        verbose_name = 'Nombre'
    )

    def __str__(self):
        return self.name
