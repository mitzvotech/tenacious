# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20141228_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bundle',
            name='date_created',
        ),
        migrations.AlterField(
            model_name='bundle',
            name='id',
            field=models.CharField(serialize=False, default='e121c83e-8f00-11e4-959c-80e650264adc', primary_key=True, max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='document',
            name='id',
            field=models.CharField(serialize=False, default='e121b0e2-8f00-11e4-937e-80e650264adc', primary_key=True, max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='matter',
            name='id',
            field=models.CharField(serialize=False, default='e1217134-8f00-11e4-96b2-80e650264adc', primary_key=True, max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.CharField(serialize=False, default='e1201f46-8f00-11e4-9f6d-80e650264adc', primary_key=True, max_length=64),
            preserve_default=True,
        ),
    ]
