from django import forms
from django.contrib.auth.models import User

class UpdateProfileForm(forms.ModelForm):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control','type':'email'}))
    first_name = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
