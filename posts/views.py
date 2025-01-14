from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(requset):
    return HttpResponse("Hello world!")

def authorization(requset):
    return HttpResponse("<h1>Authorization</h1>")
