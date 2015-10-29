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

from scaincos.reportes import generar_pdf
from scaincos.log_usuarios import log_addition, log_change

from carrera.models import Carrera, Materia, Requisitos, Grupo
from carrera.form import CarreraForm, MateriaForm, CarrerasForm
from gestion.form import GrupoForm

@permission_required('carrera.index_carrera', login_url='/login')
def index_carrera(request):
    carreras = Carrera.objects.all()
    return render(request, 'carreras/index.html', {
        'carreras':carreras,
    })

@permission_required('carrera.add_carrera', login_url='/login')
def new_carrera(request):
    if request.method == 'POST':
        formulario = CarreraForm(request.POST)
        if formulario.is_valid():
            c = formulario.save()
            log_addition(request, c, 'Carrera Creada Correctamete')
            sms = ' Carrera <strong>%s</strong> Creada Correctamente'% (c.nombre)
            messages.info(request, sms)
            return HttpResponseRedirect(reverse(index_carrera))
    else:
        formulario = CarreraForm()
    return render(request, 'carreras/new.html', {
        'formulario':formulario,
    })

@permission_required('carrera.change_carrera', login_url='/login')
def change_carrera(request):
    carreras = Carrera.objects.all()
    return render(request, 'carreras/change.html', {
        'carreras':carreras,
    })

@permission_required('carrera.change_carrera', login_url='/logn')
def update_carrera(request, carrera_id):
    carrera = get_object_or_404(Carrera, pk = carrera_id)
    if request.method == 'POST':
        formulario = CarreraForm(request.POST, instance=carrera)
        if formulario.is_valid():
            c = formulario.save()
            log_change(request, c, 'Carrera Modificada')
            sms = 'Carrera <strong>%s</strong> Modificada Correctamente'% (c.nombre)
            messages.info(request, sms)
            return HttpResponseRedirect(reverse(change_carrera))
    else:
        formulario = CarreraForm(instance=carrera)
    return render(request, 'carreras/update.html', {
        'formulario':formulario,
    })

@permission_required('carrera.detail_carrera', login_url='/login')
def list_detail_carrera(request):
    carreras = Carrera.objects.all()
    return render(request, 'carreras/list_detail.html',{
        'carreras':carreras,
    })

@permission_required('carreras.detail_carrera', '/login')
def detail_carrera(request, carrera_id):
    carrera = get_object_or_404(Carrera, pk = carrera_id)
    return render(request, 'carreras/detail.html', {
        'carrera':carrera,
    })

@permission_required('carrera.report_carrera', login_url='/login')
def list_carrera_plan(request):
    carreras = Carrera.objects.all()
    return render(request, 'carreras/list_plan.html', {
        'carreras':carreras,
    })

@login_required(login_url='/login')
def pdf_plan_curricular(request, carrera_id):
    carrera = get_object_or_404(Carrera, pk = carrera_id)
    materias = Materia.objects.filter(carrera = carrera)
    html = render_to_string('carreras/pdf_plan curricular.html', {
        'carrera':carrera,
        'materias':materias,
    }, context_instance=RequestContext(request))
    return generar_pdf(html)

@permission_required('carrera.index_materia', login_url='/login')
def index_materia(request):
    carrera = Carrera.objects.first()
    formulario = CarrerasForm(request.GET or None)
    if formulario.is_valid():
        id = request.GET['carrera']
        carrera = Carrera.objects.get(id = int(id))
    return render(request, 'materias/index.html', {
        'carrera':carrera,
        'formulario':formulario,
    })

@permission_required('carrera.add_materia', login_url='/login')
def new_materia(request):
    if request.method == 'POST':
        formulario = MateriaForm(request.POST)
        if formulario.is_valid():
            m = formulario.save()
            log_addition(request, m, 'Materia Creada')
            sms = 'Materia <strong>%s</strong> Creada Correctamente'% (m.nombre)
            messages.info(request, sms)
            return HttpResponseRedirect(reverse(index_materia))
    else:
        formulario = MateriaForm()
    return render(request, 'materias/new.html', {
        'formulario':formulario,
    })

