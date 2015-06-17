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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('owner', models.ForeignKey(related_name='product_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.AddField(
            model_name='distributor',
            name='products',
            field=models.ManyToManyField(to='products.Product'),
        ),
        migrations.AddField(
            model_name='distributor',
            name='user',
            field=models.ForeignKey(related_name='distributor_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
