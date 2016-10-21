from django.db import models

from core.models import EventUser


class Banda(EventUser, models.Model):
    nombre = models.CharField(max_length=150)
    fecha_fundacion = models.DateField()

    def __str__(self):
        return 'Banda: %s' % self.nombre


class Album(EventUser, models.Model):
    titulo = models.CharField(max_length=200)
    banda = models.ForeignKey(Banda)
    fecha = models.DateField()

    def __str__(self):
        return '%s => %s' % (self.banda, self.titulo)


class Genero(EventUser, models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return 'Género: %s' % self.nombre

class Cancion(EventUser, models.Model):
    titulo = models.CharField(max_length=150)
    duracion = models.Time() #tipo de dato para duracion?
    album = models.ForeignKey(Album)
    letra = models.TextField()

    def __str__(self):
        return 'Titulo: %s' % (self.titulo)