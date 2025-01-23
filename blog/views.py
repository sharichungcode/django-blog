from django.shortcuts import render
from django.http import HttpResponse

def my_blog(request):
    return HttpResponse("Hello, Blog!")

def home(request):
    return HttpResponse("Welcome to the homepage!")