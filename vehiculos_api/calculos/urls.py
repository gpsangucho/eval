from django.urls import path
from . import views

urlpatterns = [
    path('calculos/cambio-aceite',views.cambio_aceite),
    path('calculos/costo-reparaciones',views.costo_reparaciones),
]


