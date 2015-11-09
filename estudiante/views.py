#encoding:utf-8
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
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

from inscripcion.form import FolioLibroForm
from estudiante.form import CarreraGestionForm, EstudianteSearchForm

import datetime

@login_required(login_url='/login')
def index_estudiante(request):
    persona = get_object_or_404(Persona, usuario = request.user)
    estudiante = Estudiante.objects.get(persona = persona)
    insc = Inscripcion.objects.get(estudiante = estudiante, estado = True, terminado = False)

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
            re = programados.filter(final__lte = 50)
            reprobados = re.filter(id__in = aprobados.values('id'))
            #print aprobados
            #print reprobados
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

@permission_required('usuarios.report_estudiante', login_url='/login')
def index_notas(request):
    carrera = Carrera.objects.first()
    formulario = CarreraGestionForm(request.GET or None)
    if formulario.is_valid():
        c_id = request.GET['carrera']
        carrera = Carrera.objects.get(pk = int(c_id))
    inscripiones = Inscripcion.objects.filter(carrera = carrera, estado = True)
    return render(request, 'notas/index.html', {
        'formulario':formulario,
        'carrera':carrera,
        'inscripciones':inscripiones,
    })

def ajax_buscar_estudiantes(request):
    if request.is_ajax():
        carrera_id = request.GET['carrera']
        ci = request.GET['ci']
        carrera = get_object_or_404(Carrera, pk = carrera_id)
        #personas = Persona.objects.filter(ci__icontains = ci)
        estudiantes = Estudiante.objects.filter(persona__ci__icontains = ci)
        inscripciones = Inscripcion.objects.filter(carrera = carrera, estado = True, estudiante_id__in = estudiantes.values('id'))
        html = render_to_string('notas/ajax_inscripciones_carrera.html', {
            'inscripciones':inscripciones,
        }, context_instance=RequestContext(request))
        return JsonResponse(html, safe=False)
    else:
        raise Http404

@permission_required('usuarios.report_estudiante', login_url='/login')
def notas_estudiante(request, insc_id):
    inscripcion = get_object_or_404(Inscripcion, pk = insc_id)
    programaciones = Programacion.objects.filter(inscripcion = inscripcion)
    gestiones = Gestion.objects.all()
    return render(request, 'notas/notas_estudiante.html', {
        'inscripcion':inscripcion,
        'programaciones':programaciones,
        'gestiones':gestiones,
    })

def ajax_notas_estudiante(request):
    if request.is_ajax():
        gestion_id = request.GET['gestion_id']
        insc_id = request.GET['insc_id']
        inscripcion = get_object_or_404(Inscripcion, pk = insc_id)
        gestion = get_object_or_404(Gestion, pk = gestion_id)
        programaciones = Programacion.objects.filter(inscripcion = inscripcion, gestion = gestion)
        html = render_to_string('notas/ajax_notas_estudiante.html', {
            'programaciones':programaciones,
            'gestion':gestion,
        }, context_instance=RequestContext(request))
        return JsonResponse(html, safe=False)
    else:
        raise Http404

@permission_required('usuarios.report_estudiante', login_url='/login')
def notas_gestion_carreras(request):
    gestiones = Gestion.objects.all()
    carreras = Carrera.objects.all()
    return render(request, 'notas/notas_gestion_carrera.html', {
        'gestiones':gestiones,
        'carreras':carreras,
    })

def ajax_niveles_carrera(request):
    if request.is_ajax():
        carrera_id = request.GET['carrera']
        carrera = get_object_or_404(Carrera, pk = carrera_id)
        rango = range(0, int(carrera.tiempo), 1)
        html = render_to_string('notas/ajax_niveles_carrera.html', {
            'carrera':carrera,
            'rango':rango,
        }, context_instance=RequestContext(request))
        return JsonResponse(html, safe=False)
    else:
        raise Http404

def ajax_notas_estudiantes_gestion_carrera(request):
    if request.is_ajax():
        gestion_id = request.GET['gestion']
        carrera_id = request.GET['carrera']
        nivel = request.GET['nivel']
        gestion = get_object_or_404(Gestion, pk = gestion_id)
        carrera = get_object_or_404(Carrera, pk = carrera_id)
        materias = Materia.objects.filter(carrera = carrera, nivel = nivel)
        programaciones = Programacion.objects.filter(gestion = gestion, materia_id__in = materias.values('id')).distinct()
        inscripciones = Inscripcion.objects.filter(id__in = programaciones.values('inscripcion_id'))
        estudiantes = Estudiante.objects.filter(id__in = inscripciones.values('estudiante_id')).order_by('persona__paterno', 'persona__materno', 'persona__nombre')
        html = render_to_string('notas/ajax_notas_gestion_nivel.html', {
            'nivel':nivel,
            'gestion':gestion,
            'carrera':carrera,
            'materias':materias,
            'estudiantes':estudiantes,

        }, context_instance=RequestContext(request))
        return JsonResponse(html, safe=False)
    else:
        raise Http404

