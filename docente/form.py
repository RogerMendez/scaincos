from django import forms
from django.forms import ModelForm

from estudiante.models import Programacion
import os
class NotasForm(ModelForm):
    class Meta:
        model = Programacion
        exclude = ['inscripcion', 'materia', 'grupo', 'gestion', 'final']

IMPORT_FILE_TYPES = ['.xls', '.xlsx', ]

class NotasExcelForm(forms.Form):
    input_excel = forms.FileField(label= u"Seleccione el archivo EXCEL para subir notas.")

    def clean_input_excel(self):
        input_excel = self.cleaned_data['input_excel']
        extension = os.path.splitext( input_excel.name )[1]
        if not (extension in IMPORT_FILE_TYPES):
            raise forms.ValidationError( u'El archivo seleccionado no es de tipo excel' )
            #raise forms.ValidationError( u'%s is not a valid excel file. Please make sure your input file is an excel file (Excel 2007 is NOT supported.' % extension )
        else:
            return input_excel