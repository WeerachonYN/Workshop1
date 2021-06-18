from django.contrib import messages
from django.shortcuts import redirect,render
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from shop.forms.users.signins import SignInForm
from shop.models.Category import Category


def signInView(request):

    category  =  Category.objects.filter(is_activate = True)
    form_signIn = SignInForm()
    if request.method=="POST":

        form_signIn = SignInForm(request.POST)
        # print (form_signIn)
        #check validation
        if form_signIn.is_valid():

       
        # check login
            username = form_signIn.cleaned_data['username']
            password = form_signIn.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
     
        # login success
            if user is not None:

                login(request,user)
                response = redirect('home')
                return response
            else:
                messages.add_message(request,messages.ERROR,'Wrong password!',"danger")
    
    context = {
   
        'category':category,
        'form_signIn' : form_signIn
    }

    return render(request, 'page/include/signin.html',{'form_signIn' : form_signIn})            