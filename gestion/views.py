#encoding:utf-8
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django import template

from scaincos.reportes import generar_pdf, sms_sesion
from scaincos.log_usuarios import log_addition, log_change

from usuarios.models import Docente, Persona, Estudiante
from institucion.models import Aula
from carrera.models import Carrera, Materia, Grupo
from gestion.models import Gestion, Gestion_Carrera, AsignacionDocente, Horario
from gestion.form import GestionForm, GestionCarreraForm
from estudiante.models import Inscripcion, Programacion

register = template.Library()

@login_required(login_url='/login')
def index_gestion(request):
    gestiones = Gestion.objects.all()
    #sms = 'Usted Se Encuentra en la Gestion <strong>%s</strong>' %(request.session['gestion'])
    #messages.info(request, sms)
    sms_sesion(request)
    return render(request, 'gestion/index.html', {
        'gestiones':gestiones,
    })

@permission_required('gestion.add_gestion', login_url='/login')
def new_gestion(request):
    if request.method == 'POST':
        formulario = GestionForm(request.POST)
        if formulario.is_valid():
            g = formulario.save()
            g.usuario = request.user
            g.save()
            log_addition(request, g, 'Gestion Creada')
            sms = 'Gestion <strong>%s</strong> Creada Correctamente'% (g.gestion)
            messages.info(request, sms)
            return HttpResponseRedirect(reverse(index_gestion))
    else:
        formulario = GestionForm()
    return render(request, 'gestion/new.html', {
        'formulario':formulario,
    })

@login_required(login_url='/login')
def change_gestion_session(requesr, gestion_id):
    gestion = get_object_or_404(Gestion, pk = gestion_id)
    requesr.session['gestion'] = gestion.gestion
    return HttpResponseRedirect(reverse(index_gestion))

@permission_required('gestion.add_gestion_carrera', login_url='/login')
def list_carreras_gestion(request):
    sms_sesion(request)
    gestion = get_object_or_404(Gestion, gestion = request.session['gestion'])
    asignados = Gestion_Carrera.objects.filter(gestion = gestion)
    s_asignar = Carrera.objects.exclude(id__in = asignados.values('carrera_id'))
    return render(request, 'gestion/list_carreras_gestion.html', {
        'gestion':gestion,
        'asignados':asignados,
        'S_asignar':s_asignar,
    })

@permission_required('gestion.add_gestion_carrera', login_url='/login')
def add_carrera_gestion(request, carrera_id):
    gestion = get_object_or_404(Gestion, gestion = request.session['gestion'])
    carrera = get_object_or_404(Carrera, pk = carrera_id)
    if request.method == 'POST':
        formulario = GestionCarreraForm(request.POST)
        if formulario.is_valid():
            inscripcion = formulario.cleaned_data['inscripcion']
            matricula = formulario.cleaned_data['matricula']
            g_c = Gestion_Carrera.objects.create(
                gestion = gestion,
                carrera = carrera,
                c_inscripcion = inscripcion,
                c_matricula = matricula,
            )
            log_addition(request, g_c, 'Carrera Asignada')
            log_change(request, gestion, 'Carrera '+carrera.nombre+' Asignada')
            sms = 'Carrera <strong>%s</strong> Asignada Correctamente'%(carrera.nombre)
            messages.info(request, sms)
            return HttpResponseRedirect(reverse(list_carreras_gestion))
    else:
        formulario = GestionCarreraForm()
    return render(request, 'gestion/add_carrera_gestion.html', {
        'formulario':formulario,
    })


@permission_required('gestion.add_docente_gestion', login_url='/login')
def asignar_select_docente(request):
    docentes = Docente.objects.all()
    return render(request, 'gestion/list_docente_asignacion.html', {
        'docentes':docentes,
    })

