# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(max_length=1, choices=[(b'E', b'Airtime'), (b'G', b'General')]),
        ),
    ]
