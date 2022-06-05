from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import  User



# Create your models here.
#classes:profile,images, commenting

class Profiles(models.Model):
    bio = models.CharField(max_length=200)
    image =models.ImageField(blank=True)
    user =models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    
    
    #class methods
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
            
    @classmethod
    def get_profile_by_name(cls, search_term):
        profile  = cls.objects.filter(user__username__icontains=search_term)
        return profile
    
    @classmethod
    def get_profile_by_id(self, id):
        profile = cls.objects.get(user=id)
        return profile
    
    
    @classmethod
    def filter_profile_by_id(self,id):
        profile = Profiles.objects.filter(user=id).first()
        return profile
    
    
        
        
    
    


class Images(models.Model):
    image = models.ImageField(blank=True)
    captions = models.CharField(max_length=120)
    posted = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    
    #class menthods
    class Meta:
        ordering =('-posted',)
        
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
    
    
    @classmethod  
    def get_image_by_id(cls,id):
        image = Images.objects.get(pk=id)
        return image
    
    @classmethod
    def get_profile_images(cls,profile):
        images = Images.objects.filter(profile__pk= profile)
        return images
    @classmethod
    def get_all_images(cls):
        images = Images.objects.all()
        return images 
    
    
        
    
    
    
class Comment(models.Model):
    comment = models.CharField(max_length=100)
    posted = models.DateTimeField(auto_now_add =True)
    image = models.ForeignKey(Images,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    #class methods'
    def save_comment(self):
        self.save()
        
        
    def delete_comment(self):
        self.delete()
        
        
    @classmethod
    def get_comment_by_image(cls, id):
        comment = Comment.objects.filter(image_pk=id)
        return comment