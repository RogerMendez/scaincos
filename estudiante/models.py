#encoding: utf-8
from django.db import models

from inscripcion.models import Inscripcion
from carrera.models import Materia, Grupo
from gestion.models import Gestion
literal = [
    'Cero', 'Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve', 'Diez', 'Once', 'Doce', 'Trece', 'Catorce', 'Quince',
    'Dieciséis', 'Diecisiete', 'Dieciocho', 'Diecinueve', 'Veinte', 'Veinte y uno', 'Veinte y dos', 'Veinte y tres', 'Veinte y cuatro',
    'Veinte y cinco', 'Veinte y seis', 'Veinte y siete', 'Veinte y ocho', 'Veinte y nueve', 'Treinta', 'Treinta y uno', 'Treinta y dos', 'Treinta y tres',
    'Treinta y cuatro', 'Treinta y cinco', 'Treinta y seis', 'Treinta y siete', 'Treinta y ocho', 'Treinta y nueve', 'Cuarenta', 'Cuarenta y uno',
    'Cuarenta y dos', 'Cuarenta y tres', 'Cuarenta y cuatro', 'Cuarenta y cinco', 'Cuarenta y seis', 'Cuarenta y siete', 'Cuarenta y ocho', 'Cuarenta y nueve',
    'Cincuenta', 'Cincuenta y uno', 'Cincuenta y dos', 'Cincuenta y tres', 'Cincuenta y cuatro', 'Cincuenta y cinco', 'Cincuenta y seis', 'Cincuenta y siete',
    'Cincuenta y ocho', 'Cincuenta y nueve', 'Sesenta', 'Sesenta y uno', 'Sesenta y dos', 'Sesenta y tres', 'Sesenta y cuatro', 'Sesenta y cinco',
    'Sesenta y seis', 'Sesenta y siete', 'Sesenta y ocho', 'Sesenta y nueve', 'Setenta', 'Setenta y uno', 'Setenta y dos', 'Setenta y tres', 'Setenta y cuatro',
    'Setenta y cinco', 'Setenta y seis', 'Setenta y siete', 'Setenta y ocho', 'Setenta y nueve', 'Ochenta', 'Ochenta y uno', 'Ochenta y dos', 'Ochenta y tres',
    'Ochenta y cuatro', 'Ochenta y cinco', 'Ochenta y seis', 'Ochenta y siete', 'Ochenta y ocho', 'Ochenta y nueve', 'Noventa', 'Noventa y uno', 'Noventa y dos',
    'Noventa y tres', 'Noventa y cuatro', 'Noventa y cinco', 'Noventa y seis', 'Noventa y siete', 'Noventa y ocho', 'Noventa y nueve', 'Cien',
    ]
class Programacion(models.Model):
    fecha_registro = models.DateTimeField(auto_now_add=True)
    inscripcion = models.ForeignKey(Inscripcion)
    materia = models.ForeignKey(Materia)
    grupo = models.ForeignKey(Grupo)
    gestion = models.ForeignKey(Gestion)
    priner = models.PositiveIntegerField(verbose_name='Primer Trimestre', null=True, blank=True, default=0)
    segundo = models.PositiveIntegerField(verbose_name='Segundo Trimestre', null=True, blank=True, default=0)
    tercer = models.PositiveIntegerField(verbose_name='Tercer Trimestre', null=True, blank=True, default=0)
    segundo_T = models.PositiveIntegerField(verbose_name='Segundo Turno', null=True, blank=True, default=0)
    final = models.PositiveIntegerField(null=True, blank=True, default=0)
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
    def literal(self):
        if self.final:
            return literal[self.final]
        else:
            return literal[0]
    def __unicode__(self):
        return self.materia.nombre
    def __str__(self):
        return self.materia.nombre
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