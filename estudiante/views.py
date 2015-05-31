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

from django.contrib.auth.models import User

from scaincos.reportes import generar_pdf, sms_sesion
from scaincos.log_usuarios import log_addition, log_change

from gestion.models import Gestion
from usuarios.models import Estudiante, Persona
from inscripcion.models import Inscripcion
from carrera.models import Materia, Carrera, Requisitos
from estudiante.models import Programacion, Notas

@login_required(login_url='/login')
def index_estudiante(request):
    persona = get_object_or_404(Persona, usuario = request.user)
    estudiante = Estudiante.objects.get(persona = persona)
    insc = Inscripcion.objects.get(estudiante = estudiante, estado = True)

    return render(request, 'modestudiante/index.html', {
        'persona':persona,
        'estudiante':estudiante,
        'inscripcion':insc,
    })

@login_required(login_url='/login')
def programacion(request):
    sms_sesion(request)
    gestion = get_object_or_404(Gestion, gestion = request.session['gestion'])
    persona = get_object_or_404(Persona, usuario = request.user)
    estudiante = Estudiante.objects.get(persona = persona)
    insc = Inscripcion.objects.get(estudiante = estudiante, estado = True)
    carrera = Carrera.objects.get(id = insc.carrera_id)
    programados = Programacion.objects.filter(inscripcion = insc)
    p_programados = Programacion.objects.exclude(gestion = gestion).filter(inscripcion = insc)
    materias = Materia.objects.filter(carrera = carrera)
    mat_id = []
    if not programados:
        materias = Materia.objects.filter(carrera = carrera, nivel = 1)
    else:
        if not p_programados:
            materias = materias.filter(nivel = 1)
        else:
            aprobados = programados.filter(final__gte = 51)
            reprobados = programados.filter(final__lte = 50).exclude(id__in = aprobados.values('id'))
            for r in reprobados:
                mat_id += [r.materia_id]
            p_g = programados.filter(gestion = gestion)
            for p in p_g:
                mat_id += [p.materia_id]
            no_mate = materias.exclude(id__in = mat_id).exclude(id__in = aprobados.values('materia_id'))
            for m in no_mate:
                requisito = Requisitos.objects.filter(from_materia = m)
                cant = requisito.count()
                cont = 0
                for r in requisito:
                    if aprobados.filter(materia_id = r.to_materia_id):
                        cont += 1
                if cont == cant:
                    mat_id += [m.id]
            materias = materias.filter(id__in = mat_id)


    return render(request, 'modestudiante/programacion.html', {
        'materias':materias,
        'programados':programados,
        'inscripcion':insc,
    })

@login_required(login_url='/login')
def programar(request):
    gestion = get_object_or_404(Gestion, gestion = request.session['gestion'])
    persona = get_object_or_404(Persona, usuario = request.user)
    estudiante = Estudiante.objects.get(persona = persona)
    insc = Inscripcion.objects.get(estudiante = estudiante, estado = True)

    grupo = request.GET['grupo']
    materia = request.GET['materia']
    if not grupo:
        grupo = 1
    pro = Programacion.objects.create(
        inscripcion = insc,
        materia_id = materia,
        grupo_id = grupo,
        gestion = gestion
    )
    log_addition(request, pro, 'Programacion Creada')
    sms = "Materia Programada Correctamente"
    messages.info(request, sms)
    return HttpResponseRedirect(reverse(programacion))


@login_required(login_url='/login')
def notas(request):
    sms_sesion(request)
    gestion = get_object_or_404(Gestion, gestion = request.session['gestion'])
    persona = get_object_or_404(Persona, usuario = request.user)
    estudiante = Estudiante.objects.get(persona = persona)
    insc = Inscripcion.objects.get(estudiante = estudiante, estado = True)
    programados = Programacion.objects.filter(inscripcion = insc, gestion = gestion)
    return render(request, 'modestudiante/notas_estudiante.html', {
        'programaciones':programados,
        'estudiante':estudiante,
    })