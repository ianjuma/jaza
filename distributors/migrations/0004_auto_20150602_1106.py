# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distributors', '0003_auto_20150529_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distributor',
            name='id',
            field=models.AutoField(serialize=False, auto_created=True, primary_key=True),
        ),
    ]
