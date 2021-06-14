from django.http import request
from django.shortcuts import redirect, render
from shop.models.Category import Category
from shop.models.Product import Product


def homepage(request):
    category  =  Category.objects.filter(is_activate = True)
    list_products = Product.objects.filter(is_activate = True)
    context = {
        'list_products':list_products,
        'category':category,

    }
    return render(request, 'page/index.html',context)
