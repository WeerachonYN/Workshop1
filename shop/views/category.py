from django.http import request
from django.shortcuts import redirect, render
from shop.models.Category import Category
from shop.models.Product import Product
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def category(request):
    category  =  Category.objects.filter(is_activate = True)
    list_products = Product.objects.filter(is_activate = True )
    
    # search  
    search_post = request.GET.get('search','')
    if search_post:
        list_products = list_products.filter(Q(name__icontains=search_post))
    # sort
    sort = request.GET.get('sort','asc')
    if sort == 'desc':
       list_product = list_products.order_by('price')
    else:
       list_product = list_products.order_by('-price')

    #  pagination
    paginator = Paginator(list_product, 6)
    page = request.GET.get('page',1)
    try:
        list_product = paginator.page(page)
    except PageNotAnInteger:
        list_product = paginator.page(1)
    except EmptyPage:
        list_product = paginator.page(paginator.num_pages)
   
    context = {
        'category':category,
        'list_product':list_product,
         'search_post':search_post,
         'sort':sort,
         'page':page,
        }
   
    return render(request, 'page/category.html',context)

def categoryFilter(request,pk):
    category = Category.objects.filter(is_activate=True)
    list_product = Product.objects.filter(is_activate = True ).filter(category = pk)
    title  =  category.get(pk=pk)
    # counter = Product.objects.filter(is_activate=True).filter()
    # (category__id=category)
   
   #  pagination
    paginator = Paginator(list_product, 6)
    page = request.GET.get('page',1)
    try:
        list_product = paginator.page(page)
    except PageNotAnInteger:
        list_product = paginator.page(1)
    except EmptyPage:
        list_product = paginator.page(paginator.num_pages)
    # pages=list_product.paginator.page_range
 
    print(page)
    context = {
        'category':category,
        'list_product':list_product,
        'title':title,
        'page':page,
 
        # 'counter':counter,
        }
   
    return render(request, 'page/category.html',context)
