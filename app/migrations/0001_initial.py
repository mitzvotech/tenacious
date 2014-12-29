# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attorney',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('bar_number', models.IntegerField(null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Matter',
            fields=[
                ('id', models.CharField(serialize=False, primary_key=True, max_length=64, default='e756645a-8e4d-11e4-931d-80e650264adc')),
                ('case_number', models.CharField(null=True, blank=True, unique=True, max_length=200)),
                ('plaintiff', models.CharField(null=True, blank=True, max_length=20)),
                ('defendant', models.CharField(null=True, blank=True, max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.CharField(serialize=False, primary_key=True, max_length=64, default='e755142e-8e4d-11e4-9342-80e650264adc')),
                ('first_name', models.CharField(max_length=200)),
                ('middle_name', models.CharField(null=True, blank=True, max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email_address', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('person_ptr', models.OneToOneField(serialize=False, auto_created=True, to='app.Person', primary_key=True, parent_link=True)),
                ('phone_number', models.CharField(null=True, blank=True, max_length=200)),
                ('mailing_address', models.CharField(null=True, blank=True, max_length=200)),
                ('city', models.CharField(null=True, blank=True, max_length=200)),
                ('state', models.CharField(null=True, blank=True, max_length=20)),
                ('zip_code', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=('app.person',),
        ),
        migrations.AddField(
            model_name='matter',
            name='clients',
            field=models.ManyToManyField(to='app.Client'),
            preserve_default=True,
        ),
    ]
