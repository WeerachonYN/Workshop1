from django.contrib import messages
from django.shortcuts import redirect,render
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.views.decorators.csrf import csrf_exempt
from shop.forms.users.signups import SignupForm
@csrf_exempt
def signupView(request):
    form_signup = SignupForm()
    # Submit Signup
    if request.method == "POST":

        form_signup = SignupForm(request.POST)

        # Check validation 
        if form_signup.is_valid():

            form_signup.save()
            username = form_signup.cleaned_data.get('username')
            raw_password = form_signup.cleaned_data.get('password1')
            
            user = authenticate(username=username, password=raw_password)

            # auto login
            login(request, user)
            response = redirect('home')
            return response
       
    # Contexts
    context = {
        'form_signup' : form_signup
    }
    return render(request, 'page/include/signup.html',context)

