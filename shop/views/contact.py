from django.http import request
from django.shortcuts import redirect, render
from shop.models.Contact import Contact
from shop.models.Category import Category
from shop.forms.contact import ContactForm
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib import messages
import requests
from shop.models.ImageUser import ImageUser
@csrf_exempt
def contact(request):
    imageview = None
    if request.user.is_authenticated:
         imageview =  ImageUser.objects.get(user=request.user)
    print(imageview.images)
    contacts  =  Contact.objects.filter(is_enabled=True)
    category  =  Category.objects.filter(is_activate = True)
    form_contact = ContactForm()
    if request.method == 'POST':
        payload = {'secret': settings.RECAPTCHA_SECRET_KEY,'response':request.POST['g-recaptcha-response']}
        respone = requests.post('https://www.google.com/recaptcha/api/siteverify',payload)
        if respone.json()['success']:
            form_contact = ContactForm(request.POST)
        
            #check validation
            if form_contact.is_valid():
                print('validated')
                contact=form_contact.save(commit=False)

                contact.save()
                messages.add_message(request, messages.SUCCESS, 'Message sent',"success")
            else:
                 messages.add_message(request, messages.ERROR, 'กรุณากรอกให้ครบ','warning')
            
        else:
            messages.add_message(request, messages.ERROR, 'Recapcha timeout',"danger")

        #reset form
        form_contact = ContactForm()

    context = {
    
        'contacts':contacts,
        'category':category,
        'form_contact':form_contact,
        'imageview':imageview,
    }
    return render(request, 'page/contact.html',context)
