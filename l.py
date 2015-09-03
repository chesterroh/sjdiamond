#!/usr/bin/python3

import sys
from dialist.models import Diamond

import datetime
from django.utils import timezone

import django
django.setup()

if len(sys.argv) < 2:
    print("Usage: %s filename" % (sys.argv[0]))
    sys.exit()

max_key_to_symbol = 0
max_comment = 0

"""
maxlen_list = []
zerolen_list = []
for i in range(38):
    maxlen_list.append(0)
    zerolen_list.append(0)
"""

with open(sys.argv[1]) as f:
    for line in f:
        str = line.rstrip('\n')
        token = str.split('\t')

        Diamond.objects.create( shape = 0,
            stone_id = int(token[2]),
            cert_type = token[3],
            cert_no = token[4],
            carat = float(token[5]),
            color = token[6],
            clarity = token[7],
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
            input_date = timezone.now()
        )

        print("diamond cert_no %s added.\n" % token[4])


"""

        serial_no = token[0]
        shape = token[1]
        stone_id = int(token[2])
        cert_type = token[3]
        cert_no = token[4]
        carat = float(token[5])
        color = token[6]
        clarity = token[7]
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

        if( len(comment) > max_comment):
            max_comment = len(comment)

        if( len(key_to_symbol) > max_key_to_symbol ):
            max_key_to_symbol = len(key_to_symbol)

        t_counter = 0

        for t in token:
            if( len(t) > maxlen_list[t_counter]):
                maxlen_list[t_counter] = len(t)
            t_counter += 1

        t_counter = 0
        for t in token:
            if( len(t) == 0 ):
                zerolen_list[t_counter] = 10
            t_counter += 1
                

print("Max key to Symbol %d , max comment %d\n" % (max_key_to_symbol,max_comment))
# max 300 characters will cover the error margin.
print(maxlen_list)
print(zerolen_list)
"""
