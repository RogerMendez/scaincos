from django.shortcuts import get_object_or_404

from django import template

register = template.Library()

from institucion.models import Aula
from carrera.models import Grupo, Materia
from gestion.models import Horario, Gestion, AsignacionDocente
from usuarios.models import Docente

@register.filter(name='verificar_horario')
def verificar_horario(hora, dia):
    if Horario.objects.filter(hora = hora, dia = dia):
        hora = Horario.objects.filter(hora = hora, dia = dia)
        return hora
    else:
        return False

@register.filter(name='verificar_aula')
def verificar_aula(horario, aula):
    if horario == False:
        return False
    else:
        aula = Aula.objects.get(id = aula)
        if horario.filter(aula = aula):
            horas = horario.filter(aula = aula)
            return horas
        else:
            return False

@register.filter(name='verificar_gestion')
def verificar_gestion(horario, gestion):
    if horario == False:
        return False
    else:
        gestion = Gestion.objects.get(gestion = gestion)
        if horario.filter(gestion = gestion):
            hora = horario.filter(gestion = gestion)
            return hora#hora.asignaciondocente.materia.sigla + '/' + hora.asignaciondocente.grupo.abreviacion
        else:
            return False




@register.filter(name='asignacion_docente')
def asignacion_docente(doc_id, gestion):
    gestion = Gestion.objects.get(gestion = gestion)
    docente = get_object_or_404(Docente, pk = doc_id)
    asignacion_docente = AsignacionDocente.objects.filter(docente = docente, gestion = gestion)
    return asignacion_docente

@register.filter(name='asignacion_horarios_aula')
def asignacion_horarios_aula(asignaciones, aula_id):
    if not asignaciones:
        return False
    else:
        aula = get_object_or_404(Aula, pk = aula_id)
        horarios = Horario.objects.filter(aula = aula, asignaciondocente_id__in = asignaciones.values('id'))
        return horarios

@register.filter(name='horarios_dia')
def horarios_dia(horarios, dia):
    if not horarios:
        return False
    else:
        h = horarios.filter(dia = dia)
        return h

@register.filter(name='horario_hora')
def horario_hora(horarios, hora):
    if not horarios:
        return False
    else:
        h = horarios.filter(hora = hora)
        return h


@register.filter(name='matter_verify')
def matter_verify(materia_id, gestion):
    materia = get_object_or_404(Materia, pk = materia_id)
    gestion = Gestion.objects.get(gestion = gestion)
    asignados = AsignacionDocente.objects.filter(materia = materia, gestion = gestion)
    return asignados

@register.filter(name='asign_verify_grupo')
def asign_verify_grupo(asignaciones, grupo_id):
    grupo = get_object_or_404(Grupo, pk = grupo_id)
    if asignaciones.filter(grupo = grupo):
        return True
    else:
        return False


@register.simple_tag
def grupo_docente_materia(year, docente_id, **kwargs):
    gestion = Gestion.objects.get(gestion = year)
    docente = Docente.objects.get(pk = docente_id)
    materia_id = kwargs['materia_id']
    materia = Materia.objects.get(pk = materia_id)
    asignacion = AsignacionDocente.objects.filter(gestion = gestion, docente = docente, materia = materia)
    grupos = ""
    for a in asignacion:
        grupos += " - "
        grupos += a.grupo.grupo
    return grupos

@register.simple_tag
def horas_docente_materia(year, docente_id, **kwargs):
    gestion = Gestion.objects.get(gestion = year)
    docente = Docente.objects.get(pk = docente_id)
    materia_id = kwargs['materia_id']
    materia = Materia.objects.get(pk = materia_id)
    asignacion = AsignacionDocente.objects.filter(gestion = gestion, docente = docente, materia = materia)
    horarios = Horario.objects.filter(asignaciondocente_id__in = asignacion.values('id'))
    horas = 0
    for h in horarios:
        horas += 1
    return horas

@register.simple_tag
def horas_docente_total(year, docente_id):
    gestion = Gestion.objects.get(gestion = year)
    docente = Docente.objects.get(pk = docente_id)
    asignacion = AsignacionDocente.objects.filter(gestion = gestion, docente = docente)
    horarios = Horario.objects.filter(asignaciondocente_id__in = asignacion.values('id'))
    horas = 0
    for h in horarios:
        horas += 1
    return horas