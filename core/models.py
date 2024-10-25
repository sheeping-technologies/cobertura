from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating ``created`` and ``modified`` fields.
    """

    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Creado')
    modified = models.DateTimeField(auto_now=True, verbose_name = 'Modificado',)

    class Meta:
        abstract = True
