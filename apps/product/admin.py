#coding:utf-8
from django.contrib import admin
#from django.contrib.markup.templatetags.markup import restructuredtext

from .models import Product,ProductCategory

from sorl.thumbnail.admin import AdminImageMixin
from sorl.thumbnail import get_thumbnail

    
class ProductAdmin(admin.ModelAdmin,AdminImageMixin):

    search_fields = ('name',)
    fields = ('name',"category", 'pic','price')
    list_display = ('image_thumbnail','name', 'pic', 'create_time')
    ordering = ('create_time', )

    def image_thumbnail(self, obj):
        '''缩略图'''
        im = get_thumbnail(obj.pic, '80x80', quality=99)
        return u"<img src='/media/%s' />" % im
    image_thumbnail.allow_tags = True
    #save_on_top = True

class ProductCategoryAdmin(admin.ModelAdmin,AdminImageMixin):

    search_fields = ('name',)
    fields = ('name', 'pic',"content")
    list_display = ('image_thumbnail','name', 'pic', 'create_time')
    ordering = ('create_time', )

    def image_thumbnail(self, obj):
        '''缩略图'''
        im = get_thumbnail(obj.pic, '80x80', quality=99)
        return u"<img src='/media/%s' />" % im
    image_thumbnail.allow_tags = True


    # def save_model(self, request, obj, form, change):
    #    '''在此提取'''
    #     #obj.author = request.user
    #     if not obj.summary:
    #          obj.summary = obj.content_html
    #     # if not obj.is_old:
    #     #     obj.content_html = restructuredtext(obj.content)
    #     else:
    #         obj.content_html = obj.content_html.replace('\r\n', '<br/>')
    #         import re
    #         obj.content_html = re.sub(r"\[cc lang='\w+?'\]", '<pre>', obj.content_html)
    #         obj.content_html = obj.content_html.replace('[/cc]', '</pre>')
    #     obj.save()

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)


