# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dialist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diamond',
            name='crown_height',
            field=models.FloatField(default=0),
        ),
    ]
