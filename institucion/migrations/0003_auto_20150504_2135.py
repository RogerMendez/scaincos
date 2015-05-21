# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institucion', '0002_auto_20150504_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='nro',
            field=models.CharField(unique=True, max_length=10, verbose_name=b'Numero de Aula'),
        ),
    ]
