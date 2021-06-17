from django import forms

class SignInForm(forms.Form):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control','type': 'password'}))

