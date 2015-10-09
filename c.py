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

            if dia.delete_flag == True:
                print("%s is marked as delete_flag True\n" % token[4])
                print("%s %s %s\n" % (dia.input_date,dia.update_date,dia.delete_date))
            
        except Diamond.DoesNotExist:

            print("%s doesn't exist at all" % token[4])

print("%d numbers processed \n" % update_entry_num)
