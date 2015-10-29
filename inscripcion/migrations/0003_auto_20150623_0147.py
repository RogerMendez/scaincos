# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0002_inscripcion_estado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inscripcion',
            options={'ordering': ['carrera'], 'verbose_name_plural': 'Inscripciones', 'permissions': (('index_inscripcion', 'Index Inscripciones'), ('report_inscripcion', 'Reporte Inscripciones'))},
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='nro_folio',
            field=models.CharField(max_length=b'100', null=True),
            preserve_default=True,
        ),
    ]
