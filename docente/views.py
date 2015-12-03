#encoding:utf-8
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.conf import settings

from django.contrib.auth.models import User

from scaincos.reportes import generar_pdf, sms_sesion
from scaincos.log_usuarios import log_addition, log_change

from gestion.models import Gestion, AsignacionDocente
from usuarios.models import Estudiante, Persona, Docente
from inscripcion.models import Inscripcion
from carrera.models import Materia, Carrera
from estudiante.models import Programacion, Notas
from docente.models import ExcelNotas
from docente.form import NotasForm, NotasExcelForm

import xlrd
import os

@login_required(login_url='/login')
def index_docente(request):
    persona = get_object_or_404(Persona, usuario = request.user)
    docente = Docente.objects.get(persona = persona)

    return render(request, 'moddocente/index.html', {
        'persona':persona,
        'docente':docente,
    })


@login_required(login_url='/login')
def mis_materias(request):
    sms_sesion(request)
    gestion = get_object_or_404(Gestion, gestion = request.session['gestion'])
    persona = Persona.objects.get(usuario = request.user)
    docente = Docente.objects.get(persona = persona)
    asignaciones = AsignacionDocente.objects.filter(docente = docente, gestion = gestion)
    return render(request, 'moddocente/mis_materias.html', {
        'asignaciones':asignaciones,
    })

@login_required(login_url='/login')
def estudiantes_materia(request, asig_id):
    sms_sesion(request)
    gestion = get_object_or_404(Gestion, gestion = request.session['gestion'])
    asignacion = get_object_or_404(AsignacionDocente, pk = asig_id)
    materia = Materia.objects.get(id = asignacion.materia_id)
    programados = Programacion.objects.filter(materia = materia, grupo_id = asignacion.grupo_id, gestion = gestion)
    inscripciones = Inscripcion.objects.filter(id__in = programados.values('inscripcion_id'))
    estudiantes = Estudiante.objects.filter(id__in = inscripciones.values('estudiante_id'))
    return render(request, 'moddocente/estudiantes_materia.html', {
        'estudiantes':estudiantes,
    })

@login_required(login_url='/login')
def materias_docente_notas(request):
    sms_sesion(request)
    gestion = get_object_or_404(Gestion, gestion = request.session['gestion'])
    persona = Persona.objects.get(usuario = request.user)
    docente = Docente.objects.get(persona = persona)
    asignaciones = AsignacionDocente.objects.filter(docente = docente, gestion = gestion)
    return render(request, 'moddocente/materias_docente_notas.html', {
        'asignaciones':asignaciones,
    })

@login_required(login_url='/login')
def estudiantes_materia_notas(request, asig_id):
    gestion = get_object_or_404(Gestion, gestion = request.session['gestion'])
    asignacion = get_object_or_404(AsignacionDocente, pk = asig_id)
    materia = Materia.objects.get(id = asignacion.materia_id)
    programados = Programacion.objects.filter(materia = materia, grupo_id = asignacion.grupo_id, gestion = gestion)
    inscripciones = Inscripcion.objects.filter(id__in = programados.values('inscripcion_id'))
    estudiantes = Estudiante.objects.filter(id__in = inscripciones.values('estudiante_id'))
    if request.method == "POST":
        formulario = NotasExcelForm(request.POST, request.FILES)
        if formulario.is_valid():
            e = ExcelNotas.objects.create(
                excel = request.FILES['input_excel']
            )
            #location_file = "http://127.0.0.1:8000/media/" + str(e.excel)#
            location_file = os.path.join(settings.DIR_FIS, 'media')
            location_file = os.path.join(location_file, 'notas')
            location_file = os.path.join(location_file, str(e.excel)[6:500])
            print location_file
            workbook = xlrd.open_workbook(location_file)
            sheet = workbook.sheet_by_index(0)
            #print sheet.cell_value(7,3)
            columnas = sheet.ncols
            filas = sheet.nrows
            #print sheet.cell_value(7,3)
            n_programo = 0
            programo = 0
            for f in range(7, filas):
                ci = int(sheet.cell_value(f, 3))
                if estudiantes.filter(persona__ci = ci):
                    estudiante = estudiantes.get(persona__ci = ci)
                    inscripcion = inscripciones.get(estudiante = estudiante)
                    programacion = programados.get(inscripcion = inscripcion)
                    primer = sheet.cell_value(f,4)
                    segunto = sheet.cell_value(f, 5)
                    tercer = sheet.cell_value(f, 6)
                    final = sheet.cell_value(f, 7)
                    programacion.priner = primer
                    programacion.segundo = segunto
                    programacion.tercer = tercer
                    programacion.final = final
                    programacion.save()
                    programo = programo + 1
                else:
                    n_programo = n_programo + 1
            sms = "No Se Registraron %s notas"%(str(n_programo))
            messages.success(request, sms)
            sms = "Se Registraron %s notas Correctamente"% (str(programo))
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(estudiantes_materia_notas, args={asig_id, }))
    else:
        formulario = NotasExcelForm()
    return render(request, 'moddocente/estudiantes_materia_notas.html', {
        'materia':materia,
        'estudiantes':estudiantes,
        'programaciones':programados,
        'asignacion':asignacion,
        'formulario':formulario,
    })

@login_required(login_url='/login')
def subir_notas_pro(request, pro_id, asig_id):
    progra = get_object_or_404(Programacion, pk = pro_id)
    if request.method == 'POST':
        formulario = NotasForm(request.POST, instance=progra)
        if formulario.is_valid():
            n = formulario.save()
            n.final = (n.priner + n.segundo + n.tercer)/3
            if n.segundo_T > 50:
                n.final = n.segundo_T
            n.save()
            log_change(request, n, 'Nota Subida')
            sms = 'Nota Agregada Correctamente'
            messages.info(request, sms)
            return HttpResponseRedirect(reverse(estudiantes_materia_notas, args={asig_id,}))
    else:
        formulario = NotasForm(instance=progra)
    return render(request, 'moddocente/subir_notas.html', {
        'progra':progra,
        'formulario':formulario,
    })