from django import forms
from django.contrib.auth.models import User
from registration.models import Registration
from django.utils import timezone


class RegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    #name=forms.CharField(max_length=50)
    email=forms.EmailField(required=True)
    #last_login=forms.DateField()
    class Meta:
        model= User
        fields=['last_name','username', 'email', 'password']
