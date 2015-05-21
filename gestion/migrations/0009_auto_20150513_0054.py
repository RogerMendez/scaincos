# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0008_auto_20150512_2043'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='horario',
            options={'ordering': ['dia'], 'verbose_name': 'Horario', 'verbose_name_plural': 'Horarios', 'permissions': (('index_horario', 'Index de Horario'),)},
        ),
        migrations.RemoveField(
            model_name='horario',
            name='materia',
        ),
        migrations.AddField(
            model_name='horario',
            name='asignaciondocente',
            field=models.ForeignKey(default=1, to='gestion.AsignacionDocente'),
            preserve_default=False,
        ),
    ]
