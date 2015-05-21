#encoding: utf-8
from django.db import models
from django.contrib.auth.models import User

from usuarios.models import Docente
from institucion.models import Aula
from carrera.models import Carrera, Materia, Grupo
from datetime import datetime

hoy = datetime.now()
anho = hoy.strftime("%Y")
a_ini = int(anho) - 10
a_fin = int(anho) + 1
anhos = ()
for a in range(a_ini, a_fin):
    anhos += ((a, a),)

class Gestion(models.Model):
    gestion = models.IntegerField(max_length='4', verbose_name='Gestion Academina', choices=anhos, unique=True)
    usuario = models.ForeignKey(User, null=True, blank=True)
    def __unicode__(self):
        return str(self.gestion)
    def __str__(self):
        return str(self.gestion)
    class Meta:
        ordering = ['gestion']
        verbose_name_plural = 'Gestion'
        permissions = (

        )

class Gestion_Carrera(models.Model):
    gestion = models.ForeignKey(Gestion)
    carrera = models.ForeignKey(Carrera)
    c_inscripcion = models.FloatField(verbose_name='Costo de Inscripcion')
    c_matricula = models.FloatField(verbose_name='Consto Matricula')
    def __unicode__(self):
        return self.carrera.nombre
    def __str__(self):
        return self.carrera.nombre
    class Meta:
        ordering = ['gestion']
        verbose_name_plural = 'Carreras - Gestion'

class AsignacionDocente(models.Model):
    fecha_asignacion = models.DateField(auto_now_add=True)
    gestion = models.ForeignKey(Gestion)
    docente = models.ForeignKey(Docente)
    materia = models.ForeignKey(Materia)
    grupo = models.ForeignKey(Grupo, null=True)
    def __unicode__(self):
        return str(self.docente.persona.ci)
    def __str__(self):
        return str(self.docente.persona.ci)
    class Meta:
        ordering = ['docente']
        verbose_name_plural = 'Asignacion Docente'

class Horario(models.Model):
    dia = models.CharField(max_length='10')
    hora = models.TimeField(default="00:00:00")
    asignaciondocente = models.ForeignKey(AsignacionDocente)
    aula = models.ForeignKey(Aula)
    gestion = models.ForeignKey(Gestion)
    def __unicode__(self):
        return self.aula.nro
    def __str__(self):
        return self.aula.nro
    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
        ordering = ['dia']
        permissions = (
            ('index_horario', 'Index de Horario'),
        )