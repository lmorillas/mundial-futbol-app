from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True)
    imagen = models.URLField(blank=True)
    posicion = models.CharField(max_length=100)
    equipo = models.CharField(max_length=100)

    def __str__(self):
        if self.apellido:
            return f'{self.nombre} {self.apellido}'
        return self.nombre

    @admin.display(description=_("Image"))
    def img_imagen(self):
        if self.imagen:
            return format_html(
                '<img src="{}" width="80" />'.format(
                    self.imagen)
            )
        else:
            return ''

    class Meta:
        verbose_name = _("Player")
        verbose_name_plural = _("Players")
        ordering = ('-id',)

    

