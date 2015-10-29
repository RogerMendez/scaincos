# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excelnotas',
            name='excel',
            field=models.FileField(upload_to=b'notas/%Y/%m/%d'),
        ),
    ]
