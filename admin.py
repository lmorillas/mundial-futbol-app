from django.contrib import admin

# Register your models here.

from .models import Equipo, Jugador

admin.site.register(Equipo)

@admin.site.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'posicion')
    list_filter = ('posicion', 'equipo')
    search_fields = ('nombre', 'apellido', 'posicion')

