# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='pin',
            field=models.CharField(default=None, max_length=64),
        ),
    ]
