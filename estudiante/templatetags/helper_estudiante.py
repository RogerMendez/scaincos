from django import template

register = template.Library()

from usuarios.models import Estudiante
from carrera.models import Carrera
from gestion.models import Gestion
from inscripcion.models import Inscripcion, Matricula
from estudiante.models import Programacion
from carrera.models import Materia

@register.filter(name='materiaprogramada')
def materiaprogramada(materia_id, gestion):
    g = Gestion.objects.get(gestion = gestion)
    mate = Materia.objects.get(pk = materia_id)
    pro = Programacion.objects.filter(materia = mate, gestion = g)
    return pro


@register.filter(name='materiaprogramadaestu')
def materiaprogramadaest(programacion, ins_id):
    insc = Inscripcion.objects.get(id = ins_id)
    if programacion.filter(inscripcion = insc):
        return programacion.filter(inscripcion = insc)
    return False

@register.filter(name='programacion_gestion')
def programacion_gestion(inscripcion_id, gestion_id):
    inscripcion = Inscripcion.objects.get(pk = inscripcion_id)
    gestion = Gestion.objects.get(pk = gestion_id)
    programaciones = Programacion.objects.filter(inscripcion = inscripcion, gestion = gestion)
    return programaciones

@register.filter(name='programacion_gestion_count')
def programacion_gestion_count(inscripcion_id, gestion_id):
    inscripcion = Inscripcion.objects.get(pk = inscripcion_id)
    gestion = Gestion.objects.get(pk = gestion_id)
    programaciones = Programacion.objects.filter(inscripcion = inscripcion, gestion = gestion, final__lte = 50)
    return programaciones.count()
