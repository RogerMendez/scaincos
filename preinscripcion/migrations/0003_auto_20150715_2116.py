# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preinscripcion', '0002_preinscripcion_estado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='preinscripcion',
            options={'ordering': ['ci'], 'verbose_name': 'Preinscripcion', 'verbose_name_plural': 'Preinscripciones', 'permissions': (('index_preincripcion', 'Listado Preinscripciones'), ('report_preinscripcion', 'Reporte Preinscripciones'), ('create_inscripcion', 'Realizar Inscripcion Preinscripcion'))},
        ),
        migrations.AlterField(
            model_name='preinscripcion',
            name='ci',
            field=models.IntegerField(help_text=b'7 u 8 Numeros', verbose_name=b'Cedula de Identidad'),
        ),
    ]
