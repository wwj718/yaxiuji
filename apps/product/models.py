#coding=utf-8
from django.db import models
from sorl.thumbnail import ImageField


# Create your models here.

class ProductCategory(models.Model):
	'''建一个模型,每次编辑'''
	name = models.CharField(max_length=40, verbose_name=u'分类名称')
	#order = models.IntegerField(default=0, verbose_name=u'图片顺序')
	pic =  ImageField(blank=True,upload_to='ProductCategory', verbose_name=u'图片')
	content = models.CharField(max_length=200, verbose_name=u'内容')
	create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
	update_time = models.DateTimeField(u'更新时间', auto_now=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['-create_time']
		verbose_name_plural = verbose_name = u"产品分类"



class Product(models.Model):
	#使用cycle打出column1,column1,column1
	'''建一个模型,每次编辑'''
	name = models.CharField(max_length=40, verbose_name=u'产品名称')
	category = models.ForeignKey(ProductCategory, verbose_name=u'产品类型')
	#order = models.IntegerField(default=0, verbose_name=u'图片顺序')
	content = models.CharField(max_length=200, verbose_name=u'内容')
	pic =  ImageField(blank=True,upload_to='Product', verbose_name=u'图片')
	price =  models.IntegerField(blank=True)
	create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
	update_time = models.DateTimeField(u'更新时间', auto_now=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['-create_time']
		verbose_name_plural = verbose_name = u"产品"


