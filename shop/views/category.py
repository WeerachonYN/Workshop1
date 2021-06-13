from django.http import request
from django.shortcuts import redirect, render
from shop.models.Category import Category

def category(request):
    categorys  =  Category.objects.filter(is_activate = True)
    context = {
        {'categorys':categorys}
    }
    return render(request, 'page/category.html',context)
