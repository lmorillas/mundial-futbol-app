from django.contrib import admin

# Register your models here.

from .models import Equipo, Jugador

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    pass


@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'posicion', 'img_jugador')
    list_filter = ('posicion', 'equipo__nombre')
    search_fields = ('nombre', 'apellido', 'posicion')


