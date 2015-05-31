# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=50)),
                ('programacion', models.ForeignKey(to='estudiante.Programacion')),
            ],
            options={
                'ordering': ['programacion'],
                'verbose_name': 'Nota',
                'verbose_name_plural': 'Notas',
            },
            bases=(models.Model,),
        ),
    ]
