from django.http import request
from django.shortcuts import redirect, render
from shop.models.Contact import Contact
from shop.models.Category import Category
from shop.forms.contact import ContactForm
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib import messages

@csrf_exempt
def contact(request):
    contacts  =  Contact.objects.filter(is_enabled=True)
    category  =  Category.objects.filter(is_activate = True)
    form_contact = ContactForm()
    if request.method == 'POST':
        form_contact = ContactForm(request.POST)
        #check validation
        if form_contact.is_valid():
            contact=form_contact.save(commit=False)
            # contact.user = request.user
        contact.save()
        messages.add_message(request, messages.SUCCESS, 'Message sent',"success")
        #reset form
        form_contact = ContactForm()

    context = {
        'contacts':contacts,
        'category':category,
        'form_contact':form_contact,
        'site_key': settings.RECAPTCHA_SITE_KEY,
    }
    return render(request, 'page/contact.html',context)
