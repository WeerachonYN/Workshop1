from django.http import request
from django.shortcuts import redirect, render
from shop.models.Contact import Contact
from shop.models.Category import Category
def contact(request):
    contacts  =  Contact.objects.filter(is_enabled=True)
    category  =  Category.objects.filter(is_activate = True)

    context = {
        'contacts':contacts,
        'category':category,
    }
    return render(request, 'page/contact.html',context)
