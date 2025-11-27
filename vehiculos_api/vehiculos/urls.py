from django.urls import path
from . import views

urlpatterns = [
    path('vehiculos/cambio-aceite',views.cambio_aceite),
]