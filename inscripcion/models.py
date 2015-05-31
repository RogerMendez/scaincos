from django.db import models
from django.contrib.auth.models import User

from carrera.models import Carrera
from usuarios.models import Estudiante
from gestion.models import Gestion

class Inscripcion(models.Model):
    c_inscripcion = models.FloatField(verbose_name='Costo Inscripcion')
    fecha_registro = models.DateField(auto_now_add=True)
    estudiante = models.ForeignKey(Estudiante)
    carrera = models.ForeignKey(Carrera)
    gestion = models.ForeignKey(Gestion)
    usuario = models.ForeignKey(User, null=True)
    estado = models.BooleanField(default=True)
    def __unicode__(self):
        return str(self.estudiante.persona.ci)
    def __str__(self):
        return str(self.estudiante.persona.ci)
    class Meta:
        ordering = ['carrera']
        verbose_name_plural = 'Inscripciones'
        permissions = (
            ('index_inscripcion', 'Index Inscripciones'),
        )

class Matricula(models.Model):
    costo = models.FloatField(verbose_name='Consto Matricula')
    fecha_registro = models.DateField(auto_now_add=True)
    inscripcion = models.ForeignKey(Inscripcion)
    gestion = models.ForeignKey(Gestion)
    usuario = models.ForeignKey(User)
    def __unicode__(self):
        return str(self.gestion)
    class Meta:
        ordering = ['inscripcion']
        verbose_name_plural = 'Matriculas'
        permissions = (
            ('index_matricula', 'Index Matriculas'),
        )