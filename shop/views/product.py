from django.http import request
from django.shortcuts import redirect, render
from shop.models.Product import Product
from shop.models.Category import Category
from shop.models.ImageProduct import ImageProduct
def product(request,pk):
    products  =  Product.objects.filter(pk=pk)
    images = ImageProduct.objects.filter(product=pk)
    category  =  Category.objects.filter(is_activate = True)

    context = {
        'products':products,
        'category':category,
        'images':images
    }
    print(product)
    print(images)

    return render(request, 'page/product.html',context)
