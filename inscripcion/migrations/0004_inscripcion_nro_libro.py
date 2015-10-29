# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0003_auto_20150623_0147'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscripcion',
            name='nro_libro',
            field=models.PositiveIntegerField(null=True),
            preserve_default=True,
        ),
    ]
