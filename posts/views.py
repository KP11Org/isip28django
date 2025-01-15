from django.shortcuts import render
from django.http import HttpResponse
from posts.models import *
# Create your views here.
def index(requset):
    posts = Post.objects.all()
    return render(requset, "posts/index.html", {'posts':posts, 'title':"Hello isip28!"})

def authorization(requset):
    return HttpResponse("<h1>Authorization</h1>")
