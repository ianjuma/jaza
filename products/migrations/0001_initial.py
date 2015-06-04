# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distributors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=50, choices=[(b'E', b'Airtime'), (b'G', b'General')])),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('units', models.CharField(max_length=20)),
                ('cost_per_unit', models.PositiveIntegerField(default=1)),
                ('percent_discount', models.PositiveIntegerField(default=4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(to='distributors.Distributor')),
            ],
        ),
    ]