@permission_required('gestion.add_docente_gestion', login_url='/login')
def asignar_materia_docente(request, docente_id):
    sms_sesion(request)
    docente = get_object_or_404(Docente, pk = docente_id)
    gestion = get_object_or_404(Gestion, gestion = request.session['gestion'])
    asignados = Gestion_Carrera.objects.filter(gestion = gestion)

    return render(request, 'gestion/asignar_materia_docente.html', {
        'docente':docente,
        'asignados':asignados,
    })

@permission_required('gestion.add_docente_gestion', login_url='/login')
def add_materia_docente(request, docente_id, materia_id, grupo_id):
    gestion = get_object_or_404(Gestion, gestion = request.session['gestion'])
    docente = get_object_or_404(Docente, pk = docente_id)
    materia = get_object_or_404(Materia, pk = materia_id)
    grupo = get_object_or_404(Grupo, pk = grupo_id)
    a = AsignacionDocente.objects.create(
        gestion = gestion,
        docente = docente,
        materia = materia,
        grupo = grupo,
    )
    log_addition(request, a, 'Asignacion Creada')
    log_change(request, docente, 'Materia Asignada')
    sms = "Asignacion Creada Correctamente"
    messages.info(request, sms)
    return HttpResponseRedirect(reverse(asignar_materia_docente, args={docente.id, }))

@permission_required('gestion.delete_asignaciondocente', login_url='/login')
def remove_asignacion(request, asign_id):
    asignacion = get_object_or_404(AsignacionDocente, pk = asign_id)
    asignacion.delete()
    sms = 'Asignacion Terminada Correctamente'
    messages.info(request, sms)
    return HttpResponseRedirect(reverse(asignar_materia_docente, args={asignacion.docente_id, }))

@login_required(login_url='/login')
def ajax_materias_carrera(request):
    gestion = get_object_or_404(Gestion, gestion = request.session['gestion'])
    if request.is_ajax():
        id = request.GET['carrera_id']
        d_id = request.GET['docente_id']
        carrera = get_object_or_404(Carrera, pk = id)
        docente = get_object_or_404(Docente, pk = d_id)
        asignaciones = AsignacionDocente.objects.filter(gestion = gestion, docente = docente)
        materias = Materia.objects.filter(carrera = carrera)
        #materias = materias.exclude(id__in = asignaciones.values('materia_id'))
        html = render_to_string('gestion/ajax_materias_carrera.html', {
            'carrera':carrera,
            'materias':materias,
            'docente':docente,
        }, context_instance=RequestContext(request))
        return JsonResponse(html, safe=False)
    else:
        raise Http404

@login_required(login_url='/login')
def ajax_materias_asignadas_docente(request):
    gestion = get_object_or_404(Gestion, gestion = request.session['gestion'])
    if request.is_ajax():
        id = request.GET['docente_id']
        docente = get_object_or_404(Docente, pk = id)
        asignaciones = AsignacionDocente.objects.filter(gestion = gestion, docente = docente)
        html = render_to_string('gestion/ajax_materias_asignadas_docente.html', {
            'asignaciones':asignaciones,
        }, context_instance=RequestContext(request))
        return JsonResponse(html, safe=False)
    else:
        raise Http404


@permission_required('gestion.add_horario', login_url='/login')
def select_aula_horario(request):
    aulas = Aula.objects.all()
    return render(request, 'horario/select_aula_horario.html', {
        'aulas':aulas,
    })

@permission_required('gestion.add_horario', login_url='/login')
def aula_view_horario(request, aula_id):
    sms_sesion(request)
    aula = get_object_or_404(Aula, pk = aula_id)
    horas = ['18:00','19:00','20:00','21:00', '22:00']
    return render(request, 'horario/view_aula.html', {
        'aula':aula,
        'horas':horas,
    })

