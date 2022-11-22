from django.db import models

# Create your models here.


class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True)
    imagen = models.URLField(blank=True)
    posicion = models.CharField(max_length=100)
    equipo = models.CharField(max_length=100)
    

