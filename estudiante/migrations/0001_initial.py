# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrera', '0005_auto_20150512_1921'),
        ('inscripcion', '0002_inscripcion_estado'),
        ('gestion', '0009_auto_20150513_0054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('gestion', models.ForeignKey(to='gestion.Gestion')),
                ('grupo', models.ForeignKey(to='carrera.Grupo')),
                ('inscripcion', models.ForeignKey(to='inscripcion.Inscripcion')),
                ('materia', models.ForeignKey(to='carrera.Materia')),
            ],
            options={
                'ordering': ['inscripcion'],
                'verbose_name': 'Programacion',
                'verbose_name_plural': 'Programaciones',
            },
            bases=(models.Model,),
        ),
    ]
