# Crear jugadores desde json

## Instala ipython si no está instalado

```bash
pip install ipython
``` 
## Ejecuta el shell de django  (raíz del proyecto)

```bash
(env) $ python manage.py shell

>>> cd mundial/utils
>>> %run crea-jugadores.py
```

## Comprueba que se han creado los jugadores

> En el mismo shell de django
> 
```python
from mundial.models import Jugador

Jugador.objects.count()
```

Si quieres borrar los jugadores creados, ejecuta el siguiente comando:

```python
Jugador.objects.all().delete()
```
