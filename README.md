# Instrucciones del repo trabajoweb

## Crear entorno virtual para instalar las dependencias localmente

```
python -m venv env
source env/Scripts/activate # En windows usar `env\Scripts\activate`
```

## levantar proyecto:

py manage.py runserver

## migrar modelos

```
python manage.py makemigrations
python manage.py migrate
```

# Instrucciones para crear una API con django rest:

https://www.django-rest-framework.org/tutorial/quickstart/

# Dependencias

## obtener lista de dependencias:

pip freeze

## guardar dependencias en requirements.txt

pip freeze > requirements.txt

## usar archivo requirements.txt para instalar dependencias:

pip install -r requirements.txt

<!-- 🍻🍻🍻 -->
