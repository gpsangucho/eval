from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['POST'])
def costo_reparaciones(request):
    try:
        cost = request.data.get('costo',[])    
    except(TypeError,ValueError):
        return Response({"error":"Parámetros inválidos"},status =status.HTTP_400_BAD_REQUEST)
    
    try:
        list = [float(n) for n in cost]
    except(TypeError,ValueError):
        return Response({"error":"Parámetros inválidos"},status =status.HTTP_400_BAD_REQUEST)
    
    i = 0
    total = 0
    while i < len(list):
        total = total + list[i]        
        i = i + 1
    
    for n in list:
        total+=n
    
    
    msg = ""
    if total < 100:
        msg = "Reparacion"
    elif total < 500 and total >100:
        msg = "Reparacion media"
    else:
        msg = "Repacion costosa"
    
    return Response({
        "Costo total":total,
        "Mensaje": msg
    })
    

@api_view(['POST'])
def cambio_aceite(request):
    try:
        Km_actual = request.data.get('km_actual',0)
        Km_LastCambio = request.data.get('km_ultimo_cambio',0)
        
    except(TypeError,ValueError):
        return Response({"error":"Parámetros inválidos"},status =status.HTTP_400_BAD_REQUEST)
    
    try:
        KmActual = float(Km_actual)
        KmLastCambio = float(Km_LastCambio)
        
    except(TypeError,ValueError):
        return Response({"error":"Parámetros inválidos"},status =status.HTTP_400_BAD_REQUEST)
    
    
    
    km_recorridos = KmActual - KmLastCambio
    
    if km_recorridos < 500:
        msg = "No es necesario cambio inmediato"
    elif km_recorridos>5000 and km_recorridos<8000:
        msg = "Recomendable programar cambio"
    elif km_recorridos>8000:
        msg = "Cambio urgente de aceite"

    return Response({
        "Km_recorridos":km_recorridos,
        "Mensaje": msg
    })
    
