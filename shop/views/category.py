from django.http import request
from django.shortcuts import redirect, render
from shop.models.Category import Category
from shop.models.Product import Product
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def category(request):

    list_product = Product.objects.filter(is_activate = True )
    counters = None
    
    # search  
    search_post = request.GET.get('search','')
    if search_post:
        list_product = list_product.filter(Q(name__icontains=search_post))
        counters = list_product.count()
  
       
    # sort
    sort = request.GET.get('sort','desc')
    if sort == 'desc':
       list_product = list_product.order_by('price')
       text_sort = 'น้อยไปมาก'
    else:
       list_product = list_product.order_by('-price')
       text_sort = 'มากไปน้อย'
    #  pagination
    paginator = Paginator(list_product, 8)
    page = request.GET.get('page',1)
    try:
        list_product = paginator.page(page)
    except PageNotAnInteger:
        list_product = paginator.page(1)
    except EmptyPage:
        list_product = paginator.page(paginator.num_pages)
   
    context = {
        'list_product':list_product,
         'search_post':search_post,
         'sort':sort,
         'page':page,
         'text_sort':text_sort,
     
            'counters':counters,
     

        }
   
    return render(request, 'page/category.html',context)

def categoryFilter(request,pk):
 
 
    category = Category.objects.filter(is_activate=True)
    list_product = Product.objects.filter(is_activate = True ).filter(category = pk)
    title  =  category.get(pk=pk)
    counters = None
      # search  
    search_post = request.GET.get('search','')
        
    if search_post:
        list_product = list_product.filter(Q(name__icontains=search_post))
        counters = list_product.count()
    
    #sort
    sort = request.GET.get('sort','desc')
    if sort == 'desc':
       list_product = list_product.order_by('price')
       text_sort = 'น้อยไปมาก'
    else:
       list_product = list_product.order_by('-price')
       text_sort = 'มากไปน้อย'
   #  pagination
    paginator = Paginator(list_product,8)
    page = request.GET.get('page','1')
    try:
        list_product = paginator.page(page)
    except PageNotAnInteger:
        list_product = paginator.page(1)
    except EmptyPage:
        list_product = paginator.page(paginator.num_pages)
    # pages=list_product.paginator.page_range
  
    context = {
        'list_product':list_product,
        'title':title,
        'page':page,
        'search_post':search_post,
        'text_sort':text_sort,
         'sort':sort,
         'pk':pk,
        'counters':counters,
        }
   
    return render(request, 'page/category.html',context)
