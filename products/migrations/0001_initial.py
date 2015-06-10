# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
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
            name='Distributor',
            fields=[
                ('account_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('national_id', models.IntegerField(unique=True)),
                ('nationality', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ('created_at',),
            },
            bases=('authentication.account',),
        ),
        migrations.CreateModel(
            name='DistributorProductRelationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('distributor_id', models.ForeignKey(to='products.Distributor')),
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
            ],
        ),
        migrations.AddField(
            model_name='distributorproductrelationship',
            name='product_id',
            field=models.ForeignKey(to='products.Product'),
        ),
        migrations.AddField(
            model_name='distributor',
            name='products',
            field=models.ManyToManyField(to='products.Product', through='products.DistributorProductRelationship'),
        ),
    ]
