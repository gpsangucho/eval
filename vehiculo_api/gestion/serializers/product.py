# catalog/serializers/product.py
from rest_framework import serializers
from gestion.models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("id","placa","marca","modelo","anio","color","tipo","kilometraje",
                  "nombre_propietario","telefono_propietario","estado")
        read_only_fields = ("id","placa","estado")


