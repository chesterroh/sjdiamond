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
                ('shape', models.IntegerField(default=0)),
                ('stone_id', models.IntegerField(default=0)),
                ('cert_type', models.CharField(max_length=10)),
                ('cert_no', models.BigIntegerField(default=0, serialize=False, primary_key=True)),
                ('carat', models.FloatField(default=0)),
                ('color', models.IntegerField(default=0, choices=[(30, 'D'), (29, 'E'), (28, 'F'), (27, 'G'), (26, 'H'), (25, 'I'), (24, 'J'), (23, 'K'), (22, 'L'), (21, 'M'), (20, 'N'), (19, 'O'), (18, 'P'), (17, 'Q'), (16, 'R'), (15, 'S'), (14, 'T'), (13, 'U'), (12, 'V'), (11, 'W'), (10, 'X'), (9, 'Y'), (8, 'Z')])),
                ('clarity', models.IntegerField(default=0, choices=[(20, 'FL'), (19, 'IF'), (18, 'VVS1'), (17, 'VVS2'), (16, 'VS1'), (15, 'VS2'), (14, 'SI1'), (13, 'SI2'), (12, 'SI3'), (11, 'I1'), (10, 'I2'), (9, 'I3')])),
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
                ('input_date', models.CharField(max_length=7)),
                ('update_date', models.CharField(max_length=7)),
                ('delete_date', models.CharField(max_length=7)),
                ('delete_flag', models.BooleanField(default=False)),
            ],
        ),
    ]
