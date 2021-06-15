from django.http import request
from django.shortcuts import redirect, render
from shop.models.Product import Product
from shop.models.Category import Category
from shop.models.ImageProduct import ImageProduct

def product(request,pk,cat_id):
    products  =  Product.objects.get(pk=pk)
    images = ImageProduct.objects.filter(product=pk)
    category  =  Category.objects.filter(is_activate = True)
    title  =  category.get(name=products.category)
    # link_breadcromb = category.filter(pk = pk.category)

    context = {
        'products':products,
        'category':category,
        'images':images,
        'title':title,
    }
    # print(link_breadcromb)
    print(products)

    return render(request, 'page/product.html',context)
