from django.contrib import messages
from django.shortcuts import redirect,render
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.views.decorators.csrf import csrf_exempt
from shop.forms.users.signups import SignupForm 
from django.conf import settings
import requests


@csrf_exempt
def signupView(request):
    form_signup = SignupForm()

    # Submit Signup
    if request.method == "POST":
        payload = {'secret': settings.RECAPTCHA_SECRET_KEY,'response':request.POST['recaptcha_token_signUp']}
        respone = requests.post('https://www.google.com/recaptcha/api/siteverify',payload)
        if respone.json()['success']:
            form_signup = SignupForm(request.POST)
        

            # Check validation 
            if form_signup.is_valid() :
                # Save comment
                form_signup.save()
                username = form_signup.cleaned_data.get('username')
                raw_password = form_signup.cleaned_data.get('password1')
                # image_form.user = username
                # image_form.save()
                user = authenticate(username=username, password=raw_password)

                # auto login
                login(request, user)
                
                messages.add_message(request, messages.SUCCESS,'Sign Up Success!!',"success")

                response = redirect('home')
                return response
        else:
           messages.add_message(request, messages.ERROR, 'Recapcha timeout',"danger") 
 
    # Contexts
    context = {
        'form_signup' : form_signup,
     
     
    }
    return render(request, 'page/auth/signup.html',context)

