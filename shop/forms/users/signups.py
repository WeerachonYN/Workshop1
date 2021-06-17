from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignupForm(UserCreationForm):

    password1 = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control','type': 'password'}))
    password2 = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control','type': 'password'}))
    email = forms.EmailField(max_length=254, required=True,widget=forms.TextInput(attrs={'class': 'form-control','type':'email'}))
    first_name = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username',  'password1', 'password2','email','first_name','last_name']
          
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control'})

                                