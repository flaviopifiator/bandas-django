from django.db import models
from banda.models import Banda

class Evento (models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField()
	fecha_inicio = models.DateField()
	lugar = models.CharField(max_length=150)
	bandas = models.Banda() #Como seria aqui para poner varias bandas?, arreglo de bandas?

	def __str__(self):
		return 'Evento: %s' % (self.nombre)
