from django import template

register = template.Library()

from usuarios.models import Estudiante
from carrera.models import Carrera
from gestion.models import Gestion
from inscripcion.models import Inscripcion, Matricula

@register.filter(name='estudiantes')
def estudiantes(carrera_id):
    insc = Inscripcion.objects.filter(carrera_id = carrera_id)
    estu = Estudiante.objects.exclude(id__in = insc.values('estudiante_id'))
    return estu


@register.filter(name='estu_sin_matricula')
def estudiantes_no_matricula(carrera_id, gestion):
    g = Gestion.objects.get(gestion = gestion)
    carrera = Carrera.objects.get(id = carrera_id)
    insc = Inscripcion.objects.filter(carrera = carrera)
    estudiantes = Estudiante.objects.filter(id__in = insc.values('estudiante_id'))
    matriculas = Matricula.objects.filter(inscripcion_id__in = insc.values('id'), gestion = g)
    insc = insc.filter(id__in = matriculas.values('inscripcion_id'))
    estudiantes = estudiantes.exclude(id__in = insc.values('estudiante_id'))
    return estudiantes
