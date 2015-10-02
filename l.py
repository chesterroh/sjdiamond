#!/usr/bin/python3

COLOR_CHOICES = { 'D' : 20,
                  'E' : 19,
                  'F' : 18,
                  'G' : 17,
                  'H' : 16,
                  'I' : 15,
                  'J' : 14,
                  'K' : 13,
                  'L' : 12,
                  'M' : 11,
                  'N' : 10,
                  'O' : 9,
                  'P' : 8,
                  'Q' : 7,
                  'R' : 6,
                  'S' : 5,
                  'T' : 4,
                  'U' : 3,
                  'V' : 2,
                  }

CLARITY_CHOICES = { 'FL' : 20,
                    'IF' : 19,
                    'VVS1' : 18,
                    'VVS2' : 17,
                    'VS1' : 16,
                    'VS2' : 15,
                    'SI1' : 14,
                    'SI2' : 13,
                    'SI3' : 12,
                    'I1' : 11,
                    'I2' : 10,
                    'I3' : 9,
                    }

import sys
from dialist.models import Diamond

import datetime
from django.utils import timezone

import django
django.setup()

if len(sys.argv) < 2:
    print("Usage: %s filename" % (sys.argv[0]))
    sys.exit()

def get_cert_no(txt):
    a = txt.strip('L')
    return int(a)

def get_color(txt):
    return COLOR_CHOICES[txt]

def get_clarity(txt):
    return CLARITY_CHOICES[txt]


index_num = 0 


with open(sys.argv[1]) as f:
    for line in f:
        str = line.rstrip('\n')
        token = str.split('\t')

        Diamond.objects.create( shape = 0,
                                stone_id = int(token[2]),
                                cert_type = token[3],
                                cert_no = get_cert_no(token[4]),
                                carat = float(token[5]),
                                color = get_color(token[6]),
                                clarity = get_clarity(token[7]),
                                measurement = token[8],
                                depth = float(token[9]),
                                table = float(token[10]),
                                girdle = token[11],
                                culet = token[12],
                                cut = token[13],
                                pol = token[14],
                                sym = token[15],
                                flo = token[16],
                                hna = token[17],
                                rapa_price = int(token[18]),
                                discount_rate = float(token[19]),
                                comment = token[20],
                                lust = token[21],
                                table_inc = token[22],
                                side_inc = token[23],
                                table_black = token[24],
                                side_black = token[25],
                                table_open = token[26],
                                side_open = token[27],
                                extra_facet = token[28],
                                key_to_symbol = token[29],
                                crown_angle = float(token[30]),
                                crown_height = float(token[31]),
                                pav_angle = float(token[32]),
                                pav_height = float(token[33]),
                                star_length = float(token[34]),
                                lower_half = float(token[35]),
                                girdle_percent = float(token[36]),
                                girdle_condition = token[37],
                                input_date = timezone.now(),
                                update_date = timezone.now(),
                                delete_flag = False,
                            )

        print("stone_id %s processed. \n" % (token[2]))

"""
with open(sys.argv[1]) as f:
    for line in f:
        str = line.rstrip('\n')
        token = str.split('\t')

        serial_no = token[0]
        shape = token[1]
        stone_id = int(token[2])
        cert_type = token[3]
        cert_no = get_cert_no(token[4])
        carat = float(token[5])
        color = get_color(token[6])
        clarity = get_clarity(token[7])
        measurement = token[8]
        depth = float(token[9])
        table = float(token[10])
        girdle = token[11]
        culet = token[12]
        cut = token[13]
        pol = token[14]
        sym = token[15]
        flo = token[16]
        hna = token[17]
        rapa_price = int(token[18])
        discount_rate = float(token[19])
        comment = token[20]
        lust = token[21]
        table_inc = token[22]
        side_inc = token[23]
        table_black = token[24]
        side_black = token[25]
        table_open = token[26]
        side_open = token[27]
        extra_facet = token[28]
        key_to_symbol = token[29]
        crown_angle = float(token[30])
        crown_height = float(token[31])
        pav_angle = float(token[32])
        pav_height = float(token[33])
        star_length = float(token[34])
        lower_half = float(token[35])
        girdle_percent = float(token[36])
        girdle_condition = token[37]

        print("cert_nd:%d / color:%d / clarity:%d" % ( cert_no, color, clarity) )
"""
