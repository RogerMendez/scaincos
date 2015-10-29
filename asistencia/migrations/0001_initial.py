# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('hora', models.TimeField(null=True, blank=True)),
                ('persona', models.ForeignKey(to='usuarios.Persona')),
            ],
            options={
                'ordering': ['fecha'],
                'verbose_name_plural': 'Asistencia',
                'permissions': (('detail_asistencia', 'Detalle Asistencia'), ('detail_fecha_asistencia', 'Asistencia Por Fecha'), ('historial_month_asistencia', 'Historial Mensual'), ('historial_year_asistencia', 'Historial Anual')),
            },
            bases=(models.Model,),
        ),
    ]
