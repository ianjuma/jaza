# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('account_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('national_id', models.PositiveIntegerField(unique=True)),
                ('nationality', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ('created_at',),
            },
            bases=('authentication.account',),
        ),
        migrations.CreateModel(
            name='AgentProductRelationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('agent_id', models.ForeignKey(to='agents.Agent')),
                ('distributor_id', models.ForeignKey(to='products.Distributor')),
                ('product_id', models.ForeignKey(to='products.Product')),
            ],
        ),
        migrations.AddField(
            model_name='agent',
            name='products',
            field=models.ManyToManyField(to='products.Distributor', through='agents.AgentProductRelationship'),
        ),
    ]
