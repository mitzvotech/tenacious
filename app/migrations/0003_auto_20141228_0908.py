# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20141228_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.CharField(default='0e74f694-8e9b-11e4-8a10-80e650264adc', serialize=False, max_length=64, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('language', models.CharField(default='en', max_length=2, choices=[('en', 'English'), ('sp', 'Spanish')])),
                ('document_file', models.FileField(upload_to='/documents/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MatterPackage',
            fields=[
                ('id', models.CharField(default='0e750dbe-8e9b-11e4-aa95-80e650264adc', serialize=False, max_length=64, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('documents', models.ManyToManyField(to='app.Document')),
                ('matter', models.ForeignKey(to='app.Matter')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='matter',
            name='id',
            field=models.CharField(default='0e74b922-8e9b-11e4-8e8d-80e650264adc', serialize=False, max_length=64, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.CharField(default='0e736a7a-8e9b-11e4-98a7-80e650264adc', serialize=False, max_length=64, primary_key=True),
            preserve_default=True,
        ),
    ]
