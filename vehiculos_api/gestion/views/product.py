# catalog/views/product.py
from rest_framework import viewsets, filters
from gestion.models import Product
from gestion.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related("category").all()
    serializer_class = ProductSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("placa","marca","modelo")
    ordering_fields = ("marca","tipo","anio")

    def get_queryset(self):
        qs = super().get_queryset()
        category = self.request.query_params.get("category")
        is_active = self.request.query_params.get("is_active")
        if category:
            qs = qs.filter(category__id=category)
        if is_active is not None:
            qs = qs.filter(is_active=is_active.lower() in ("1","true","t","yes"))
        return qs
