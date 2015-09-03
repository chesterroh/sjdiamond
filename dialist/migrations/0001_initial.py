# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diamond',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('shape', models.IntegerField(default=0)),
                ('stone_id', models.IntegerField(default=0)),
                ('cert_type', models.CharField(max_length=10)),
                ('cert_no', models.CharField(max_length=20)),
                ('carat', models.FloatField(default=0)),
                ('color', models.CharField(max_length=10)),
                ('clarity', models.CharField(max_length=10)),
                ('measurement', models.CharField(max_length=30)),
                ('depth', models.FloatField(default=0)),
                ('table', models.FloatField(default=0)),
                ('girdle', models.CharField(max_length=20)),
                ('culet', models.CharField(max_length=10)),
                ('cut', models.CharField(max_length=10)),
                ('pol', models.CharField(max_length=10)),
                ('sym', models.CharField(max_length=10)),
                ('flo', models.CharField(max_length=10)),
                ('hna', models.CharField(max_length=10)),
                ('rapa_price', models.IntegerField(default=0)),
                ('discount_rate', models.FloatField(default=0)),
                ('comment', models.CharField(max_length=100)),
                ('lust', models.CharField(max_length=10)),
                ('table_inc', models.CharField(max_length=10)),
                ('side_inc', models.CharField(max_length=10)),
                ('table_black', models.CharField(max_length=10)),
                ('side_black', models.CharField(max_length=10)),
                ('table_open', models.CharField(max_length=10)),
                ('side_open', models.CharField(max_length=10)),
                ('extra_fact', models.CharField(max_length=10)),
                ('key_to_symbol', models.CharField(max_length=200)),
                ('crown_angle', models.FloatField(default=0)),
                ('pav_angle', models.FloatField(default=0)),
                ('pav_height', models.FloatField(default=0)),
                ('star_length', models.FloatField(default=0)),
                ('lower_half', models.FloatField(default=0)),
                ('girdle_percent', models.FloatField(default=0)),
                ('girdle_condition', models.CharField(max_length=20)),
                ('input_date', models.DateTimeField(verbose_name='date input')),
            ],
        ),
    ]
