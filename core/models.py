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

class Persona(models.Model):
    class Meta:
        abstract = True

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    sexo = models.CharField(max_length=9)
    nacimiento = models.DateField()
    edad = models.IntegerField()
