from django.contrib import admin

# Register your models here.

from .models import Equipo, Jugador

admin.site.register(Equipo)
admin.site.register(Jugador)