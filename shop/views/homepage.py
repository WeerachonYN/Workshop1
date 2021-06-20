from django.http import request
from django.shortcuts import redirect, render
from shop.models.Category import Category
from shop.models.Product import Product


def homepage(request):

    category = Category.objects.filter(is_activate=True)
    category  =  category.order_by('name')
    list_products = Product.objects.filter(is_activate = True)
    recomment = Product.objects.filter(is_activate=True).filter(is_recomment=True).order_by('price')[:8]
    context = {
        'list_products':list_products,
        'category':category,
        'list_product':recomment,


    }
    return render(request, 'page/index.html',context)
