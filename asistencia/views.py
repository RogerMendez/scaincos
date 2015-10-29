#encoding:utf-8
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, HttpResponse, Http404, JsonResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404

from scaincos.reportes import generar_pdf, sms_sesion
from scaincos.log_usuarios import log_addition, log_change
import datetime

from usuarios.models import Persona, Docente
from asistencia.models import Asistencia
from gestion.models import Gestion, Horario, AsignacionDocente
from asistencia.form import DatForm, FechaForm

@permission_required('asistencia.detail_fecha_asistencia', login_url='/login')
def index(request):
    fecha = datetime.datetime.now()
    formulario = FechaForm(request.GET or None)
    if formulario.is_valid():
        fecha = request.GET['fecha']
        fecha = datetime.date(int(fecha[0:4]), int(fecha[5:7]), int(fecha[8:10]))
    asistencias = Asistencia.objects.filter(fecha = fecha)
    return render(request, 'asistencia/index.html', {
        'asistencias':asistencias,
        'fecha':fecha,
        'formulario':formulario,
    })

@permission_required('asistencia.add_asistencia', login_url='/login')
def new_asistencia(request):
    sms_sesion(request)
    if request.method == 'POST':
        formulario = DatForm(request.POST, request.FILES)
        if formulario.is_valid():
            file1 = request.FILES['archivo']
            for c in file1:
                fila = c.split()
                codigo = fila[0]
                if Docente.objects.filter(nro_docente = codigo):
                    doc = Docente.objects.get(nro_docente = codigo)
                    fecha = fila[1]
                    hora = fila[2]
                    hora = hora[0:5]+':00'
                    if not Asistencia.objects.filter(persona_id = doc.persona_id, hora = hora, fecha = fecha):
                        a = Asistencia.objects.create(
                            fecha = fecha,
                            hora = hora[0:5],
                            persona_id = doc.persona_id,
                        )
            sms = "Datos Importados Correctamente"
            messages.info(request, sms)
            return HttpResponseRedirect(reverse(index))
    else:
        formulario = DatForm()
    return render(request, 'asistencia/subir_archivo.html', {
        'formulario':formulario
    })

@permission_required('asistencia.report_asistencia', login_url='/login')
def asistencia_list_docente(request):
    docentes = Docente.objects.all()

    return render(request, 'asistencia/list_docente_asistencia.html', {
        'docentes':docentes,
    })

@permission_required('asistencia.report_asistencia', login_url='/login')
def asistencia_docente(request, docente_id):
    sms_sesion(request)
    docente = get_object_or_404(Docente, pk = docente_id)
    return render(request, 'asistencia/asistencia_docente.html', {
        'docente':docente,
    })

def ajax_horario_docente(request):
    if request.is_ajax():
        gestion = Gestion.objects.get(gestion = request.session['gestion'])
        docente_id = request.GET['docente']
        dia = request.GET['dia']
        if dia == 'Lunes':
            num_dia = 2
        elif dia == 'Martes':
            num_dia = 3
        elif dia == 'Miercoles':
            num_dia = 4
        elif dia == 'Jueves':
            num_dia = 5
        elif dia == 'Viernes':
            num_dia = 6
        elif dia == 'Sabado':
            num_dia = 7
        else:
            num_dia = 1
        docente = get_object_or_404(Docente, pk = docente_id)
        persona = Persona.objects.get(id = docente.persona_id)
        asistencias = Asistencia.objects.filter(persona = persona, fecha__year = gestion.gestion, fecha__week_day = num_dia).order_by('fecha', 'hora')
        asignaciones = AsignacionDocente.objects.filter(docente = docente, gestion = gestion)
        horarios = Horario.objects.filter(dia = dia, gestion = gestion, asignaciondocente_id__in = asignaciones.values('id'))
        html = render_to_string('asistencia/ajax_asistencia_docente.html', {
            'dia':dia,
            'asistencias':asistencias,
            'horarios':horarios,
        }, context_instance=RequestContext(request))
        return JsonResponse(html, safe=False)
    else:
        raise Http404