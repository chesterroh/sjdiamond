from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from .models import Diamond

# Create your views here.

def index(request):
    paginator = Paginator(Diamond.objects.all(),500)
    page = request.GET.get('page')

    try:
        diamonds = paginator.page(page)
    except PageNotAnInteger:
        diamonds = paginator.page(1)
    except EmptyPage:
        diamonds = paginator.page(paginator.num_pages)

    return render(request,'dialist/index.html',{ 'diamond_list' : diamonds })



def detail(request,diamond_id):
    diamond = get_object_or_404(Diamond,pk=diamond_id)
    return render(request,'dialist/detail.html',{ 'diamond' : diamond })



def search(request):
    return render(request,'dialist/search.html')



def results(request):
    from_carat = request.GET.get('from_carat')
    to_carat = request.GET.get('to_carat')
    color = request.GET.get('color')
    clarity = request.GET.get('clarity')

    diamonds = Diamond.objects.filter(carat__gte=float(from_carat)).filter(carat__lte=float(to_carat))

    diamonds = diamonds.filter(color__startswith=color).filter(clarity__startswith=clarity)

    diamonds = diamonds.order_by('carat')

    return render(request,'dialist/results.html', { 'diamonds' : diamonds })
