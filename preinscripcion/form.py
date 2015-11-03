from django import forms
from django.forms import TextInput
from django.forms import ModelForm
from django.core.exceptions import ValidationError

from preinscripcion.models import Preinscripcion
from usuarios.models import Persona, Estudiante


def validar_nro_estudiante(value):
    if Estudiante.objects.filter(nro_estudiante = value):
        raise ValidationError(u'%s Ya existe este numero de estudiante' % value)

class PreinscripcionForm(ModelForm):
    class Meta:
        model = Preinscripcion
        exclude = ['gestion', 'estado']
        widgets = {
            'fecha_nac':TextInput(attrs={'type':'date'}),
            }

class EstudianteForm(forms.Form):
    email = forms.EmailField(label='Correo Electronico')
    nro_estudiante = forms.IntegerField(label='Numero de estudiante', validators=[validar_nro_estudiante])
