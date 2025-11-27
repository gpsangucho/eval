from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['POST'])
def costo_total(request):
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