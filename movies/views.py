
from django.http import HttpResponse, request
from django.shortcuts import render
from .models import Movies

data =  Movies.objects.all()
def movies(request):
    return render(request, "hello.html", {'movies' : data})

def home(request):
    return HttpResponse("Homepage")
