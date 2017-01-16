# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrera', '0003_auto_20150512_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grupo', models.CharField(unique=True, max_length=10)),
                ('abreviacion', models.CharField(unique=True, max_length=3)),
            ],
            options={
                'ordering': ['abreviacion'],
                'verbose_name': 'Grupo',
                'verbose_name_plural': 'Grupos',
                'permissions': (('index_grupo', 'Index Grupo'),),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='materia',
            name='grupo',
            field=models.ManyToManyField(to='carrera.Grupo', verbose_name=b'Seleccione Los Grupos Para Materia'),
            preserve_default=True,
        ),
    ]