@login_required(login_url='/login')
def ajax_materia_horario(request):
    if request.is_ajax():
        aula_id = request.GET['aula']
        aula = get_object_or_404(Aula, pk = aula_id)
        dia = request.GET['dia']
        hora = request.GET['hora']
        gestion = get_object_or_404(Gestion, gestion = request.session['gestion'])
        asignar = AsignacionDocente.objects.filter(gestion = gestion)
        html = render_to_string('horario/ajax_materias_no_horarios.html', {
            'dia':dia,
            'hora':hora,
            'aula':aula,
            'asignados':asignar,
        }, context_instance=RequestContext(request))
        return JsonResponse(html, safe=False)
    else:
        raise Http404

@login_required(login_url='/login')
def ajax_search_matter(request):
    if request.is_ajax():
        carrera_id = request.GET['carrera_id']
        materia = request.GET['materia']
        gestion = get_object_or_404(Gestion, gestion = request.session['gestion'])
        docente_id = request.GET['docente_id']
        docente = Docente.objects.get(id = docente_id)
        carrera = Carrera.objects.get(id = carrera_id)
        matters = Materia.objects.filter(carrera = carrera, nombre__icontains = materia)
        html = render_to_string('gestion/result_matter_search.html', {
            'materias':matters,
            'docente':docente,
            'g':gestion,
        })
        return JsonResponse(html, safe=False)
    else:
        raise Http404

@permission_required('gestion.add_horario', login_url='/login')
def add_materia_horario(request, aula_id, asig_id):
    aula = get_object_or_404(Aula, pk = aula_id)
    gestion = get_object_or_404(Gestion, gestion = request.session['gestion'])
    asignacion = get_object_or_404(AsignacionDocente, pk = asig_id)
    hora = request.GET['hora']
    dia = request.GET['dia']
    if Horario.objects.filter(dia = dia, hora = hora, asignaciondocente = asignacion, gestion = gestion):
        sms = 'No se puede Asignar a este horario Ya fue Asignado en esta Hora'
    else:
        docente = Docente.objects.get(id = asignacion.docente_id)
        asignaciones = AsignacionDocente.objects.filter(docente = docente)
        horarios = Horario.objects.filter(asignaciondocente_id__in = asignaciones.values('id'))
        if horarios.filter(dia = dia, gestion = gestion, hora = hora):
            sms = "No se pude asignar horario <strong>DOCENTE OCUPADO</strong>"
        else:
            horas_docente = 0
            for h in horarios:
                horas_docente += 1
            if horas_docente < docente.carga_horario:
                h = Horario.objects.create(
                    dia = dia,
                    hora = hora,
                    aula = aula,
                    asignaciondocente = asignacion,
                    gestion = gestion,
                )
                log_addition(request, h, 'Horario Creado')
                sms = 'Horario Asignado Correctamente'
            else:
                sms = 'Carago Horaria de Docente Completa -- No se puede asignar'
    messages.info(request, sms)
    return HttpResponseRedirect(reverse(aula_view_horario, args={aula_id,}))

@permission_required('gestion.delete_horario', login_url='/login')
def remove_materia_horario(request, horario_id):
    horario = get_object_or_404(Horario, pk = horario_id)
    horario.delete()
    sms = "Horario Removido Correctamente"
    messages.info(request, sms)
    return HttpResponseRedirect(reverse(aula_view_horario, args={horario.aula.id}))

@permission_required('usuarios.report_docente', login_url='/login')
def materias_docente(request, docente_id):
    sms_sesion(request)
    gestion = get_object_or_404(Gestion, gestion = request.session['gestion'])
    docente = get_object_or_404(Docente, pk = docente_id)
    asignaciones = AsignacionDocente.objects.filter(docente = docente, gestion = gestion).order_by('materia__carrera')
    return render(request, 'gestion/docente_materias.html', {
        'docente':docente,
        'asignaciones':asignaciones,
    })

