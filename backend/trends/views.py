from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import permissions
from trends.models import *
from django.core import serializers
import json
import sys
import datetime
import urllib.parse
# Create your views here.


@api_view(['GET'])
def index(request):
    dat=request.GET.get('date')
    results=TweetSearchTable.objects.filter(tdate=dat)
    results =json.loads(serializers.serialize('json', results))
    results1=[]
    i=0
    for i in range(len(results)):
        results1.append(results[i]['fields'])
    results=json.dumps(results1)
    results=json.loads(results)
    results1={}
    results1['data']=results
    return Response(results1)

@api_view(['GET'])
def today(request):
    now = datetime.datetime.now()
    tdate=str(now.year)+"-"+str('%02d' % now.month)+"-"+str('%02d' % now.day)
    print(tdate)
    results=TweetSearchTable.objects.filter(tdate="2018-05-20")
    results =json.loads(serializers.serialize('json', results))
    results1=[]
    i=0
    for i in range(len(results)):
        results1.append(results[i]['fields'])
    results=json.dumps(results1)
    results=json.loads(results)
    results1={}
    results1['data']=results
    return Response(results1)

@api_view(['GET'])
def tweets(request):
    a=request.GET.get('query')
    print(a)
   # aa=urllib.parse.quote_plus(a)
    #print(aa)
    results=ReplayTable.objects.filter(uname=a)
    results =json.loads(serializers.serialize('json', results))
    i=0
    results1=[]
    for i in range(len(results)):
        results1.append(results[i]['fields'])
    results=json.dumps(results1)
    results=json.loads(results)
    results1={}
    results1['data']=results
    return Response(results1)

@api_view(['GET'])
def tweetsall(request):
    results=TweetSearchTable.objects.all()
    results =json.loads(serializers.serialize('json', results))
    i=0
    results1=[]
    for i in range(len(results)):
        results1.append(results[i]['fields'])
    results=json.dumps(results1)
    results=json.loads(results)
    results1={}
    results1['data']=results
    return Response(results1)


def getdata(request):
    results=ReplayTable.objects.filter(uname="impradeepmachi")
    results =json.loads(serializers.serialize('json', results))
    results1=[]
    i=0
    for i in range(len(results)):
        results1.append(results[i]['fields'])
    #results1['data']=results
    return HttpResponse(results)



