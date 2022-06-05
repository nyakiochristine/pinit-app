from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import  User



# Create your models here.
#classes:profile,images, commenting

class Profile(models.Model):
    bio = models.CharField(max_length=200)
    image =models.ImageField(blank=True)
    user =models.OneToOneField(User,ondelete=models.CASCADE, primary_key=True)