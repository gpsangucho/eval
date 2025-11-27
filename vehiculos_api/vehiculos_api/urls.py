# billing_api/urls.py (añadir catálogo)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('api/', include('gestion.urls')),   # Parte 2: /api/categories/ y /api/products/
  path('api/', include('calculos.urls')),
  path('api/', include('reparaciones.urls')),
  path('api/', include('vehiculos.urls')),
]
