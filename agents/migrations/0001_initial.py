# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.OneToOneField(primary_key=True, serialize=False, to='authentication.Account')),
                ('national_id', models.PositiveIntegerField(unique=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='ProductChannels',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('agent_id', models.ForeignKey(to='agents.Agent')),
                ('product_id', models.ForeignKey(to='products.Product')),
            ],
        ),
        migrations.AddField(
            model_name='agent',
            name='products',
            field=models.ManyToManyField(to='products.Product', through='agents.ProductChannels'),
        ),
    ]
