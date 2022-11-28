# herramienta para crear datos a partir de jugadores_mundial·json

'''
 {
        "nombre": "RUI",
        "apellido": "PATRICIO",
        "imagen": "https://digitalhub.fifa.com/transform/f4e4fea4-17a1-4242-ab3f-b6799e37e11c/1442846670?io=transform:fill,width:792,height:900",
        "posicion": "Arquero",
        "equipo": "Portugal"
} 
'''

import json
from mundial.models import Jugador, Equipo

url = 'jugadores_mundial.json'
with open(url) as f:
    jugadores = json.load(f, encoding='utf-8')

for jugador in jugadores:
    # existe el equipo?
    equipo = Equipo.objects.filter(nombre=jugador['equipo'])
    if equipo:
        equipo = equipo.first() # el primer elemento es mi equpo
    else:  # no existe el equipo
        equipo = Equipo.objects.create(nombre=jugador['equipo'])
        # equipo = Equipo()
        # equipo.nombre = jugador['equipo']
        # equipo.save()
    # crear el jugador

    del jugador['equipo']
    if jugador.get('imagen'):
        imagen = jugador['imagen']
        if not imagen.startswith('http'):
            del jugador['imagen']


    j = Jugador()  # j es el jugador que estoy creando. jugador es el dato del json
    


    '''
    j.nombre = jugador['nombre']
    if jugador.get('apellido'):
        j.apellido = jugador['apellido']
    if jugador.get('imagen'):
        imagen = jugador['imagen']
        if imagen.startswith('http'):  # este dato me interesa
            j.imagen = jugador['imagen']  
    j.posicion = jugador['posicion']
    j.equipo = equipo
    '''
    j.save()








    