@permission_required('usuarios.report_estudiante', login_url='/login')
def pdf_notas_gestion_carrera(request, gestion_id, carrera_id, nivel):
    gestion = get_object_or_404(Gestion, pk = gestion_id)
    carrera = get_object_or_404(Carrera, pk = carrera_id)
    materias = Materia.objects.filter(carrera = carrera, nivel = nivel)
    programaciones = Programacion.objects.filter(gestion = gestion, materia_id__in = materias.values('id')).distinct()
    inscripciones = Inscripcion.objects.filter(id__in = programaciones.values('inscripcion_id'))
    estudiantes = Estudiante.objects.filter(id__in = inscripciones.values('estudiante_id')).order_by('persona__paterno', 'persona__materno', 'persona__nombre')
    html = render_to_string('notas/pdf_notas_gestion_estudiante.html', {
        'nivel':nivel,
        'gestion':gestion,
        'carrera':carrera,
        'materias':materias,
        'estudiantes':estudiantes,
    }, context_instance=RequestContext(request))
    return generar_pdf(html)

@permission_required('usuarios.report_estudiante', login_url='/login')
def estudiantes_finalizacion(request):
    carrera = Carrera.objects.first()
    formulario = CarreraGestionForm(request.GET or None)
    if formulario.is_valid():
        c_id = request.GET['carrera']
        carrera = Carrera.objects.get(pk = int(c_id))
    materias = Materia.objects.filter(carrera = carrera, nivel = int(carrera.tiempo))
    programaciones = Programacion.objects.filter(materia_id__in = materias.values('id'), final__gte = 51)
    inscripciones = Inscripcion.objects.filter(id__in = programaciones.values('inscripcion_id'), estado = True)
    return render(request, 'notas/estudiantes finalizacion.html', {
        'formulario':formulario,
        'carrera':carrera,
        'inscripciones':inscripciones,
    })

@permission_required('usuarios.report_estudiante', login_url='/login')
def historial_notas(request, insc_id):
    inscripcion = get_object_or_404(Inscripcion, pk = insc_id)
    programaciones = Programacion.objects.filter(inscripcion = inscripcion, final__gte = 51).order_by('materia__nivel')
    return render(request, 'notas/historial_notas.html', {
        'inscripcion':inscripcion,
        'programaciones':programaciones,
    })

@permission_required('usuarios.report_estudiante', login_url='/login')
def crear_folio_libro(request, insc_id):
    inscripcion = get_object_or_404(Inscripcion, pk = insc_id)
    if request.method == 'POST':
        formulario = FolioLibroForm(request.POST, instance=inscripcion)
        if formulario.is_valid():
            formulario.save()
            sms = 'Numero de Folio Creado Correctamente'
            messages.info(request, sms)
            return HttpResponseRedirect(reverse(historial_notas, args={inscripcion.id,}))
    else:
        formulario = FolioLibroForm(instance=inscripcion)
    return render(request, 'notas/nro_folio_form.html', {
        'inscripcion':inscripcion,
        'formulario':formulario,
    })

@permission_required('usuarios.report_estudiante', login_url='/login')
def pdf_certificado_calificaciones(request, insc_id):
    inscripcion = get_object_or_404(Inscripcion, pk = insc_id)
    hoy = datetime.datetime.now()
    gestion = get_object_or_404(Gestion, gestion = request.session['gestion'])
    carrera = Carrera.objects.get(id = inscripcion.carrera.id)
    materias = Materia.objects.filter(carrera = carrera, nivel = int(carrera.tiempo))
    programaciones = Programacion.objects.filter(materia_id__in = materias.values('id'), final__gte = 51, inscripcion = inscripcion)
    html = render_to_string('notas/pdf_certificado_calificaciones.html', {
        'inscripcion':inscripcion,
        'gestion':gestion,
        'fecha':hoy,
        'programaciones':programaciones,
    }, context_instance=RequestContext(request))
    return generar_pdf(html)