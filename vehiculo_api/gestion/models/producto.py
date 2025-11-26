# catalog/models/product.py
from django.db import models
#from .category import Category

class Product(models.Model):
    id = models.PositiveIntegerField(default=0)
    placa =  models.CharField(max_length=7)
    marca = models.CharField(max_length=160)
    modelo = models.CharField(max_length=160)
    anio =  models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=160)
    tipo = models.CharField(max_length=160)
    kilometraje = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_propietario = models.CharField(max_length=160)
    telefono_propietario = models.PositiveIntegerField(default=0)
    estado = models.CharField(max_length=160)
    

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return self.id


