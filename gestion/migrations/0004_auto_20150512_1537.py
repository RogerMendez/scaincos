# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_auto_20150512_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='abreviacion',
            field=models.CharField(unique=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='grupo',
            field=models.CharField(unique=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='materia_grupo',
            name='grupo',
            field=models.ForeignKey(to='gestion.Grupo'),
        ),
        migrations.AlterField(
            model_name='materia_grupo',
            name='materia',
            field=models.ForeignKey(to='carrera.Materia'),
        ),
    ]
