from django.forms import ModelForm
from django import forms
from shop.models.Contact import Contact


class ContactForm(ModelForm):
    email = forms.EmailField(max_length=254, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    messages = forms.CharField(max_length=255,required=True)
    # recaptcha_token
    class Meta:
        model = Contact
        fields = ['email','first_name','last_name','messages']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #css
        self.fields['email'].widget=forms.TextInput(attrs={'class': 'form-control','type':'email'})
        self.fields['first_name'].widget=forms.TextInput(attrs={'class': 'form-control',})
        self.fields['last_name'].widget=forms.TextInput(attrs={'class': 'form-control'})
        self.fields['messages'].widget=forms.Textarea(attrs={'class':'form-control'})