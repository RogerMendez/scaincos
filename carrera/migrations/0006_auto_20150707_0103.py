# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrera', '0005_auto_20150512_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrera',
            name='area',
            field=models.CharField(default=b'Comercial', max_length=b'50'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='carrera',
            name='nivel',
            field=models.CharField(default=b'Superior', max_length=b'50'),
            preserve_default=True,
        ),
    ]
