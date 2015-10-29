# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preinscripcion', '0003_auto_20150715_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='preinscripcion',
            name='avatar',
            field=models.ImageField(default=b'1', upload_to=b'avatar', verbose_name=b'Seleccione Una Imagen'),
            preserve_default=True,
        ),
    ]
