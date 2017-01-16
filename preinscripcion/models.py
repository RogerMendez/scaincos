#encoding:utf-8
from django.core.exceptions import ValidationError
from django.db import models

from gestion.models import Gestion
from carrera.models import Carrera
from datetime import date, datetime


def validate_fecha_nac(value):
    hoy = datetime.today()
    today = hoy
    if today.month < value.month or \
      (today.month == value.month and today.day < value.day):
        return today.year - value.year - 1
    else:
        edad = today.year - value.year
    if edad <= 15:
        raise ValidationError(u'Debe tener por lo menos 15 años para preinscribirse %s' %(edad))


class Preinscripcion(models.Model):
    ci = models.IntegerField(verbose_name='Cedula de Identidad', help_text='7 u 8 Numeros')
    nombre = models.CharField(max_length=20, verbose_name='Nombres')
    paterno = models.CharField(max_length=20, verbose_name='Apellido Paterno')
    materno = models.CharField(max_length=20, verbose_name='Apellido Materno')
    fecha_nac = models.DateField(verbose_name='Fecha de Nacimiento', validators=[validate_fecha_nac])
    direccion = models.CharField(max_length=100, verbose_name=u'Dirección')
    telefono = models.CharField(max_length=10, verbose_name='Telefono/Celular')
    gestion = models.ForeignKey(Gestion, null=True)
    carrera = models.ForeignKey(Carrera)
    avatar = models.ImageField(upload_to='avatar', verbose_name='Seleccione Una Imagen', default='1')
    estado = models.BooleanField(default=True)
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Preinscripcion'
        verbose_name_plural = 'Preinscripciones'
        ordering = ['ci']
        permissions = (
            ('index_preincripcion', 'Listado Preinscripciones'),
            ('report_preinscripcion', 'Reporte Preinscripciones'),
            ('create_inscripcion', 'Realizar Inscripcion Preinscripcion'),
        )