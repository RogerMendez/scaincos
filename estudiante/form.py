from django import forms
from django.forms import TextInput

from gestion.models import Gestion
from carrera.models import Carrera

class CarreraGestionForm(forms.Form):
    #gestion = forms.ModelChoiceField(label='Seleccione Gestion', queryset=Gestion.objects.all())
    carrera = forms.ModelChoiceField(label='Seleccione Carrera', queryset = Carrera.objects.all())

class EstudianteSearchForm(forms.Form):
    ci = forms.IntegerField(label='Cedula de Identidad')