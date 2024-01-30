
from django.http import HttpResponse, request
from django.shortcuts import render

data = {'movies': ['MADAR','CHOR1']}

def movies(request):
    return render(request, "hello.html", data )

def home(request):
    return HttpResponse("Homepage")
