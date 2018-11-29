#from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('trend/$', views.index, name='index'),
    url('tweets/$', views.tweets, name='tweets'),
    url('today/', views.today, name='today'),
    url('tweetsall/', views.tweetsall, name='tweetsall'),
    url(r'^test/$',views.getdata)
]
