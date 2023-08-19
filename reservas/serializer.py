from rest_framework import serializers
from . models import Cliente, Habitacion, Reserva

class clienteSerializer():
    class Meta:
        model = Cliente
        fields = '__all__'
    
class habitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__'

class reservaSerializer():
    class Meta:
        model = Reserva
        fields = '__all__'