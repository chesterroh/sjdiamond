from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<cert_no>[0-9]+)/$', views.detail, name='detail'),
    url(r'^stockupdate/(?P<check_date>[0-9]+)/$', views.stockupdate, name='stockupdate'),
    url(r'^search/$', views.search, name='search'),
    ]
