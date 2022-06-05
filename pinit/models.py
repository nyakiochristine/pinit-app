from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import  User



# Create your models here.
#classes:profile,images, commenting

class Profile(models.Model):
    bio = models.CharField(max_length=200)
    image =models.ImageField(blank=True)
    user =models.OneToOneField(User,ondelete=models.CASCADE, primary_key=True)
    
    


class Images(models.Model):
    image = models.ImageField(blank=True)
    captions = models.CharField(max_length=120)
    posted = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User,ondelete=models.CASCADE)
    
    
    
class Comment(models.Model):
    comment = models.CharField(max_length=100)
    posted = models.DateTimeField(auto_now_add =True)
    image = models.ForeignKey(Images,ondelete=models.CASCADE)
    user = models.ForeignKey(User,ondelete=models.CASCADE)