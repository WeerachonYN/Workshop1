from django.http import request
from django.shortcuts import redirect, render

def homepage(request):
    
    return render(request, 'page/index.html')