@permission_required('usuarios.report_docente', login_url='/login')
def pdf_materias_docente(request, docente_id):
    gestion = get_object_or_404(Gestion, gestion = request.session['gestion'])
    docente = get_object_or_404(Docente, pk = docente_id)
    asignaciones = AsignacionDocente.objects.filter(docente = docente, gestion = gestion).order_by('materia__carrera')
    html = render_to_string('gestion/pdf_docente_materias.html', {
        'docente':docente,
        'asignaciones':asignaciones,
        'gestion':gestion,
    })
    return generar_pdf(html)

@permission_required('usuarios.report_docente', login_url='/login')
def estudiantes_docente_materia(request, asig_id):
    sms_sesion(request)
    gestion = get_object_or_404(Gestion, gestion = request.session['gestion'])
    asignacion = get_object_or_404(AsignacionDocente, pk = asig_id)
    materia = Materia.objects.get(id = asignacion.materia_id)
    programados = Programacion.objects.filter(materia = materia, grupo_id = asignacion.grupo_id, gestion = gestion)
    inscripciones = Inscripcion.objects.filter(id__in = programados.values('inscripcion_id'))
    estudiantes = Estudiante.objects.filter(id__in = inscripciones.values('estudiante_id'))
    return render(request, 'gestion/estudiantes_materia.html', {
        'estudiantes':estudiantes,
        'asignacion':asignacion,
    })

@permission_required('usuarios.report_docente', login_url='/login')
def pdf_estudiantes_docente_materia(request, asig_id):
    gestion = get_object_or_404(Gestion, gestion = request.session['gestion'])
    asignacion = get_object_or_404(AsignacionDocente, pk = asig_id)
    materia = Materia.objects.get(id = asignacion.materia_id)
    programados = Programacion.objects.filter(materia = materia, grupo_id = asignacion.grupo_id, gestion = gestion)
    inscripciones = Inscripcion.objects.filter(id__in = programados.values('inscripcion_id'))
    estudiantes = Estudiante.objects.filter(id__in = inscripciones.values('estudiante_id'))
    html = render_to_string('gestion/pdf_estudiantes_materias.html', {
        'estudiantes':estudiantes,
        'asignacion':asignacion,
        'gestion':gestion,
    }, context_instance=RequestContext(request))
    return generar_pdf(html)

@permission_required('usuarios.report_docente', login_url='/login')
def horario_docente(request, doc_id):
    sms_sesion(request)
    gestion = get_object_or_404(Gestion, gestion = request.session['gestion'])
    docente = get_object_or_404(Docente, pk = doc_id)
    asignaciones = AsignacionDocente.objects.filter(docente = docente, gestion = gestion)
    horarios = Horario.objects.filter(asignaciondocente_id__in = asignaciones.values('id'))
    aulas = Aula.objects.filter(id__in = horarios.values('aula_id'))
    horas = ['18:00','19:00','20:00','21:00', '22:00']
    return render(request, 'gestion/horario_docente.html', {
        'horas':horas,
        'docente':docente,
        'horarios':horarios,
        'aulas':aulas,
    })

@login_required(login_url='/login')
def ajax_search_docente(request):
    if request.is_ajax():
        nombre = request.GET['nombres']
        paterno = request.GET['paterno']
        materno = request.GET['materno']
        aula_id = request.GET['aula_id']
        hora = request.GET['hora']
        dia = request.GET['dia']
        asignaciones = AsignacionDocente.objects.filter(
            docente__persona__nombre__icontains = nombre,
            docente__persona__paterno__icontains = paterno,
            docente__persona__materno__icontains = materno
        )
        #asignaciones = AsignacionDocente.objects.filter(
        #    Q(docente__persona__nombre__icontains = nombre) | Q(docente__persona__paterno__icontains = paterno) | Q(docente__persona__materno__icontains = materno)
        #)
        html = render_to_string('horario/ajax_docente_search.html', {
            'asignados':asignaciones,
            'hora':hora,
            'dia':dia,
            'aula_id':aula_id,
        }, context_instance=RequestContext(request))
        return JsonResponse(html, safe=False)
    else:
        raise Http404