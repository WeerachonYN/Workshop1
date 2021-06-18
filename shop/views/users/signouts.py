from django.contrib import messages
from django.shortcuts import redirect,render
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def signouts(request):
    logout(request)
    messages.info(request, "Logged out Successfully!")
    return redirect("signin")