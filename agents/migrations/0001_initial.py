# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(unique=True, max_length=16)),
                ('pin', models.CharField(max_length=64, null=True, blank=True)),
                ('verification_code', models.IntegerField()),
                ('verification_status', models.CharField(default=b'N', max_length=1, choices=[(b'V', b'VERIFIED'), (b'N', b'NOT_VERIFIED')])),
                ('products', models.ManyToManyField(to='products.Product')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
