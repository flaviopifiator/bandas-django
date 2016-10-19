from django.contrib import admin

from .models import Album, Banda, Genero


admin.site.register(Banda)
admin.site.register(Album)
admin.site.register(Genero)

