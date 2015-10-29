# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='docente',
            name='carga_horario',
            field=models.PositiveIntegerField(default=1, help_text=b'En Horas', verbose_name=b'Carga Horaria Semanal'),
            preserve_default=True,
        ),
    ]
