from django.urls import path
from . import views

urlpatterns = [
    path('reparaciones/costo-total',views.costo_total),
]
