#!/usr/bin/python3

COLOR_CHOICES = { 'D' : 30,
                  'E' : 29,
                  'F' : 28,
                  'G' : 27,
                  'H' : 26,
                  'I' : 25,
                  'J' : 24,
                  'K' : 23,
                  'L' : 22,
                  'M' : 21,
                  'N' : 20,
                  'O' : 19,
                  'P' : 18,
                  'Q' : 17,
                  'R' : 16,
                  'S' : 15,
                  'T' : 14,
                  'U' : 13,
                  'V' : 12,
                  'W' : 11,
                  'X' : 10,
                  'Y' :  9,
                  'Z' :  8,
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

if len(sys.argv) < 3:
    print("Usage: %s filename date" % (sys.argv[0]))
    sys.exit()

def get_cert_no(txt):
    a = txt.strip('L')
    return int(a)

def get_color(txt):
    return COLOR_CHOICES[txt]

def get_clarity(txt):
    return CLARITY_CHOICES[txt]

index_num = 0

# the following variables are for the counting the # of entries. 
create_entry_num = 0
update_entry_num = 0
deleted_entry_num = 0

with open(sys.argv[1]) as f:
    for line in f:
        str = line.rstrip('\n')
        token = str.split('\t')

        try:
            dia = Diamond.objects.get(cert_no=get_cert_no(token[4]))

            update_entry_num += 1
            # check rapa_price and discount rate
            print("Updating the entry %s\n" % token[4])
            
            dia.rapa_price = int(token[18])
            dia.discount_rate = float(token[19])
            
            print("rapa price %d-->%d, discount rate %f-->%f" % (dia.rapa_price,int(token[18]),dia.discount_rate,float(token[19])))
            
            
            dia.rapa_price = int(token[18])
            dia.discount_rate = float(token[19])
            dia.consumer_price = dia.rapa_price * dia.carat * ( 100 - dia.discount_rate ) / 100 

            dia.update_date = sys.argv[2]

            if dia.delete_flag == True:   # this is re-entered stock
                dia.delete_date = ''
                dia.delete_flag = False
                
            dia.save()

        except Diamond.DoesNotExist:
            create_entry_num += 1
            print("Creating a new entry %s \n" % token[4])
            Diamond.objects.create( shape = 0,
                                    stone_id = token[2],
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
                                    consumer_price = int(token[18]) * float(token[5]) * ( 100 - float(token[19])) / 100,
                                    comment = token[20],
                                    input_date = sys.argv[2],
                                    update_date = '',
                                    delete_date = '',
                                    delete_flag = False,
                                )
# This is the end of update/create for loop .... pythong, so complicated !
            
for dia in Diamond.objects.all():
    if dia.input_date == sys.argv[2] or dia.update_date == sys.argv[2]:
        continue
    elif dia.delete_flag == False:
        print("Deleting %d \n" % dia.cert_no)
        deleted_entry_num += 1
        dia.delete_date = sys.argv[2]
        dia.delete_flag = True
        dia.save()

print("==================================================================")
print("update: %d, create: %d, delete: %d\n" % (update_entry_num,create_entry_num,deleted_entry_num))

# the following line should be check the delete processing...
