from django.db import models
from core.models import Persona
from banda.models import Banda

class Instrumento(models.Model):
    nombre = models.CharField(max_length=20)
    marca = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=200)


class Integrante(Persona, models.Model):
    banda = models.ManyToManyField(Banda)
    instrumento = models.ManyToManyField(Instrumento)
