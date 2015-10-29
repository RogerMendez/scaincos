from django.shortcuts import get_object_or_404

from django import template

register = template.Library()

from usuarios.models import Estudiante
from carrera.models import Materia, Carrera
from estudiante.models import Programacion
from inscripcion.models import Inscripcion
from gestion.models import Gestion

@register.filter(name='inscripcion_notas')
def inscripcion_notas(estudiante, materia):
    estudiante = get_object_or_404(Estudiante, pk = estudiante)
    materia = get_object_or_404(Materia, pk = materia)
    carrera = get_object_or_404(Carrera, pk = materia.carrera_id)
    inscripcion = Inscripcion.objects.get(estudiante = estudiante, carrera = carrera, estado = True)
    return inscripcion

@register.filter(name='programaciones_gestion')
def programaciones_gestion(inscripcion, gestion):
    gestion = get_object_or_404(Gestion, pk = gestion)
    programacion = Programacion.objects.filter(inscripcion = inscripcion, gestion = gestion)
    return programacion


@register.filter(name='notas_final')
def notas_final(programacion, materia):
    if programacion:
        materia = get_object_or_404(Materia, pk = materia)
        programacion = programacion.filter(materia = materia)
        return programacion
    else:
        return False