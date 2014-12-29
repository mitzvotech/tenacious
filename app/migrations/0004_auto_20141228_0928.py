# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20141228_0908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bundle',
            fields=[
                ('id', models.CharField(serialize=False, max_length=64, primary_key=True, default='c150bb48-8e9d-11e4-b4b5-80e650264adc')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('documents', models.ManyToManyField(to='app.Document')),
                ('matter', models.ForeignKey(to='app.Matter')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='matterpackage',
            name='documents',
        ),
        migrations.RemoveField(
            model_name='matterpackage',
            name='matter',
        ),
        migrations.DeleteModel(
            name='MatterPackage',
        ),
        migrations.AlterField(
            model_name='document',
            name='document_file',
            field=models.FileField(upload_to=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='document',
            name='id',
            field=models.CharField(serialize=False, max_length=64, primary_key=True, default='c150a3ec-8e9d-11e4-93ec-80e650264adc'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='matter',
            name='id',
            field=models.CharField(serialize=False, max_length=64, primary_key=True, default='c1506576-8e9d-11e4-bee2-80e650264adc'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.CharField(serialize=False, max_length=64, primary_key=True, default='c14f0a34-8e9d-11e4-b327-80e650264adc'),
            preserve_default=True,
        ),
    ]
