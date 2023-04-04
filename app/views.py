from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def insert_topic(request):
    To=input('enter topic_name')
    to=Topic.objects.get_or_create(topic_name=To)[0]
    to.save()
    return HttpResponse('topic is successfully register')
def insert_webpage(request):
    co=input('enter a topic_name')
    l1=input('enter a name')
    url=input('enter a url')
    tt=Topic.objects.get_or_create(topic_name=co)[0]
    tt.save()
    c1=Webpages.objects.get_or_create(topic_name=tt,name=l1,url=url)[0]
    c1.save()
    return HttpResponse('webpage is successfully resgister')
def insert_AccessRecord(request):
    ao=input('enter a topic_name')
    m1=input('enter a name')
    url=input('enter a u url')
    n1=input('enter author name')
    n2=input('enter a date ')
    ll=Topic.objects.get_or_create(topic_name=ao)[0]
    ll.save()
    l2=Webpages.objects.get_or_create(topic_name=ll,name=m1,url=url)[0]
    l2.save()
    l3=AccessRecords.objects.get_or_create(name=l2,author=n1,date=n2)[0]
    return HttpResponse('Accesss record is successfully')
    