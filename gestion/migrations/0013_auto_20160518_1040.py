# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0012_auto_20151222_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gestion',
            name='gestion',
            field=models.IntegerField(unique=True, verbose_name=b'Gestion Academina', choices=[(2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016)]),
        ),
    ]
