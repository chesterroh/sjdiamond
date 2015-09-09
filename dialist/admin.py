from django.contrib import admin
from .models import Diamond

class DiamondAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Input Date', { 'fields' : ['input_date'], 'classes' : ['collapse'] }),
        (None, { 'fields' : ['cert_no'] }),
        (None, { 'fields' : ['carat'] }),
        (None, { 'fields' : ['color'] }),
        (None, { 'fields' : ['clarity'] }),
        (None, { 'fields' : ['cut'] }),
        (None, { 'fields' : ['pol'] }),
        (None, { 'fields' : ['sym'] }),
        (None, { 'fields' : ['flo'] }),
        (None, { 'fields' : ['rapa_price'] }),
        (None, { 'fields' : ['discount_rate'] }),
        (None, { 'fields' : ['comment'] }),
        ]
    list_display = ( 'cert_no', 'carat' , 'color', 'clarity', 'cut', 'pol', 'sym' , 'flo', 'rapa_price' , 'discount_rate' )
    list_filter = ['carat']
    search_fields = [ 'carat' ]
               
admin.site.register(Diamond,DiamondAdmin)