@permission_required('carrera.change_carrera')
def list_materias_update(request):
    carrera = Carrera.objects.first()
    formulario = CarrerasForm(request.GET or None)
    if formulario.is_valid():
        id = request.GET['carrera']
        carrera = Carrera.objects.get(id = int(id))
    return render(request, 'materias/list_update.html', {
        'carrera':carrera,
        'formulario':formulario,
    })

@permission_required('carrera.change_carrera')
def update_materia(request, materia_id):
    materia = get_object_or_404(Materia, pk = materia_id)
    if request.method == 'POST':
        formulario = MateriaForm(request.POST, instance=materia)
        if formulario.is_valid():
            m = formulario.save()
            log_change(request, m, 'Materia Modificada')
            sms = 'Materia <strong>%s</strong> modificada correctamente'%(m.nombre)
            messages.info(request, sms)
            return HttpResponseRedirect(reverse(index_materia))
    else:
        formulario = MateriaForm(instance=materia)
    return render(request, 'materias/update.html', {
        'formulario':formulario,
    })

@permission_required('carrera,requirement_materia', login_url='/login')
def list_materias_requisitos(request):
    carrera = Carrera.objects.first()
    formulario = CarrerasForm(request.GET or None)
    if formulario.is_valid():
        id = request.GET['carrera']
        carrera = Carrera.objects.get(id = int(id))
    return render(request, 'materias/list_materias_add_requisitos.html', {
        'carrera':carrera,
        'formulario':formulario,
    })

@permission_required('carrera,requirement_materia', login_url='/login')
def requisitos_materia(request, materia_id):
    materia = get_object_or_404(Materia, pk = materia_id)
    carrera = get_object_or_404(Carrera, pk = materia.carrera_id)
    asignados = Requisitos.objects.filter(from_materia = materia.id)
    q1 = asignados.values('to_materia_id')
    s_asignar = Materia.objects.exclude(nivel = materia.nivel).filter(nivel__lt = materia.nivel).exclude(id__in = q1).filter(carrera = carrera)
    return render(request, 'materias/requisitos_materia.html', {
        'materia':materia,
        'carrera':carrera,
        'asignados':asignados,
        's_asignar':s_asignar,
    })

@permission_required('carrera,requirement_materia', login_url='/login')
def add_requisito(request, materia_id, requisito_id):
    materia = get_object_or_404(Materia, pk = materia_id)
    requisito = get_object_or_404(Materia, pk = requisito_id)
    q1 = Requisitos.objects.create(
        from_materia = materia,
        to_materia = requisito,
    )
    sms = 'Requisito agregado Correctamente'
    messages.info(request, sms)
    return HttpResponseRedirect(reverse(requisitos_materia, args={materia_id, }))

@permission_required('carrera,requirement_materia', login_url='/login')
def remove_requisito(request, requisito_id):
    requisito = get_object_or_404(Requisitos, pk = requisito_id)
    requisito.delete()
    sms = 'Requisito Quitado Correctamente'
    messages.info(request, sms)
    return HttpResponseRedirect(reverse(requisitos_materia, args={requisito.from_materia_id}))


@permission_required('carrera.index_grupo', login_url='/login')
def index_grupos(request):
    grupos = Grupo.objects.all()
    return render(request, 'grupos/index.html', {
        'grupos':grupos,
    })

@permission_required('carrera.add_grupo', login_url='/login')
def new_grupo(request):
    if request.method == 'POST':
        formulario = GrupoForm(request.POST)
        if formulario.is_valid():
            g = formulario.save()
            log_addition(request, g, 'Grupo Creado Correctamente')
            sms = 'Grupo Creado correctamente'
            messages.info(request, sms)
            return HttpResponseRedirect(reverse(index_grupos))
    else:
        formulario = GrupoForm()
    return render(request, 'grupos/new.html', {
        'formulario':formulario,
    })

@permission_required('carrera.report_carrera', login_url='/login')
def pdf_carreras(request):
    carreras = Carrera.objects.all()
    html = render_to_string('carreras/pdf_carreras.html', {
        'carreras':carreras,
    }, context_instance=RequestContext(request))
    return generar_pdf(html)