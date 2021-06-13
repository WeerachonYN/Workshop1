from django.http import request
from django.shortcuts import redirect, render
from shop.models.Product import Product
from shop.models.Category import Category

def product(request):
    products  =  Product.objects.filter(is_activate = True)
    category  =  Category.objects.filter(is_activate = True)

    context = {
        'products':products,
        'category':category,
    }
    return render(request, 'page/product.html',context)
