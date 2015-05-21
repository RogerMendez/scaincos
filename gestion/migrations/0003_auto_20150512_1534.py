# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_grupo_materia_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia_grupo',
            name='grupo',
            field=models.ForeignKey(to='gestion.Grupo', unique=True),
        ),
        migrations.AlterField(
            model_name='materia_grupo',
            name='materia',
            field=models.ForeignKey(to='carrera.Materia', unique=True),
        ),
    ]
