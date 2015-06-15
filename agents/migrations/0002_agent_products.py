# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='products',
            field=models.ManyToManyField(to='products.Product', through='agents.AgentProductRelationship'),
        ),
    ]
