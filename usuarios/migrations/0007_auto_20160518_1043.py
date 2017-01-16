# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_auto_20160518_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='ci',
            field=models.CharField(unique=True, max_length=10, verbose_name=b'Cedula de Identidad'),
        ),
    ]
