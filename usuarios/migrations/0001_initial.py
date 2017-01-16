# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrativo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nro_item', models.IntegerField(verbose_name=b'Numero de Item')),
                ('cargo', models.CharField(max_length=50, verbose_name=b'Cargo Ocupado')),
            ],
            options={
                'ordering': ['nro_item'],
                'verbose_name_plural': 'Administrativos',
                'permissions': (('index_administrativo', 'Index Administrativos'), ('detail_administrativo', 'Detalle Administrativos'), ('report_administrativo', 'Reporte Administrativos')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nro_docente', models.IntegerField(unique=True, verbose_name=b'Codigo Docente')),
                ('fecha_ingreso', models.DateField(verbose_name=b'Fecha de Ingreso')),
            ],
            options={
                'ordering': ['nro_docente'],
                'verbose_name_plural': 'Docentes',
                'permissions': (('index_docente', 'Index Docente'), ('detail_docente', 'Detalle Docente'), ('report_docente', 'Reporte Docente')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nro_estudiante', models.IntegerField(unique=True, verbose_name=b'Codigo Estudiante')),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True)),
                ('fecha_salida', models.DateTimeField(null=True, blank=True)),
                ('terminado', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['nro_estudiante'],
                'verbose_name_plural': 'Estudiantes',
                'permissions': (('index_estudiante', 'Index Estudiante'), ('detail_estudiante', 'Detalle Estudiante'), ('report_estudiante', 'Reporte Estudiante')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ci', models.IntegerField(help_text=b'7 u 8 Numeros', unique=True, verbose_name=b'Cedula de Identidad')),
                ('nombre', models.CharField(max_length=20, verbose_name=b'Nombres')),
                ('paterno', models.CharField(max_length=20, verbose_name=b'Apellido Paterno')),
                ('materno', models.CharField(max_length=20, verbose_name=b'Apellido Materno')),
                ('fecha_nac', models.DateField(verbose_name=b'Fecha de Nacimiento')),
                ('direccion', models.CharField(max_length=100, verbose_name=b'Direcci\xc3\xb3n')),
                ('telefono', models.CharField(max_length=10, verbose_name=b'Telefono/Celular')),
                ('avatar', models.ImageField(upload_to=b'avatar', verbose_name=b'Seleccione Una Imagen')),
                ('activo', models.BooleanField(default=True)),
                ('tipo', models.CharField(default=b'Estudiante', max_length=20)),
                ('email', models.EmailField(max_length=75, verbose_name=b'Correo Electronico')),
                ('usuario', models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'ordering': ['ci'],
                'verbose_name_plural': 'Personas',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='persona',
            field=models.ForeignKey(null=True, blank=True, to='usuarios.Persona', unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='docente',
            name='persona',
            field=models.ForeignKey(null=True, blank=True, to='usuarios.Persona', unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='administrativo',
            name='persona',
            field=models.ForeignKey(null=True, blank=True, to='usuarios.Persona', unique=True),
            preserve_default=True,
        ),
    ]
