# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='tracking',
            field=models.CharField(max_length=1, choices=[(b'1', b'TRACKED'), (b'0', b'NOT TRACKED')]),
        ),
    ]
