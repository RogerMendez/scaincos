# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0009_auto_20150513_0054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gestion_carrera',
            options={'ordering': ['gestion'], 'verbose_name_plural': 'Carreras - Gestion', 'permissions': (('report_gestion', 'Reporte Gestiones'),)},
        ),
    ]
