# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_auto_20151222_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='email',
            field=models.EmailField(max_length=75, verbose_name=b'Correo Electronico'),
        ),
    ]
