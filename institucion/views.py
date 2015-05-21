#encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

from scaincos.reportes import generar_pdf, sms_sesion
from scaincos.log_usuarios import log_addition, log_change

from institucion.models import Aula
from institucion.form import AulaForm

@permission_required('institucion.index_aula', login_url='/login')
def index_aula(request):
    aulas = Aula.objects.all()
    return render(request, 'aulas/index.html', {
        'aulas':aulas,
    })

@permission_required('institucion.add_aula', login_url='/login')
def new_aula(request):
    if request.method == 'POST':
        formulario = AulaForm(request.POST)
        if formulario.is_valid():
            a = formulario.save()
            log_addition(request, a, 'Aula Creada')
            sms = 'Aula Creada Correctamente'
            messages.info(request, sms)
            return  HttpResponseRedirect(reverse(index_aula))
    else:
        formulario = AulaForm()
    return render(request, 'aulas/new.html', {
        'formulario':formulario,
    })