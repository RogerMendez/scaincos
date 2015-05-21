# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrera', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grupo', models.CharField(max_length=b'10')),
                ('abreviacion', models.CharField(max_length=b'3')),
            ],
            options={
                'ordering': ['abreviacion'],
                'verbose_name': 'Grupo',
                'verbose_name_plural': 'Grupos',
                'permissions': (('index_grupo', 'Index Grupo'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Materia_Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grupo', models.ForeignKey(to='carrera.Grupo')),
                ('materia', models.ForeignKey(to='carrera.Materia')),
            ],
            options={
                'ordering': ['materia'],
            },
            bases=(models.Model,),
        ),
    ]
