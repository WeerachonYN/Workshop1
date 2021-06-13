from django.http import request
from django.shortcuts import redirect, render
from shop.models.Category import Category
from shop.models.Product import Product
from django.db.models import Q

def category(request,pk):
    category  =  Category.objects.filter(is_activate = True)
    if pk is not None:
        list_product = Product.objects.filter(is_activate = True ).filter(category = pk)
        title  =  Category.objects.filter(is_activate = True).filter(pk=pk)
      
    else:
        list_product = Product.objects.filter(is_activate = True )
     
   
      
       
    context = {
        'category':category,
        'list_product':list_product,
        'title':title
        }
   
    return render(request, 'page/category.html',context)

def search_category(request):
    category  =  Category.objects.filter(is_activate = True)
    list_product = Product.objects.filter(is_activate = True).order_by("-created_datetime")

    search_post = request.GET.get('word')
    if search_post:
        list_product = list_product.filter(Q(name__icontains=search_post))
  
    context = {
         'category':category,
        'list_product':list_product,
        'search_post':search_post,
        }
            
    return render(request, 'page/category.html',context)