# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrera', '0005_auto_20150512_1921'),
        ('gestion', '0009_auto_20150513_0054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preinscripcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ci', models.IntegerField(help_text=b'7 u 8 Numeros', unique=True, verbose_name=b'Cedula de Identidad')),
                ('nombre', models.CharField(max_length=20, verbose_name=b'Nombres')),
                ('paterno', models.CharField(max_length=20, verbose_name=b'Apellido Paterno')),
                ('materno', models.CharField(max_length=20, verbose_name=b'Apellido Materno')),
                ('fecha_nac', models.DateField(verbose_name=b'Fecha de Nacimiento')),
                ('direccion', models.CharField(max_length=100, verbose_name='Direcci\xf3n')),
                ('telefono', models.CharField(max_length=10, verbose_name=b'Telefono/Celular')),
                ('carrera', models.ForeignKey(to='carrera.Carrera')),
                ('gestion', models.ForeignKey(to='gestion.Gestion', null=True)),
            ],
            options={
                'ordering': ['ci'],
                'verbose_name': 'Preinscripcion',
                'verbose_name_plural': 'Preinscripciones',
            },
            bases=(models.Model,),
        ),
    ]
