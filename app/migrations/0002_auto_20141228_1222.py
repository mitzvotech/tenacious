# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('sp', 'Spanish')], max_length=2, default='en'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='matter',
            name='attorneys',
            field=models.ManyToManyField(to='app.Attorney'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='matter',
            name='id',
            field=models.CharField(serialize=False, max_length=64, default='36a10e46-8e8c-11e4-b6e1-80e650264adc', primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.CharField(serialize=False, max_length=64, default='369fa72c-8e8c-11e4-9905-80e650264adc', primary_key=True),
            preserve_default=True,
        ),
    ]
