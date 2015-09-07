from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("This would be the main dia list view page")

def detail(request,diamond_id):
    response = "you're looking at diamond %s."
    return HttpResponse( response % diamond_id )

def results(request,diamond_id):
    response = "You're look the results of diamond %s."
    return HttpResponse( response % diamond_id )


