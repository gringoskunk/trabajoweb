from django.db import models

# Create your models here.
class planta(models.Model):      # Creating model class
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=10)
    numero = models.IntegerField()

    def __str__(self):
        return self.nombre+self.tipo
        
