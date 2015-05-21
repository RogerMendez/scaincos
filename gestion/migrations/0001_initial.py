# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '__first__'),
        ('carrera', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AsignacionDocente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_asignacion', models.DateField(auto_now_add=True)),
                ('docente', models.ForeignKey(to='usuarios.Docente')),
            ],
            options={
                'ordering': ['docente'],
                'verbose_name_plural': 'Asignacion Docente',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gestion', models.IntegerField(unique=True, max_length=b'4', verbose_name=b'Gestion Academina', choices=[(2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015)])),
                ('usuario', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['gestion'],
                'verbose_name_plural': 'Gestion',
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gestion_Carrera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('c_inscripcion', models.FloatField(verbose_name=b'Costo de Inscripcion')),
                ('c_matricula', models.FloatField(verbose_name=b'Consto Matricula')),
                ('carrera', models.ForeignKey(to='carrera.Carrera')),
                ('gestion', models.ForeignKey(to='gestion.Gestion')),
            ],
            options={
                'ordering': ['gestion'],
                'verbose_name_plural': 'Carreras - Gestion',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='asignaciondocente',
            name='gestion',
            field=models.ForeignKey(to='gestion.Gestion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='asignaciondocente',
            name='materia',
            field=models.ForeignKey(to='carrera.Materia'),
            preserve_default=True,
        ),
    ]
