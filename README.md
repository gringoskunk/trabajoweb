# Instrucciones del repo trabajoweb

## levantar proyecto:

py manage.py runserver

## Instrucciones para crear una API con django rest:

1. crear carpeta para el proyecto y entrar en el:

```
mkdir tutorial
cd tutorial
```

2. crear entorno virtual para las dependencias:
   python -m venv env

3. ir a la ruta "env\Scripts\" que se creó en el paso 2

```
cd env\Scripts\
```

4. activar el entorno virtual:

   - en bash:

   ```
    . activate
   ```

   - en powershell:

   ```
    ./Activate.ps1
   ```

5. instalar dependencias:
   pip install django
   pip install djangorestframework

6. crear la un proyecto django y su API:

   - (ste paso ya se hizo al crear el proyecto)

   ```
   django-admin startproject PRUEBA .
   cd PRUEBA
   ```

   - se crea una app llamada API, dentro de PRUEBA

   ```
   django-admin startapp API
   cd ..
   ```

7. migrar datos:

```
python manage.py migrate
```

...continua acá

https://www.django-rest-framework.org/tutorial/quickstart/

## Dependencias

# obtener lista de dependencias:

pip freeze

# guardar dependencias en requirements.txt

pip freeze > requirements.txt

# usar archivo requirements.txt para instalar dependencias:

pip install -r requirements.txt
