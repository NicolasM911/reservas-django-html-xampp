from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Cliente, Habitacion, Reserva
from .forms import ReservaForm
from django.core.exceptions import ValidationError
from datetime import datetime

from rest_framework import viewsets
from .serializer import clienteSerializer, habitacionSerializer , reservaSerializer

# Create your views here.
class clienteView(viewsets.ModelViewSet):
    serializer_class = clienteSerializer
    queryset = Cliente.objects.all()

class habitacionView(viewsets.ModelViewSet):
    serializer_class = habitacionSerializer
    queryset = Habitacion.objects.all()

class reservaView(viewsets.ModelViewSet):
    serializer_class = reservaSerializer
    queryset = Reserva.objects.all()

# def inicio(request):
#     return HttpResponse("Bienvenido hotel nicolas")

def inicio_view(request):
    #clientes = Cliente.objects.all()
    habitaciones = Habitacion.objects.all()
    reservas = Reserva.objects.all()

    context = {
        #'clientes': clientes,
        'habitaciones': habitaciones,
        'reservas': reservas,
    }

    return render(request, 'inicio.html', context)








def reservar_view(request, habitacion_id):
    try:
        habitacion = Habitacion.objects.get(pk=habitacion_id)
    except Habitacion.DoesNotExist:
        return redirect('inicio')
    
    reservacion_exitosa = False  # Variable para controlar la visualización de la alerta
    
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            cliente = Cliente.objects.create(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                correo_electronico=form.cleaned_data['correo_electronico'],
                telefono=form.cleaned_data['telefono']
            )
            reserva = form.save(commit=False)
            reserva.cliente = cliente
            reserva.habitacion = habitacion
            reserva.estado_reserva = 'Reservado'  # Cambia el estado de la reserva
            reserva.save()
            reservacion_exitosa = True
    else:
        form = ReservaForm()
    
    context = {
        'habitacion': habitacion,
        'form': form,
        'reservacion_exitosa': reservacion_exitosa,
    }
    
    return render(request, 'reservas.html', context)









