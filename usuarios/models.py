#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from datetime import datetime

def validate_fecha_nac(value):
    hoy = datetime.today()
    today = hoy
    year = today.year
    edad = year - value.year
    if edad <= 15:
        raise ValidationError(u'Debe tener por lo menos 15 años para preinscribirse')


class Persona(models.Model):
    ci = models.CharField(max_length=10, unique=True, verbose_name='Cedula de Identidad')
    nombre = models.CharField(max_length=20, verbose_name='Nombres')
    paterno = models.CharField(max_length=20, verbose_name='Apellido Paterno')
    materno = models.CharField(max_length=20, verbose_name='Apellido Materno')
    fecha_nac = models.DateField(verbose_name='Fecha de Nacimiento', validators=[validate_fecha_nac])
    direccion = models.CharField(max_length=100, verbose_name='Dirección')
    telefono = models.CharField(max_length=10, verbose_name='Telefono/Celular')
    avatar = models.ImageField(upload_to='avatar', verbose_name='Seleccione Una Imagen')
    activo = models.BooleanField(default=True)
    tipo = models.CharField(max_length=20, default='Estudiante')
    email = models.EmailField(verbose_name='Correo Electronico')
    usuario = models.OneToOneField(User, null=True, blank=True)
    def __unicode__(self):
        return str(self.ci)
    def __str__(self):
        return str(self.ci)
    class Meta:
        ordering = ['ci']
        verbose_name_plural = 'Personas'

class Administrativo(models.Model):
    nro_item = models.IntegerField(verbose_name='Numero de Item')
    cargo = models.CharField(max_length=50, verbose_name='Cargo Ocupado')
    persona = models.OneToOneField(Persona, null=True, blank=True)
    def __unicode__(self):
        return str(self.persona.ci)
    def __str__(self):
            return str(self.persona.ci)
    class Meta:
        ordering = ['nro_item']
        verbose_name_plural = 'Administrativos'
        permissions = (
            ('index_administrativo', 'Index Administrativos'),
            ('detail_administrativo', 'Detalle Administrativos'),
            ('report_administrativo', 'Reporte Administrativos'),
        )

class Estudiante(models.Model):
    nro_estudiante = models.IntegerField(unique=True, verbose_name='Codigo Estudiante')
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_salida = models.DateTimeField(null=True, blank=True)
    terminado = models.BooleanField(default=False)
    persona = models.OneToOneField(Persona, null=True, blank=True)
    def __unicode__(self):
        return str(self.persona)
    def __str__(self):
        return str(self.persona)
    class Meta:
        ordering = ['nro_estudiante']
        verbose_name_plural = 'Estudiantes'
        permissions = (
            ('index_estudiante', 'Index Estudiante'),
            ('detail_estudiante', 'Detalle Estudiante'),
            ('report_estudiante', 'Reporte Estudiante'),
        )

class Docente(models.Model):
    nro_docente = models.IntegerField(unique=True, verbose_name='Item Docente')
    fecha_ingreso = models.DateField(verbose_name='Fecha de Ingreso')
    carga_horario = models.PositiveIntegerField(verbose_name='Carga Horaria Semanal', default=1, help_text='En Horas')
    persona = models.OneToOneField(Persona, null=True, blank=True)
    def __unicode__(self):
        return str(self.persona)
    def __str__(self):
        return str(self.persona)
    class Meta:
        ordering = ['nro_docente']
        verbose_name_plural = 'Docentes'
        permissions = (
            ('index_docente', 'Index Docente'),
            ('detail_docente', 'Detalle Docente'),
            ('report_docente', 'Reporte Docente'),
        )