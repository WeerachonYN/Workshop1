from django.http import request
from django.shortcuts import redirect, render
from shop.models.Contact import Contact
from shop.forms.contact import ContactForm
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib import messages
import requests

@csrf_exempt
def contact(request):
    contacts  =  Contact.objects.filter(is_enabled=True)
    form_contact = ContactForm()
    if request.method == 'POST':
        payload = {'secret': settings.RECAPTCHA_SECRET_KEY,'response':request.POST['recaptcha_token']}
        respone = requests.post('https://www.google.com/recaptcha/api/siteverify',payload)
        if respone.json()['success']:
            form_contact = ContactForm(request.POST)
        
            #check validation
            if form_contact.is_valid():
                print('validated')
                contact=form_contact.save(commit=False)

                contact.save()
                form_contact = ContactForm()
                messages.add_message(request, messages.SUCCESS, 'Message sent',"success")
            # else:
            #      messages.add_message(request, messages.ERROR, 'กรุณากรอกให้ครบ','warning')
            
        else:
            messages.add_message(request, messages.ERROR, 'Recapcha timeout',"danger")

        #reset form
    # c = Contact.objects.get(pk=1)
    # form_contact = ContactForm()


    context = {
    
        'contacts':contacts,
       
        'form_contact':form_contact,
    }
    return render(request, 'page/contact.html',context)
