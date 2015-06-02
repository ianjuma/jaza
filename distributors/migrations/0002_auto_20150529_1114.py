# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distributors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distributor',
            name='national_id',
            field=models.IntegerField(),
        ),
    ]
