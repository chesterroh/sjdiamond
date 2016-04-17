from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from .models import Diamond

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
                  'Z' :  8
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

# Create your views here.

def index(request):
    paginator = Paginator(Diamond.objects.filter(delete_flag=False).order_by('-carat'),100)
    page = request.GET.get('page')

    try:
        diamonds = paginator.page(page)
    except PageNotAnInteger:
        diamonds = paginator.page(1)
    except EmptyPage:
        diamonds = paginator.page(paginator.num_pages)

    return render(request,'dialist/index.html',{ 'diamond_list' : diamonds })


def detail(request,cert_no):
    diamond = get_object_or_404(Diamond,pk=cert_no)
    return render(request,'dialist/detail.html',{ 'dia' : diamond })



def stockupdate(request,check_date):
    c_dia = Diamond.objects.filter(input_date=check_date).order_by('-carat')
    d_dia = Diamond.objects.filter(delete_date=check_date).order_by('-carat')
    return render(request,'dialist/stockupdate.html', { 'c_dia' : c_dia , 'd_dia' : d_dia, 'check_date' : check_date })



def search(request):

    cut_ex_flag = False
    flo_non_flag = False
    price_order_flag = False

    error_messages = []
    
    carat_from = request.GET.get('carat_from')
    carat_to  = request.GET.get('carat_to')
    
    color_from  = request.GET.get('color_from')
    color_to  = request.GET.get('color_to')
    
    clarity_from = request.GET.get('clarity_from')
    clarity_to = request.GET.get('clarity_to')

    cut_flag = request.GET.get('cut_flag')
    flo_flag = request.GET.get('flo_flag')
    price_flag = request.GET.get('price_flag')

    if carat_from == None:
        return render(request,'dialist/search.html')

    '''
    Convert the values to integer 
    We'll apply try-catch to the following block
    '''

    num_carat_from = float(carat_from)
    num_carat_to = float(carat_to)

    num_color_from = COLOR_CHOICES[color_from]
    num_color_to = COLOR_CHOICES[color_to]

    num_clarity_from = CLARITY_CHOICES[clarity_from]
    num_clarity_to = CLARITY_CHOICES[clarity_to]

    if cut_flag == "True":
        cut_ex_flag = True

    if flo_flag == "None":
        flo_non_flag = True

    if price_flag == "True":
        price_order_flag = True
            

    if num_carat_from > num_carat_to:
        error_messages.append("CARAT FROM-TO RANGE ERROR")

    if num_color_from < num_color_to:
        error_messages.append("COLOR FROM-TO RANGE ERROR")

    if num_clarity_from < num_clarity_to:
        error_messages.append("CLARITY FROM-TO RANGE ERROR")
        
    
    if error_messages:
        return render(request,'dialist/search.html', { 'error_messages' : error_messages })

    else:

        diamonds = Diamond.objects.filter(carat__lte=num_carat_to).filter(carat__gte=num_carat_from).filter(color__lte=num_color_from).filter(color__gte=num_color_to).filter(clarity__lte=num_clarity_from).filter(clarity__gte=num_clarity_to)

        if flo_non_flag == True:
            diamonds = diamonds.filter(flo='NON')

        if cut_ex_flag == True:
            diamonds = diamonds.filter(cut='EX')

        if price_order_flag == True:
            diamonds = diamonds.order_by('-consumer_price')

        return render(request,'dialist/search.html',{ 'diamonds' : diamonds })

