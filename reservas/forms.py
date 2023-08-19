from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    # Campos del formulario para los detalles del cliente
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    correo_electronico = forms.EmailField(max_length=100)
    telefono = forms.CharField(max_length=15)

    class Meta:
        model = Reserva
        fields = ['nombre', 'apellido', 'correo_electronico', 'telefono', 'fecha_entrada', 'fecha_salida']
        widgets = {
            'fecha_entrada': forms.DateInput(attrs={'type': 'date'}),
            'fecha_salida': forms.DateInput(attrs={'type': 'date'}),
        }
        
