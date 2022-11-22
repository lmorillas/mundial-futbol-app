from mundial.models import Jugador

import json

jugadores = json.load(open('spain.json'))

for j in jugadores:
    # elimino imagenes que no son urls
    if not j['imagen'].startswith('http'):
        del j['imagen']
    # añado el valor del equipo
    j['equipo'] = 'España'

    jugador = Jugador(**j)
    jugador.save()
