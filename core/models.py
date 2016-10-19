from django.db import models


class EventUser(models.Model):
    class Meta:
        abstract = True

    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        editable=False
    )
