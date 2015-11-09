from django.forms import ModelForm
from django import forms

from carrera.models import Carrera
from gestion.models import Gestion
from carrera.models import Grupo

class GestionForm(ModelForm):
    class Meta:
        model = Gestion
        exclude = ['usuario']

class GestionCarreraForm(forms.Form):
    inscripcion = forms.FloatField(label='Costo Inscripcion', help_text='En Bolivianos')
    matricula = forms.FloatField(label='Costo Matricula', help_text='En Bolvianos')

class GrupoForm(ModelForm):
    class Meta:
        model = Grupo
        fields = '__all__'


class SearchCarreraForm(forms.Form):
    carrera = forms.ModelChoiceField(label='Seleccione Carrera', queryset = Carrera.objects.all())