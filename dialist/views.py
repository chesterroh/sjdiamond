from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from .models import Diamond

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
    carat_from = request.GET.get('carat_from')
    carat_to  = request.GET.get('carat_to')
    color_from  = request.GET.get('color_from')
    color_to  = request.GET.get('color_to')
    clarity_from = request.GET.get('clarity_from')
    clarity_to = request.GET.get('clarity_to')

    '''
    diamonds = Diamond.objects.filter(carat__gte=float(carat_from)).filter(carat__lte=float(carat_to))


    diamonds = diamonds.order_by('-carat')

    return render(request,'dialist/search.html', { 'diamonds' : diamonds })
    '''

    return render(request,'dialist/search.html')
