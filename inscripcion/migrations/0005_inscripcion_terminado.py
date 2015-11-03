# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0004_inscripcion_nro_libro'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscripcion',
            name='terminado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
