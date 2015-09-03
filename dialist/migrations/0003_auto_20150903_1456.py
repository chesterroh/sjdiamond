# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dialist', '0002_diamond_crown_height'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diamond',
            old_name='extra_fact',
            new_name='extra_facet',
        ),
    ]
