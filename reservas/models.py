from django.db import models

# Create your models here.

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo_electronico = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=15)


class Habitacion(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_habitacion = models.CharField(max_length=50)
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    capacidad = models.IntegerField()
    foto = models.ImageField(upload_to='habitacion_fotos/', blank=True, null=True)
    estado_reserva = models.CharField(max_length=20, choices=(('Disponible', 'Disponible'), ('Reservado', 'Reservado')), default='Disponible')

    def __str__(self):
        return self.tipo_habitacion


class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    estado_reserva = models.CharField(max_length=20)
    fecha_reservada = models.DateTimeField(auto_now_add=True)  # Cambio aquí

