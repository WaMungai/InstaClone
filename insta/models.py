from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    '''
    Class containing user profile details
    '''
    
    profile_photo=models.ImageField(upload_to='images/',blank=True)
    bio=models.CharField(max_length=100)
    editor=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.bio
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
        
    @classmethod
    def get_profile(cls):
        profile=cls.objects.all()
        return profile

class Image(models.Model):
    image=models.ImageField(upload_to='images/',blank=True)
    image_name=models.CharField(max_length=30)
    image_caption=models.CharField(max_length=100)
    editor=models.ForeignKey(User,on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile,null=True)
    likes=models.ManyToManyField(User,related_name="likes",blank=True)
    followers=models.ManyToManyField(User,related_name="followers",blank=True)
    pub_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    @classmethod
    def get_images(cls):
        image=cls.objects.all()
        return image
    
    @classmethod
    def search_by_category(cls,category):
        category_result=cls.objects.filter(image_name__icontains=category)
        return category_result
        
class Comments(models.Model):
    detail=HTMLField()
    editor=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    image_foreign=models.ForeignKey(Image,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.detail
    
    def save_comment(self):
        self.save()
        
    def delete_comment(self):
        self.delete()
        
    @classmethod
    def get_comments(cls):
        comment=cls.objects.all()
        return comment
    
class NewsLetterRecipients(models.Model):
    name=models.CharField(max_field=30)
    email=models.EmailField()
        
    