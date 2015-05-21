# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=b'50', verbose_name=b'Nombre de Carrera')),
                ('tiempo', models.CharField(max_length=b'2', verbose_name=b'Tiempo de Carrera', choices=[(b'1', b'1 A\xc3\xb1o'), (b'2', b'2 A\xc3\xb1os'), (b'3', b'3 A\xc3\xb1os'), (b'4', b'4 A\xc3\xb1os'), (b'5', b'5 A\xc3\xb1os')])),
                ('fecha_creacion', models.DateField(verbose_name=b'Creacion de Carrera')),
                ('resenha', models.TextField(verbose_name=b'Breve Rese\xc3\xb1a')),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Carreras',
                'permissions': (('index_carrera', 'Index Carreras'), ('detail_carrera', 'Detalle Carrera'), ('report_carrera', 'Reporte Carrera')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=b'50', verbose_name=b'Nombre Materia')),
                ('sigla', models.CharField(unique=True, max_length=b'10', verbose_name=b'Sigla Materia')),
                ('nivel', models.IntegerField(verbose_name=b'Nivel de Materia')),
                ('carrera', models.ForeignKey(to='carrera.Carrera')),
            ],
            options={
                'ordering': ['carrera', 'nivel'],
                'verbose_name_plural': 'Materias',
                'permissions': (('index_materia', 'Index Materia'), ('detail_materia', 'Detalle Materia'), ('report_materia', 'Reporte Materia'), ('requirement_materia', 'Requisitos Materia')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Requisitos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_materia', models.ForeignKey(related_name=b'from_materia_id', to='carrera.Materia')),
                ('to_materia', models.ForeignKey(related_name=b'to_materia_id', to='carrera.Materia')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
