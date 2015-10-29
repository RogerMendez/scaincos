# -*- encoding: utf-8 -*-
from django.db import models

class Grupo(models.Model):
    grupo = models.CharField(max_length='10', unique=True)
    abreviacion = models.CharField(max_length='3', unique=True)
    def __unicode__(self):
        return self.grupo
    def __str__(self):
        return self.grupo
    class Meta:
        ordering = ['abreviacion']
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
        permissions = (
            ('index_grupo', 'Index Grupo'),
        )

class Carrera(models.Model):
    choicestiempo = (
        ('1', '1 Año'),
        ('2', '2 Años'),
        ('3', '3 Años'),
        ('4', '4 Años'),
        ('5', '5 Años'),
    )
    nombre = models.CharField(max_length='50', verbose_name='Nombre de Carrera', unique=True)
    tiempo = models.CharField(max_length='2', verbose_name='Tiempo de Carrera', choices=choicestiempo)
    area = models.CharField(max_length='50', default='Comercial')
    nivel = models.CharField(max_length='50', default='Superior')
    fecha_creacion = models.DateField(verbose_name='Creacion de Carrera')
    resenha = models.TextField(verbose_name='Breve Reseña')
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre
    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Carreras'
        permissions = (
            ('index_carrera', 'Index Carreras'),
            ('detail_carrera', 'Detalle Carrera'),
            ('report_carrera', 'Reporte Carrera'),
        )

class Materia(models.Model):
    nombre = models.CharField(max_length='50', verbose_name='Nombre Materia')
    sigla = models.CharField(max_length='10', verbose_name='Sigla Materia')
    nivel = models.IntegerField(verbose_name='Nivel de Materia')
    carrera = models.ForeignKey(Carrera)
    grupo = models.ManyToManyField(Grupo, verbose_name='Seleccione Los Grupos Para Materia')
    def requ(self):
        return Requisitos.objects.filter(from_materia = self)
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre
    class Meta:
        ordering = ['carrera', 'nivel']
        verbose_name_plural = 'Materias'
        permissions = (
            ('index_materia', 'Index Materia'),
            ('detail_materia', 'Detalle Materia'),
            ('report_materia', 'Reporte Materia'),
            ('requirement_materia', 'Requisitos Materia'),
        )

class Requisitos(models.Model):
    from_materia = models.ForeignKey(Materia, related_name='from_materia_id')
    to_materia = models.ForeignKey(Materia, related_name='to_materia_id')
