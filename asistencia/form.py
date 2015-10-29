from django import forms
from django.forms import TextInput

class DatForm(forms.Form):
    archivo = forms.FileField(label='Seleccione Archivo de Asistencia')

class FechaForm(forms.Form):
    fecha = forms.DateField(label = 'Seleccion una Fecha', widget=forms.TextInput(attrs={'type':'date'}))
