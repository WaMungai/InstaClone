from django.test import TestCase
from .models import Profile,Image
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.newuser=User(username='jayb')
        self.newuser.save()
        self.biography=Profile(profile_photo='pic.jpg',bio='treats',editor=self.newuser)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.biography,Profile))
        
    def test_save_method(self):
        self.biography.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)
        
    def test_delete_method(self):
        self.biography.save_profile()
        self.biography.delete_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)==0)
        
    def test_get_profile(self):
        self.biography.save_profile()
        firstprofile=Profile.get_profile()
        self.assertTrue(firstprofile is not None)
    
class ImageTestClass(TestCase):
    def setUp(self):
        self.newuser=User(username='jayb')
        self.newuser.save()
        self.images=Image(image='img.jpg',image_name='cars',image_caption='fastcars',editor=self.newuser)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.images,Image))
     
    def test_save_image(self):
        self.images.save_image()
        allimages=Image.objects.all()
        self.assertTrue(len(allimages)>0)
        
    def test_delete_image(self):
        self.images.save_image()
        self.images.delete_image()
        allimages=Image.objects.all()
        self.assertTrue(len(allimages)==0)
        
    def test_get_images(self):
        self.images.save_image()
        secondimage=Image.get_images()
        self.assertTrue(secondimage is not None)