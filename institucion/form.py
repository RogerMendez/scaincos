#encodign:utf-8
from django.forms import ModelForm

from institucion.models import Aula

class AulaForm(ModelForm):
    class Meta:
        model = Aula