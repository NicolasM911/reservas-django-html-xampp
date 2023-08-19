from django.contrib import admin
from .models import Cliente, Habitacion, Reserva

# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'correo_electronico', 'telefono')

@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('tipo_habitacion', 'precio_por_noche', 'capacidad')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'habitacion', 'fecha_entrada', 'fecha_salida', 'estado_reserva')