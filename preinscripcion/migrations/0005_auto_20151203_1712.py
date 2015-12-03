# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import preinscripcion.models


class Migration(migrations.Migration):

    dependencies = [
        ('preinscripcion', '0004_preinscripcion_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preinscripcion',
            name='fecha_nac',
            field=models.DateField(verbose_name=b'Fecha de Nacimiento', validators=[preinscripcion.models.validate_fecha_nac]),
        ),
    ]
