# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 06:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20151222_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrativo',
            name='persona',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Persona'),
        ),
        migrations.AlterField(
            model_name='docente',
            name='persona',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Persona'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='persona',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Persona'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='usuario',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
