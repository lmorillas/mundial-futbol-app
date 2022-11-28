from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

# Create your models here.
'''
Datos que quiero almacenar:
{
        "nombre": "RUI",
        "apellido": "PATRICIO",  # puede ser nulo!!

        # Imagen a veces no es una url !!
        "imagen": "https://digitalhub.fifa.com/transform/f4e4fea4-17a1-4242-ab3f-b6799e37e11c/1442846670?io=transform:fill,width:792,height:900",
        "posicion": "Arquero",
        "equipo": "Portugal"
    },
'''

# Modelo para el equipo


class Equipo(models.Model):
    nombre = models.CharField(max_length=200)
    bandera = models.URLField(max_length=200, null=True, blank=True)
    # incompleto

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']

# Modelo para el jugador

POSICIONES = (
    ('Mediocampista', 'Mediocampista'),
    ('Arquero', 'Arquero'),
    ('Defensor', 'Defensor'),
    ('Delantero', 'Delantero')
    )

class Jugador(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200, blank=True)
    imagen = models.URLField(max_length=200, null=True, blank=True)
    posicion = models.CharField(max_length=60, choices=POSICIONES)
    equipo = models.ForeignKey(Equipo,
                               on_delete=models.SET_NULL, null=True, blank=True)
    # incompleto

    def __str__(self):
        return f'{self.nombre } {self.apellido} ({self.posicion})'

    class Meta:
        ordering = ['apellido', 'nombre']
        verbose_name_plural = 'Jugadores'

    @admin.display(description=_("Imagen"))
    def img_jugador(self):
        if self.imagen:
            return format_html(
                '<img src="{}" width="80" />'.format(
                    self.imagen)
            )
        else:
            return ''
