# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=1, choices=[(b'E', b'Airtime'), (b'G', b'General')])),
            ],
            options={
                'ordering': ('id',),
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.OneToOneField(related_name='distributor_id', primary_key=True, serialize=False, to='authentication.Account')),
                ('national_id', models.IntegerField(unique=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='DistributorProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('distributor_id', models.ForeignKey(related_name='dist_id', to='products.Distributor')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_id', models.ForeignKey(related_name='product_category', to='products.Category')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='distributorproduct',
            name='product_id',
            field=models.ForeignKey(related_name='owner_id', to='products.Product'),
        ),
        migrations.AddField(
            model_name='distributor',
            name='products',
            field=models.ManyToManyField(to='products.Product', through='products.DistributorProduct'),
        ),
    ]
