# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docente', '0002_auto_20151029_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excelnotas',
            name='excel',
            field=models.FileField(upload_to=b'notas'),
        ),
    ]
