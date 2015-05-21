# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
        ('carrera', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('c_inscripcion', models.FloatField(verbose_name=b'Costo Inscripcion')),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('carrera', models.ForeignKey(to='carrera.Carrera')),
                ('estudiante', models.ForeignKey(to='usuarios.Estudiante')),
                ('gestion', models.ForeignKey(to='gestion.Gestion')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['carrera'],
                'verbose_name_plural': 'Inscripciones',
                'permissions': (('index_inscripcion', 'Index Inscripciones'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('costo', models.FloatField(verbose_name=b'Consto Matricula')),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('gestion', models.ForeignKey(to='gestion.Gestion')),
                ('inscripcion', models.ForeignKey(to='inscripcion.Inscripcion')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['inscripcion'],
                'verbose_name_plural': 'Matriculas',
                'permissions': (('index_matricula', 'Index Matriculas'),),
            },
            bases=(models.Model,),
        ),
    ]
