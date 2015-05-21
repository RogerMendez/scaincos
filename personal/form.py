#encodign:utf-8
from django.forms import ModelForm, TextInput
from django import forms

from usuarios.models import Persona, Administrativo, Estudiante, Docente

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        exclude = ['usuario', 'activo', 'tipo']
        widgets = {
            'fecha_nac':TextInput(attrs={'type':'date'}),

            }

class AdministrativoForm(ModelForm):
    class Meta:
        model = Administrativo
        exclude = ['persona']

class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        exclude = ['persona', 'fecha_salida', 'terminado']

class DocenteForm(ModelForm):
    class Meta:
        model = Docente
        exclude = ['persona']
        widgets = {
            'fecha_ingreso':TextInput(attrs={'type':'date'}),

            }