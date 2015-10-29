from django import forms
from django.forms import ModelForm

from estudiante.models import Programacion

class NotasForm(ModelForm):
    class Meta:
        model = Programacion
        exclude = ['inscripcion', 'materia', 'grupo', 'gestion', 'final']