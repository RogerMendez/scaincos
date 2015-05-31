#encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, AdminPasswordChangeForm
from django.contrib.auth.decorators import login_required

from django.db.models import Max

from usuarios.models import Persona
from gestion.models import Gestion

from estudiante.views import index_estudiante
from docente.views import index_docente

def index(request):
    return render(request, 'base.html', {
		})


def login_user(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect(reverse(info_usuario))
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    if  Persona.objects.filter(usuario = request.user):
                        persona = Persona.objects.get(usuario = request.user)
                        request.session['type'] = persona.tipo
                    else:
                        request.session['type'] = 'Admin'
                    if Gestion.objects.all():
                        g = Gestion.objects.all().values('gestion')
                        a = g.latest('gestion')
                        request.session['gestion'] = a['gestion']
                    else:
                        request.session['gestion'] = None
                    sms = 'Sesión Iniciada Correctamente'
                    messages.success(request, sms, )
                    if 'next' in request.GET:
                        return HttpResponseRedirect(str(request.GET['next']))
                    else:
                        return HttpResponseRedirect(reverse(info_usuario))
                else:
                    sms = 'Su Cuenta de Usuario No Esta Activada'
                    messages.warning(request, sms,)
                    return HttpResponseRedirect(reverse(login_user))
            else:
                sms = 'Usted No Es Usuario Registrado'
                #messages.warning(request, sms,)
                messages.error(request, sms, 'alert')
                #messages.info(request, sms, )
                #messages.success(request, sms, )
                return HttpResponseRedirect(reverse(login_user))
    else:
        formulario = AuthenticationForm()
    return render(request, 'usuarios/login.html',{
        'formulario':formulario,
    })

@login_required(login_url='/login')
def logout_user(request):
    logout(request)
    sms = 'Sesión Terminada Correctamente'
    messages.add_message(request, messages.INFO, sms)
    return HttpResponseRedirect('/')

@login_required(login_url='/login')
def info_usuario(request):
    if  request.session['type'] == 'Estudiante' :
        return HttpResponseRedirect(reverse(index_estudiante))
    if request.session['type'] == 'Docente' :
        return HttpResponseRedirect(reverse(index_docente))
    return render(request,'usuarios/info_usuario.html',{

    })

@login_required(login_url='/login')
def change_password(request):
    if request.method == 'POST':
        formulario = AdminPasswordChangeForm(user=request.user, data=request.POST)
        if formulario.is_valid():
            formulario.save()
            sms = "Contraseña Modificada Correctamente"
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(info_usuario))
    else:
        formulario = AdminPasswordChangeForm(user=request.user)
    return render(request, 'usuarios/change_password.html', {
        'formulario':formulario,
    })