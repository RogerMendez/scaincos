from django import template

register = template.Library()

from institucion.models import Aula
from gestion.models import Horario, Gestion

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