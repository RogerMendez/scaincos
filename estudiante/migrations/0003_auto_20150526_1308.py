# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0002_notas'),
    ]

    operations = [
        migrations.AddField(
            model_name='programacion',
            name='priner',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Primer Trimestre'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='programacion',
            name='segundo',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Segundo Trimestre'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='programacion',
            name='segundo_T',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Segundo Turno'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='programacion',
            name='tercer',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Tercer Trimestre'),
            preserve_default=True,
        ),
    ]
