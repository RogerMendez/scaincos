# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0002_auto_20150607_0112'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asistencia',
            options={'ordering': ['fecha'], 'verbose_name_plural': 'Asistencia', 'permissions': (('detail_asistencia', 'Detalle Asistencia'), ('detail_fecha_asistencia', 'Asistencia Por Fecha'), ('historial_month_asistencia', 'Historial Mensual'), ('historial_year_asistencia', 'Historial Anual'), ('report_asistencia', 'Reporte Asistencia'))},
        ),
    ]
