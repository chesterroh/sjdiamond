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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('shape', models.IntegerField(default=0)),
                ('stone_id', models.IntegerField(default=0)),
                ('cert_type', models.CharField(max_length=10)),
                ('cert_no', models.BigIntegerField(default=0)),
                ('carat', models.FloatField(default=0)),
                ('color', models.IntegerField(default=0, choices=[(20, 'D'), (19, 'E'), (18, 'F'), (17, 'G'), (16, 'H'), (15, 'I'), (14, 'J'), (13, 'K'), (12, 'L'), (11, 'M'), (10, 'N'), (9, 'O'), (8, 'P'), (7, 'Q'), (6, 'R'), (5, 'S'), (4, 'T'), (3, 'U'), (2, 'V')])),
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
                ('lust', models.CharField(max_length=10)),
                ('table_inc', models.CharField(max_length=10)),
                ('side_inc', models.CharField(max_length=10)),
                ('table_black', models.CharField(max_length=10)),
                ('side_black', models.CharField(max_length=10)),
                ('table_open', models.CharField(max_length=10)),
                ('side_open', models.CharField(max_length=10)),
                ('extra_facet', models.CharField(max_length=10)),
                ('key_to_symbol', models.CharField(max_length=200)),
                ('crown_angle', models.FloatField(default=0)),
                ('crown_height', models.FloatField(default=0)),
                ('pav_angle', models.FloatField(default=0)),
                ('pav_height', models.FloatField(default=0)),
                ('star_length', models.FloatField(default=0)),
                ('lower_half', models.FloatField(default=0)),
                ('girdle_percent', models.FloatField(default=0)),
                ('girdle_condition', models.CharField(max_length=20)),
                ('input_date', models.DateTimeField(verbose_name='date input')),
                ('update_date', models.DateTimeField(verbose_name='date updated')),
                ('delete_flag', models.BooleanField(default=False)),
            ],
        ),
    ]
