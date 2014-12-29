# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20141228_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bundle',
            name='id',
            field=models.CharField(primary_key=True, serialize=False, max_length=64, default='09f81770-8f06-11e4-b01e-80e650264adc'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='document',
            name='id',
            field=models.CharField(primary_key=True, serialize=False, max_length=64, default='09f80048-8f06-11e4-9448-80e650264adc'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='matter',
            name='id',
            field=models.CharField(primary_key=True, serialize=False, max_length=64, default='09f7c21e-8f06-11e4-891a-80e650264adc'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.CharField(primary_key=True, serialize=False, max_length=64, default='09f664b6-8f06-11e4-8c7c-80e650264adc'),
            preserve_default=True,
        ),
    ]
