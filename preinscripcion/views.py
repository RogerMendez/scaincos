#encoding:utf-8
from django.shortcuts import render, RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, AdminPasswordChangeForm
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMultiAlternatives

from scaincos.reportes import sms_sesion, generar_pdf
from scaincos.log_usuarios import log_addition, log_change
from personal.views import password_create

from django.contrib.auth.models import User
from usuarios.models import Persona, Estudiante
from gestion.models import Gestion
from carrera.models import Carrera
from carrera.form import CarrerasForm
from preinscripcion.models import Preinscripcion
from preinscripcion.form import PreinscripcionForm, EstudianteForm
from inscripcion.views import info_new_inscripxion

def new_preinscripcion(request):
    if request.method == 'POST':
        formulario = PreinscripcionForm(request.POST, request.FILES)
        if formulario.is_valid():
            pre = formulario.save()
            pre.gestion = Gestion.objects.last()
            pre.save()
            sms = "Preinscripcion Registrada Correctamente"
            messages.info(request, sms)
            return HttpResponseRedirect('/')
    else:
        formulario = PreinscripcionForm()
    return render(request, 'preinscripcion/new.html', {
        'formulario':formulario,
    })

@permission_required('preinscripcion.index_preinscripcion', login_url='/login')
def index_preinscripcion(request):
    sms_sesion(request)
    gestion = get_object_or_404(Gestion, gestion = request.session['gestion'])
    carrera = Carrera.objects.first()
    formulario = CarrerasForm(request.GET or None)
    if formulario.is_valid():
        id = request.GET['carrera']
        carrera = Carrera.objects.get(id = int(id))
    preinscripciones = Preinscripcion.objects.filter(gestion = gestion, carrera = carrera)
    return render(request, 'preinscripcion/index.html', {
        'carrera':carrera,
        'preinsctipciones':preinscripciones,
        'formulario':formulario,
    })

@permission_required('preinscripcion.create_inscripcion', login_url='/login')
def list_preinscripciones_gestion(request):
    sms_sesion(request)
    gestion = get_object_or_404(Gestion, gestion = request.session['gestion'])
    gestion1 = Gestion.objects.last()
    carrera = Carrera.objects.first()
    formulario = CarrerasForm(request.GET or None)
    if formulario.is_valid():
        id = request.GET['carrera']
        carrera = Carrera.objects.get(pk = int(id))
    preinscripciones = Preinscripcion.objects.filter(gestion = gestion, carrera = carrera)
    return render(request, 'preinscripcion/list_preincripciones_gestion.html', {
        'gestion':gestion1,
        'carrera':carrera,
        'formulario':formulario,
        'preinscripciones':preinscripciones,
    })

@permission_required('preinscripcion.create_inscripcion', login_url='/login')
def new_inscripcion(request, pre_id):
    pre = get_object_or_404(Preinscripcion, pk = pre_id)
    if request.method == 'POST':
        formulario = EstudianteForm(request.POST)
        if formulario.is_valid():
            password = password_create()
            email = formulario.cleaned_data['email']
            nro_estu = formulario.cleaned_data['nro_estudiante']
            usuario = User.objects.create_user(pre.ci, email, password)
            persona = Persona.objects.create(
                ci = pre.ci,
                nombre = pre.nombre,
                paterno = pre.paterno,
                materno = pre.materno,
                fecha_nac = pre.fecha_nac,
                direccion = pre.direccion,
                telefono = pre.telefono,
                avatar = pre.avatar,
                tipo = 'Estudiante',
                email = email,
                usuario = usuario,
            )
            estudiante = Estudiante.objects.create(
                nro_estudiante = nro_estu,
                persona = persona,
            )
            pre.estado = False
            pre.save()
            log_addition(request, persona, 'Persona Creada')
            log_addition(request, estudiante, 'Estudiante Creado')
            html = render_to_string('estudiante/email_confimacion.html',{
                'username':usuario.username,
                'password':password,
            }, context_instance=RequestContext(request))
            subject = 'Cuenta Creada Correctamente'
            text_content = 'Mensaje...nLinea 2nLinea3'
            html_content = html
            from_email = '"INCOS" <sieboliva@gmail.com>'
            to = persona.email
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            sms = "Estudiante Creado Correctamente"
            messages.success(request, sms)
            sms = "Un mensaje fue enviado a <strong>%s</strong> con los datos de su Cuenta"% (persona.email)
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(info_new_inscripxion, args={pre.carrera_id, estudiante.id}))
    else:
        formulario = EstudianteForm()
    return render(request, 'preinscripcion/new_estudiante.html', {
        'formulario':formulario,
        'preinscripcion':pre,
    })