from django import forms
from .models import Profile,Comment,Images
from django.contrib.auth.forms import AuthentificationForm


class LoginForm(AuthentificationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'
                                                            'placeholder':'Username'}))
    
    
password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'
                                                        'placeholder':'Password'}))