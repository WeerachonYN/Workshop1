from django.http import request
from django.shortcuts import redirect, render
from shop.models.Category import Category
from shop.models.Product import Product

def category(request,pk):
    category  =  Category.objects.filter(is_activate = True)
    if pk is not None:
        list_product = Product.objects.filter(is_activate = True ).filter(category = pk)
        title  =  Category.objects.filter(is_activate = True).filter(pk=pk)
    else:
        list_product = Product.objects.filter(is_activate = True)
        title = 'Category'
       
    context = {
        'category':category,
        'list_product':list_product,
        'title':title
        }
  
    return render(request, 'page/category.html',context)
