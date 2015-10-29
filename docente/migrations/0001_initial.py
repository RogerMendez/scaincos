# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelNotas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('excel', models.FileField(upload_to=b'Notas/%Y/%m/%d')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
