# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distributors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tracking', models.CharField(max_length=1, choices=[(b'1', b'Tracked'), (b'0', b'NOT TRACKED')])),
                ('category', models.CharField(max_length=1, choices=[(b'E', b'Airtime'), (b'G', b'General')])),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('units', models.CharField(max_length=20)),
                ('cost_per_unit', models.PositiveIntegerField(default=1)),
                ('percent_discount', models.PositiveIntegerField(default=4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(to='products.Category')),
                ('owner', models.ForeignKey(to='distributors.Distributor')),
            ],
        ),
    ]
