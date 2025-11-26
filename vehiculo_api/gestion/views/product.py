# catalog/views/product.py
from rest_framework import viewsets, filters
from gestion.models import Product
from gestion.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related("category").all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("placa","marca","modelo")
    ordering_fields = ("color","tipo","kilometraje")


