from django.test import TestCase
from .models import Profiles,Comment,Images
import datetime as dt
from django.contrib.auth.models import  User


# Create your tests here.

class ProfilesTestClass(TestCase):
    def setUp(self):
        self.user = User(username="kris", email="chrismwangi@gmail.com",password="charlie")
        self.user.save()
        self.profile = Profile(bio="I am awesome",image="http://",user=self.user)
        self.profile.save()
        
    def test_instance(self):
        self.asssertTrue(self.profile.Profiles)
        
    def test_save_method(self):
        profile =Profiles.objects.all()
        self.assertTrue(len(profile) > 0)
        
        
    def test_delete_method(self):
        self.profile.delete_profile()
        profile = Profiles.objects.all()
        self.assertTrue(len(profile) == 0)
        
    def tearDown(self):
        Images.objects.all().delete()
        
class ImagesTestCase(TestCase):
    def setUp(self):
        self.image = Images(image='/pic1',captions:"testing this class", profile=self.user,dateposted='05/06/2022')
        self.image.save()
        
    def tearDown(self):
        Images.objects.all().delete()
        
class CommentTestCase(TestCase):
    def setUp(self):
        self.comment = Comment(comment='test comment', image='/pic',user=self.user,posted=auto_now())
        
    
    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comments))
        
    
    def test_save_method(self):
        comment=Comment.objects.all()
        self.assertTrue(len(comment) > 0)
        
        
    def test_delete_method(self):
        self.comment.delete_comment()
        comment= Comment.objects.all()
        self.assertTrue(len(comment) == 0)
        
        
        
    def tearDown(self):
            Comments.objects.all().delete()

    
        
        
