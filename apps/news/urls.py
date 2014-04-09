#coding=utf-8
from django.conf.urls import patterns, include, url
from .views import hello,news_news_details,news_news_list,news_news_search,news_by_category
from django.shortcuts import get_object_or_404


NEWS_URL = r'(?P<id>\d+)'

urlpatterns = patterns('',
    url(r'^$',news_news_list),
    url(r'^%s$' % NEWS_URL, news_news_details, name='news_news_details'),
    url(r'^list$' , news_news_list, name='news_news_list'),
    url(r'^search$' , news_news_search, name='news_news_search'),
    url(r'^category/(?P<id>\d+)$' , news_by_category, name='news_by_category'),


)

