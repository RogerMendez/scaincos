from django.forms import ModelForm
from django import forms

from inscripcion.models import Inscripcion

class InscripcionForm(forms.Form):
    costo = forms.FloatField(label='Costo de Inscripcion')