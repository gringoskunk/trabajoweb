from django.db import models

class Usuario(models.model):
    nombre=models.CharField(max_length=30, primary_key=True)
    rut=models.CharField(max_length=15)
    apellido=models.Charfield(max_length=30)
    correo=models.EmailField()

class Producto(models.model):
    codigoBarra=models.CharField(max_length=60, primary_key=True)
    descripcion=models.CharField(max_length=200)
    precioCosto=models.IntegerField()
    precioVenta=models.IntegerField()
    marca=models.CharField(max_length=30)
    categoria=models.CharField(max_length=30)

class Categoria(models.model)
    marca=models.CharField(max_length=30)

