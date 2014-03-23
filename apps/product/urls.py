#coding=utf-8
from django.conf.urls import patterns, include, url
from .views import product_productcategory_list,product_product_list

#1.6有变？
#from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
	url(r'^$', product_productcategory_list),
    url(r'^productcategory/$', product_productcategory_list),
    url(r'^product/(?P<id>\d+)$', product_product_list,name="product_product_list"),

)