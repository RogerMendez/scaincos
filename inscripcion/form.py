#encodign:utf-8
from django.forms import ModelForm, TextInput
from django import forms

from inscripcion.models import Inscripcion

class InscripcionForm(forms.Form):
    costo = forms.FloatField(label='Costo de Inscripcion')

class FolioLibroForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        exclude = ['c_inscripcion', 'estudiante', 'carrera', 'gestion', 'usuario', 'estado', 'terminado']
        widgets = {
            'nro_folio':TextInput(attrs={'type':'number'}),
            }