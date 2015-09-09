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

    carat_from = request.POST["from_carat"]
    carat_to = request.POST["to_carat"]
    
    response = "You're look the results of diamond %s to %s"
    return HttpResponse( response % ( carat_from, carat_to))






