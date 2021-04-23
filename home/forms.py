from django import forms
from .models import *

class contacto_form(forms.Form):

    correo = forms.EmailField(widget = forms.TextInput())
    titulo = forms.CharField(widget = forms.TextInput())
    texto = forms.CharField(widget = forms.TextInput())

class agregar_producto_form(forms.ModelForm):
    class Meta:
            model = producto
            fields = '__all__'