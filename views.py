from django.shortcuts import render
from .models import Jugador
from django.views.generic import ListView

# Create your views here.


def ListadoJugadores(ListView):
    model = Jugador
    template_name = 'mundial/listado_jugadores.html'
