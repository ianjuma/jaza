# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveIntegerField()),
                ('price_per_unit', models.PositiveIntegerField(default=1)),
                ('percent_discount', models.PositiveIntegerField(default=4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('agent_id', models.ForeignKey(to='agents.Agent')),
                ('distributor_id', models.ForeignKey(to='products.Distributor')),
                ('product_id', models.ForeignKey(to='products.Product')),
            ],
        ),
    ]
