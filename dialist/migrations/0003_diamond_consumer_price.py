# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dialist', '0002_auto_20151005_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='diamond',
            name='consumer_price',
            field=models.IntegerField(default=0),
        ),
    ]
