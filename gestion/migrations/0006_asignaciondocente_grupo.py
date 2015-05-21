# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrera', '0005_auto_20150512_1921'),
        ('gestion', '0005_auto_20150512_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignaciondocente',
            name='grupo',
            field=models.ForeignKey(to='carrera.Grupo', null=True),
            preserve_default=True,
        ),
    ]
