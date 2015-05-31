# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0004_auto_20150526_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='programacion',
            name='final',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='programacion',
            name='priner',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Primer Trimestre', blank=True),
        ),
        migrations.AlterField(
            model_name='programacion',
            name='segundo',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Segundo Trimestre', blank=True),
        ),
        migrations.AlterField(
            model_name='programacion',
            name='segundo_T',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Segundo Turno', blank=True),
        ),
        migrations.AlterField(
            model_name='programacion',
            name='tercer',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Tercer Trimestre', blank=True),
        ),
    ]
