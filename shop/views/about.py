from django.http import request
from django.shortcuts import redirect, render
from shop.models.Category import Category

def about(request):
    category  =  Category.objects.filter(is_activate = True)
    context ={
    'category':category}
    return render(request, 'page/about.html',context)
