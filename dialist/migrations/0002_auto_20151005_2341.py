# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dialist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diamond',
            name='cert_no',
            field=models.BigIntegerField(serialize=False, default=0, unique=True, primary_key=True),
        ),
    ]
