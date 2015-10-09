from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<cert_no>[0-9]+)/$', views.detail, name='detail'),
    url(r'^search/results/$', views.results, name='results'),
    url(r'^search/$', views.search, name='search'),
    ]
