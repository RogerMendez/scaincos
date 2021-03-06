# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 06:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrera', '0006_auto_20150707_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrera',
            name='area',
            field=models.CharField(default=b'Comercial', max_length=50),
        ),
        migrations.AlterField(
            model_name='carrera',
            name='nivel',
            field=models.CharField(default=b'Superior', max_length=50),
        ),
        migrations.AlterField(
            model_name='carrera',
            name='nombre',
            field=models.CharField(max_length=50, unique=True, verbose_name=b'Nombre de Carrera'),
        ),
        migrations.AlterField(
            model_name='carrera',
            name='tiempo',
            field=models.CharField(choices=[(b'1', b'1 A\xc3\xb1o'), (b'2', b'2 A\xc3\xb1os'), (b'3', b'3 A\xc3\xb1os'), (b'4', b'4 A\xc3\xb1os'), (b'5', b'5 A\xc3\xb1os')], max_length=2, verbose_name=b'Tiempo de Carrera'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='abreviacion',
            field=models.CharField(max_length=3, unique=True),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='grupo',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='materia',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name=b'Nombre Materia'),
        ),
        migrations.AlterField(
            model_name='materia',
            name='sigla',
            field=models.CharField(max_length=10, verbose_name=b'Sigla Materia'),
        ),
    ]
