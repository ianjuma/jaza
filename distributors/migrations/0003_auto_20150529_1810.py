# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distributors', '0002_auto_20150529_1114'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='distributor',
            options={'ordering': ('created_at',)},
        ),
    ]
