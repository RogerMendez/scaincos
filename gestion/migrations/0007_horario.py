# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institucion', '0003_auto_20150504_2135'),
        ('carrera', '0005_auto_20150512_1921'),
        ('gestion', '0006_asignaciondocente_grupo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.CharField(max_length=10)),
                ('hora', models.TimeField()),
                ('aula', models.ForeignKey(to='institucion.Aula')),
                ('gestion', models.ForeignKey(to='gestion.Gestion')),
                ('materia', models.ForeignKey(to='carrera.Materia')),
            ],
            options={
                'ordering': ['materia'],
                'verbose_name': 'Horario',
                'verbose_name_plural': 'Horarios',
                'permissions': ('index_horario', 'Index de Horario'),
            },
            bases=(models.Model,),
        ),
    ]
