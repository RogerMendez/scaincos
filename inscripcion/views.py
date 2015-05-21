#encoding:utf-8
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django import template
from django.contrib.auth.models import User

from scaincos.reportes import generar_pdf, sms_sesion
from scaincos.log_usuarios import log_addition, log_change

from usuarios.models import Estudiante
from personal.form import PersonaForm, EstudianteForm
from personal.views import password_create
from carrera.models import Carrera
from gestion.models import Gestion, Gestion_Carrera
from inscripcion.models import Inscripcion, Matricula

register = template.Library()

@permission_required('inscripcion.index_inscripcion', login_url='/login')
def index_inscripcion(request):
    sms_sesion(request)
    gestion = Gestion.objects.get(gestion = request.session['gestion'])
    inscripciones = Inscripcion.objects.filter(gestion = gestion)
    return render(request, 'inscripcion/index.html', {
        'inscripciones':inscripciones,
    })

@permission_required('inscripcion.add_inscripcion')
def select_carrera_inscripcion(request):
    sms_sesion(request)
    gestion = Gestion.objects.get(gestion = request.session['gestion'])
    g_c = Gestion_Carrera.objects.filter(gestion = gestion)
    carreras = Carrera.objects.filter(id__in = g_c.values('carrera_id'))
    return render(request, 'inscripcion/carreras_new_inscripcion.html', {
        'carreras':carreras,
    })

@permission_required('inscripcion.add_inscripcion')
def new_estudiante(request, carrera_id):
    carrera = get_object_or_404(Carrera, pk = carrera_id)
    if request.method == 'POST':
        perform = PersonaForm(request.POST, request.FILES)
        estform = EstudianteForm(request.POST)
        if perform.is_valid() and estform.is_valid():
            password = password_create()
            p = perform.save()
            u = User.objects.create_user(str(p.ci), p.email, password)
            p.usuario = u
            p.tipo = 'Estudiante'
            p.save()
            e = estform.save()
            e.persona = p
            e.save()
            u.email = p.email
            u.first_name = p.nombre
            u.last_name = p.paterno + ' ' + p.materno
            u.save()
            log_addition(request, p, 'Persona Creada')
            log_addition(request, u, 'Usuario Creado')
            log_addition(request, e, 'Estudiante Creado')
            html = render_to_string('estudiante/email_confimacion.html',{
                'username':u.username,
                'password':password,
            }, context_instance=RequestContext(request))
            subject = 'Cuenta Creada Correctamente'
            text_content = 'Mensaje...nLinea 2nLinea3'
            html_content = html
            from_email = '"INCOS" <sieboliva@gmail.com>'
            to = p.email
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            sms = "Estudiante Creado Correctamente"
            messages.success(request, sms)
            sms = "Un mensaje fue enviado a <strong>%s</strong> con los datos de su Cuenta"% (p.email)
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(info_new_inscripxion, args=(carrera.id, e.id, )))
    else:
        perform = PersonaForm()
        estform = EstudianteForm()
    return render(request, 'inscripcion/new_estudiante.html', {
        'perform':perform,
        'estform':estform,
    })

@permission_required('inscripcion.add_inscripcion')
def info_new_inscripxion(request, carrera_id, estu_id):
    sms_sesion(request)
    carrera = get_object_or_404(Carrera, pk = carrera_id)
    estudiante = get_object_or_404(Estudiante, pk = estu_id)
    gestion = Gestion.objects.get(gestion = request.session['gestion'])
    g_c = Gestion_Carrera.objects.get(gestion = gestion, carrera = carrera)
    return render(request, 'inscripcion/info_new_inscripcion.html', {
        'carrera':carrera,
        'estudiante':estudiante,
        'ges_ca':g_c,
    })

@permission_required('inscripcion.add_inscripcion')
def confirm_new_inscripcion(request, carrera_id, estu_id):
    carrera = get_object_or_404(Carrera, pk = carrera_id)
    estudiante = get_object_or_404(Estudiante, pk = estu_id)
    gestion = Gestion.objects.get(gestion = request.session['gestion'])
    g_c = Gestion_Carrera.objects.get(gestion = gestion, carrera = carrera)
    i = Inscripcion.objects.create(
        c_inscripcion = g_c.c_inscripcion,
        estudiante = estudiante,
        carrera = carrera,
        gestion = gestion,
        usuario = request.user,
    )
    log_addition(request, i, 'Inscripcion Creada')
    sms = "Estudiante <strong>%s %s, %s</strong> Inscrito Correctamente"%(estudiante.persona.paterno, estudiante.persona.materno, estudiante.persona.nombre)
    messages.info(request, sms)
    return HttpResponseRedirect(reverse(index_inscripcion))

@permission_required('inscripcion.index_matricula', login_url='/login')
def index_matricula(request):
    sms_sesion(request)
    print request.session['gestion']
    gestion = Gestion.objects.get(gestion = request.session['gestion'])
    #inscripciones = Inscripcion.objects.filter(gestion = gestion)
    #matriculas = Matricula.objects.filter(inscripcion_id__in = inscripciones.values('id'))
    matriculas = Matricula.objects.filter(gestion = gestion)
    return render(request, 'matricula/index.html', {
        'matriculas':matriculas,
    })

@permission_required('inscripcion.add_matricula', login_url='login')
def select_carrera_new_matricula(request):
    sms_sesion(request)
    gestion = Gestion.objects.get(gestion = request.session['gestion'])
    g_c = Gestion_Carrera.objects.filter(gestion = gestion)
    carreras = Carrera.objects.filter(id__in = g_c.values('carrera_id'))
    return render(request, 'matricula/carreras_new_matricula.html', {
        'carreras':carreras,
    })

@permission_required('inscripcion.add_matricula', login_url='/login')
def info_new_matricula(request, carrera_id, estu_id):
    sms_sesion(request)
    carrera = get_object_or_404(Carrera, pk = carrera_id)
    estudiante = get_object_or_404(Estudiante, pk = estu_id)
    gestion = Gestion.objects.get(gestion = request.session['gestion'])
    g_c = Gestion_Carrera.objects.get(gestion = gestion, carrera = carrera)
    return render(request, 'matricula/info_new_matricula.html', {
        'carrera':carrera,
        'estudiante':estudiante,
        'ges_ca':g_c,
    })

@permission_required('inscripciones.add_matricula', login_url='/login')
def confirm_new_matricula(request, g_c_id, estu_id):
    g = Gestion.objects.get(gestion = request.session['gestion'])
    g_c = get_object_or_404(Gestion_Carrera, pk = g_c_id)
    carrera = Carrera.objects.get(id = g_c.carrera_id)
    estudiante = get_object_or_404(Estudiante, pk = estu_id)
    inscripcion = Inscripcion.objects.get(estudiante = estudiante, carrera = carrera)
    matri = Matricula.objects.create(
        costo = g_c.c_matricula,
        inscripcion = inscripcion,
        gestion = g,
        usuario = request.user,
    )
    log_addition(request, matri, 'Matricula Creada')
    return HttpResponseRedirect(reverse(index_matricula))
