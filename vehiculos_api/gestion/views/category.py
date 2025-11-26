# catalog/views/category.py
from rest_framework import viewsets, filters
from gestion.models import Category
from gestion.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
   
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("name","slug")
    ordering_fields = ("name","created_at")
