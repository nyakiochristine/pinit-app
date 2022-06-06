from django import forms
from .models import Profiles,Comment,Images
from django.contrib.auth.forms import AuthentificationForm



class LoginForm(AuthentificationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'
                                                            'placeholder':'Username'}))
    
    
password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'
                                                        'placeholder':'Password'}))

class PostImageForm(forms.ModelForm):
    image =forms.ImageField()
    captions = forms.CharField(max_length=200)
    
    class Meta:
        models = Images
        exclude = ('posted','profile')
        
        
class  PostCommentForm(forms.ModelForm):
    class Meta:
        models = Comment
        exclude = ('image','posted','user')
    
    
class PostProfileForm(forms.ModelForm):
    class Meta:
        models = Profiles
        exclude = ['user',]