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

    error_messages = []
    
    carat_from = request.GET.get('carat_from')
    carat_to  = request.GET.get('carat_to')
    
    color_from  = request.GET.get('color_from')
    color_to  = request.GET.get('color_to')
    
    clarity_from = request.GET.get('clarity_from')
    clarity_to = request.GET.get('clarity_to')

    cut_flag = request.GET.get('cut_flag')
    flo_flag = request.GET.get('flo_flag')



    if error_messages:
        return render(request,'dialist/search.html', { 'error_messages' : error_messages })

    else:
        '''
        Try to query the DB
        '''

        return render(request,'dialist/search.html')

    '''
    diamonds = Diamond.objects.filter(carat__gte=float(carat_from)).filter(carat__lte=float(carat_to))


    diamonds = diamonds.order_by('-carat')

    return render(request,'dialist/search.html', { 'diamonds' : diamonds })
    '''
