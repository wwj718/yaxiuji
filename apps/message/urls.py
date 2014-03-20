#coding=utf-8
from django.conf.urls import patterns, include, url
from .views import hello,message_create
from django.shortcuts import get_object_or_404



urlpatterns = patterns('',
    url(r'^hello$',hello),
    url(r'^$' , message_create, name='message_create'),
)

