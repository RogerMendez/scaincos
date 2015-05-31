from django.db import models

from inscripcion.models import Inscripcion
from carrera.models import Materia, Grupo
from gestion.models import Gestion

class Programacion(models.Model):
    fecha_registro = models.DateTimeField(auto_now_add=True)
    inscripcion = models.ForeignKey(Inscripcion)
    materia = models.ForeignKey(Materia)
    grupo = models.ForeignKey(Grupo)
    gestion = models.ForeignKey(Gestion)
    priner = models.PositiveIntegerField(verbose_name='Primer Trimestre', null=True, blank=True)
    segundo = models.PositiveIntegerField(verbose_name='Segundo Trimestre', null=True, blank=True)
    tercer = models.PositiveIntegerField(verbose_name='Tercer Trimestre', null=True, blank=True)
    segundo_T = models.PositiveIntegerField(verbose_name='Segundo Turno', null=True, blank=True)
    final = models.PositiveIntegerField(null=True, blank=True)
    def promedio(self):
        if self.priner == None or self.segundo == None or self.tercer == None:
            return 0
        return (self.priner + self.segundo + self.tercer)/3
    def final1(self):
        if self.promedio()>50:
            return self.promedio()
        else:
            if self.segundo_T > 50:
                return self.segundo_T
            else:
                return self.promedio()
    def __unicode__(self):
        return self.inscripcion.estudiante.persona.nombre
    def __str__(self):
        return self.inscripcion.estudiante.persona.nombre
    class Meta:
        verbose_name_plural = 'Programaciones'
        verbose_name = 'Programacion'
        ordering = ['inscripcion']

class Notas(models.Model):
    tipo = models.CharField(max_length=50)
    programacion = models.ForeignKey(Programacion)
    def aprobado(self):
        return False
    def __unicode__(self):
        return self.programacion
    def __str__(self):
        return self.programacion
    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'
        ordering = ['programacion']