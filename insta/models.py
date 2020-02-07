from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    '''
    Class containing user profile details
    '''
    profie_photo=models.ImageField(upload_to='images/',blank=True)
    bio=models.CharField(max_length=100)
    editor=models.ForeignKey(User,on_delete=models.CASCADE)

class Image(models.Model):
    image=models.ImageField(upload_to='images/',blank=True)
    image_name=models.CharField(max_length=30)
    image_caption=models.CharField(max_length=100)
    editor=models.ForeignKey(User,on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile,null=True)
    likes=models.ManyToManyField(User,related_name="likes",blank=True)
    followers=models.ManyToManyField(User,related_name="followers",blank=True)
    pub_date=models.DateTimeField(auto_now_add=True)