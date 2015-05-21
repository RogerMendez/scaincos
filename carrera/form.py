from django.forms import ModelForm, TextInput

from carrera.models import Carrera, Materia

class CarreraForm(ModelForm):
    class Meta:
        model = Carrera
        field = ['nombre', 'tiempo', 'fecha_creaion', 'resenha']
        exclude = ['']
        widgets = {
            'fecha_creacion':TextInput(attrs={'type':'date'}),
        }

class MateriaForm(ModelForm):
    class Meta:
        model = Materia
        exclude = ['requisito']