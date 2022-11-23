from django.contrib import admin

from .models import Jugador

# Register your models here.

@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'posicion', 'img_imagen')
    list_filter = ('posicion', 'equipo')
    search_fields = ('nombre', 'apellido', 'posicion')

 