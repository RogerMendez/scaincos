# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institucion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aula',
            options={'ordering': ['nro'], 'verbose_name_plural': 'Aulas', 'permissions': (('index_aula', 'Index Aulas'),)},
        ),
    ]
