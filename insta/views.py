from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .forms import NewsLetterForm
from .models import Image,Profile,NewsLetterRecipients,Comments
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

# Create your views here.
def welcome(request):
    if request.method == 'POST':
        form=NewsLetterForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['your_name']
            email=form.cleaned_data['email']
            recipient=NewsLetterRecipients(name=name,email=email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResposeRedirect('welcome')
            print('valid')
    else:
        form=NewsLetterForm()
    return render(request,'welcome.html',{"letterForm":form})

def search_category(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term=request.GET.get("category")
        searched_categories=Image.search_by_category(search_term)
        message=f"{search_term}"
        return render(request,"search.html",{"message":message,"categories":searched_categories})
    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})

@login_required(login_url='accounts/login/')
def single_photo(request,photo_id):
    if request.method='POST':
        form=NewCommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.editor=request.user
            post=Image.objects.get(id=photo_id)
            comment.image_foreign=post
            comment.save()
            HttpResponseRedirect('single_photo')
    else:
        form=NewCommentForm()
    image_posted=Image.single_image(photo_id)
    imageId=Image.get_image_id(photo_id)
    comments=Comments.get_singlepost_comments(imageId)
    return render(request,'photo.html',{"form":form,"comments":comments,"photo":image_posted})
    