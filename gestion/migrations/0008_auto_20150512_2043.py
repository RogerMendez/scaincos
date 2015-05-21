# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0007_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='hora',
            field=models.TimeField(default=b'00:00:00'),
        ),
    ]
