from django.shortcuts import render

#create your views here

from django.http import HttpResponse

def index(request): 
    return HttpResponse("Hello, world. You're at the polls index.")
