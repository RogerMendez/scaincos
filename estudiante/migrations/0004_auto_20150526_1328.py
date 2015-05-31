# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0003_auto_20150526_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programacion',
            name='priner',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Primer Trimestre'),
        ),
        migrations.AlterField(
            model_name='programacion',
            name='segundo',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Segundo Trimestre'),
        ),
        migrations.AlterField(
            model_name='programacion',
            name='tercer',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Tercer Trimestre'),
        ),
    ]
