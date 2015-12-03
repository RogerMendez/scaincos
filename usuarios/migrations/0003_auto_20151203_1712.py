# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import usuarios.models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_docente_carga_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='nro_docente',
            field=models.IntegerField(unique=True, verbose_name=b'Item Docente'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_nac',
            field=models.DateField(verbose_name=b'Fecha de Nacimiento', validators=[usuarios.models.validate_fecha_nac]),
        ),
    ]
