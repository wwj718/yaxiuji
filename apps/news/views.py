#coding:utf-8

# Create your views here.
from .models import News,NewsCategory
from django.http import HttpResponse
from django.shortcuts import render


#from django.views.generic import list_detail
from django.shortcuts import get_object_or_404
#django.views.generic.list.ListView

def hello(request):
    return HttpResponse("Hello news")	

def news_news_details(request,id,template_name='news_details.htm'):
    """
    Returns a news list page.
    """
    news = get_object_or_404(News, id=int(id))
    category = NewsCategory.objects.all()
    return render(request, template_name, {
        'news': news,
        'category':category,
    })


def news_news_list(request,template_name='news_all.htm'):
    """
    Returns a news detail page.
    """
    news_list = News.objects.all()
    category = NewsCategory.objects.all()
    return render(request, template_name, {
        'news_list': news_list,
        'category':category,
    })

def news_news_search(request,template_name='news_all.htm'):
    """
    Returns a news detail page.
    """
    title = request.GET.get("q",'')
    category = NewsCategory.objects.all()
    news_list = News.objects.filter(title__icontains=title)
    return render(request, template_name, {
        'news_list': news_list,
        'category':category,
    })

def news_by_category(request,id,template_name='news_all.htm'):
    """
    Returns a news detail page.
    """
    category=get_object_or_404(NewsCategory,id=int(id))
    news_list = News.objects.filter(category=category)
    return render(request, template_name, {
        'news_list': news_list,
        'category':category,
    })
