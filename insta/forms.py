from django import forms
from .models import Image,Profile,Comments

class NewsLetterForm(forms.Form):
    your_name=forms.CharField(label='First Name',max_length=30)
    email=forms.EmailField(label='Email')