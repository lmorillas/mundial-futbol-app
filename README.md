## Ejemplo app jugadores mundial

### Haz un fork del repositorio

### Instala la aplicación como un submódulo en tu proyecto.

```bash
git submodule add <url-clone> mundial
```

### Añade la app al fichero `settings.py` de tu proyecto.

### Prepara la base de datos

```bash
python manage.py makemigrations mundial
python manage.py migrate
```

### Carga los datos de los jugadores

En la carpeta [utils](tree/main/utils) tienes las instrucciones
