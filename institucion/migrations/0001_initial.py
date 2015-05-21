# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nro', models.CharField(max_length=10, verbose_name=b'Numero de Aula')),
            ],
            options={
                'ordering': ['nro'],
                'verbose_name_plural': 'Aulas',
                'permissions': ('index_aula', 'Index Aulas'),
            },
            bases=(models.Model,),
        ),
    ]
