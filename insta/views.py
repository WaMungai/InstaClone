from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .forms import NewsLetterForm,NewImageForm,NewProfileForm,NewCommentForm,UpdateProfileForm
from .models import Image,Profile,NewsLetterRecipients,Comments
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

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
    if request.method =='POST':
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

@login_required(login_url='/accounts/login')
def new_image(request):
    current_user =request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.editor=current_user
            image.save()
            return redirect('welcome')
        else:
            form =NewImageForm()
            return render(request,'new_image.html',{"form":form}) 
        
@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method =='POST':
        form = NewProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile =form.save(commit=False)
            profile.editor =current_user
            profile.save()
            return redirect('welcome')
    else:
        form =NewProfileForm()
    return render(request,'new_profile.html',{"form":form})  

@login_required(login_url='/accounts/login/')
def update_profile(request):
    if request.method =='POST':
        profileform=UpdateProfile(request.POST,request.FILES,instance=request.user)
        if profileform.is_valid():
            profileform.save()
        return redirect('welcome')
    else:
        profileform=UpdateProfileForm(instance=request.user)
    context={
        'profileform':profileform,
    }
    return render(request,'updateprofile.html',context)

@login_required(login_url='/accounts/login/')
def display_profile(request,user_id):
    try:
        single_profile=Profile.single_profile(user_id)
        image_posted=Image.user_images(user_id)
        return render(request,'profiledisplay.html',{"profile":single_profile,"image":image_posted})
    except Profile.DoesNotExist:
        messages.info(request,'The user has not yet a profile yet')
        return redirect('welcome')

def makecomment(request):
    current_user =request.user
    if request. moethod == 'POST':
        form =NewCommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.editor =current_user
            comment.save()
        return redirect('welcome')
    else:
        form=NewCommentForm()
    return render(request,'comment.html',{"form":form})

def like_a_post(request):
    post = get_object_or_404(Image,id=request.POST.get(post_id))
    post.likes.add(request.user)
    post.likes.add(request.user)
    return redrect('welcome')

def follow(request):
    post = get_object_or_404(Image,id=request.POST.get('post_id'))
    post.followers.add(request.user)
    return redirect('welcome')

def delete_post(request,post_id=None):
    post_to_delete=get_object_or_404(Image,id=('post_id'))
    post.likes.add(request.user)
    return redirect('welcome')