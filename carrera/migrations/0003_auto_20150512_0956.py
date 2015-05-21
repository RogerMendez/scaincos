# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrera', '0002_grupo_materia_grupo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materia_grupo',
            name='grupo',
        ),
        migrations.DeleteModel(
            name='Grupo',
        ),
        migrations.RemoveField(
            model_name='materia_grupo',
            name='materia',
        ),
        migrations.DeleteModel(
            name='Materia_Grupo',
        ),
    ]
