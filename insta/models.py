from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    '''
    Class containing user profile details
    '''
    profie_photo=models
