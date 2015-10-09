from django.db import models

# Create your models here.

class Diamond(models.Model):
    COLOR_CHOICES = (
        (30 , 'D'),
        (29 , 'E'),
        (28 , 'F'),
        (27 , 'G'),
        (26 , 'H'),
        (25 , 'I'),
        (24 , 'J'),
        (23 , 'K'),
        (22 , 'L'),
        (21 , 'M'),
        (20 , 'N'),
        (19, 'O'),
        (18 , 'P'),
        (17 , 'Q'),
        (16 , 'R'),
        (15 , 'S'),
        (14 , 'T'),
        (13 , 'U'),
        (12 , 'V'),
        (11 , 'W'),
        (10 , 'X'),
        (9 , 'Y'),
        (8 , 'Z'),
        )
    CLARITY_CHOICES = (
        (20 , 'FL'),
        (19 , 'IF'),
        (18 , 'VVS1'),
        (17 , 'VVS2'),
        (16 , 'VS1'),
        (15 , 'VS2'),
        (14 , 'SI1'),
        (13 , 'SI2'),
        (12 , 'SI3'),
        (11 , 'I1'),
        (10 , 'I2'),
        (9 , 'I3'),
        )

    shape = models.IntegerField(default=0)
    stone_id = models.CharField(max_length=20)
    cert_type = models.CharField(max_length=10)
    cert_no = models.BigIntegerField(default=0,primary_key=True,unique=True)
    carat = models.FloatField(default=0)
    color = models.IntegerField(default=0, choices=COLOR_CHOICES)
    clarity = models.IntegerField(default=0, choices=CLARITY_CHOICES)
    measurement = models.CharField(max_length=30)
    depth = models.FloatField(default=0)
    table = models.FloatField(default=0)
    girdle = models.CharField(max_length=20)
    culet = models.CharField(max_length=10)
    cut = models.CharField(max_length=10)
    pol = models.CharField(max_length=10)
    sym = models.CharField(max_length=10)
    flo = models.CharField(max_length=10)
    hna = models.CharField(max_length=10)
    rapa_price = models.IntegerField(default=0)
    discount_rate = models.FloatField(default=0)
    comment = models.CharField(max_length=100)
    input_date = models.CharField(max_length=7)
    update_date = models.CharField(max_length=7)
    delete_date = models.CharField(max_length=7)
    delete_flag = models.BooleanField(default=False)

    def __str__(self):
        return str(self.cert_no) + " " + str(self.carat) + " " + str(self.rapa_price) + " " + str(self.discount_rate)

    def calculate_price(self):
        return int(self.carat * self.rapa_price * ( 100 - self.discount_rate) / 100)
    
