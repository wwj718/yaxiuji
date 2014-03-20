#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import HomePic

# Create your views here.
def hello(request):
	return HttpResponse("hello home")

def index(request):
    """
    """
    return render_to_response('index.html',{},RequestContext(request))

def yaxiuji(request):
	pic_list = HomePic.objects.all().order_by("-create_time")

	return render_to_response('yaxiuji.htm',{"pic_list":pic_list},RequestContext(request))
