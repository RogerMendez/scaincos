# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrera', '0004_auto_20150512_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='sigla',
            field=models.CharField(max_length=b'10', verbose_name=b'Sigla Materia'),
        ),
    ]
