#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product,ProductCategory
from django.shortcuts import get_object_or_404

# Create your views here.
def hello(request):
	return HttpResponse("hello home")

def product_productcategory_list(request,template_name='productcategory.htm'):
    """
    Returns a news detail page.
    """
    productcategory_list = ProductCategory.objects.all()
    return render(request, template_name, {
        'productcategory_list': productcategory_list,
    })

def product_product_list(request,id,template_name='product.htm'):
    """
    Returns a news detail page.
    """
    category = get_object_or_404(ProductCategory,id=int(id))
    product_list = Product.objects.filter(category=category)
    return render(request, template_name, {
        'product_list': product_list,
    })