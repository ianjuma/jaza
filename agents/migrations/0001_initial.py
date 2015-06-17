# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.CharField(unique=True, max_length=12)),
                ('national_id', models.PositiveIntegerField(unique=True)),
            ],
            options={
                'ordering': ('national_id',),
            },
        ),
        migrations.CreateModel(
            name='AgentProductRelationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('agent_id', models.ForeignKey(to='agents.Agent')),
                ('product_id', models.ForeignKey(to='products.Product')),
            ],
        ),
        migrations.AddField(
            model_name='agent',
            name='products',
            field=models.ManyToManyField(to='products.Product', through='agents.AgentProductRelationship'),
        ),
        migrations.AddField(
            model_name='agent',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
