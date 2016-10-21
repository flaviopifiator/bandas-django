from django.contrib import admin

from .models import Album, Banda, Genero, Cancion


admin.site.register(Banda)
admin.site.register(Album)
admin.site.register(Genero)
admin.site.register(Cancion)
