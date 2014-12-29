# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20141228_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bundle',
            name='id',
            field=models.CharField(max_length=64, serialize=False, primary_key=True, default='93430a90-8f00-11e4-abe5-80e650264adc'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='document',
            name='id',
            field=models.CharField(max_length=64, serialize=False, primary_key=True, default='9342f29e-8f00-11e4-b4cc-80e650264adc'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='matter',
            name='id',
            field=models.CharField(max_length=64, serialize=False, primary_key=True, default='9342aa14-8f00-11e4-a7c1-80e650264adc'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.CharField(max_length=64, serialize=False, primary_key=True, default='934137ba-8f00-11e4-99fb-80e650264adc'),
            preserve_default=True,
        ),
    ]
