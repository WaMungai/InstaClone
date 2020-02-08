from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def search_category(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term=request.GET.get("category")
        searched_categories=Image.search_by_category(search_term)
        message=f"{search_term}"
        return render(request,"search.html",{"message":message,"categories":searched_categories})
    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})

# def single_photo(request,photo_id):
    