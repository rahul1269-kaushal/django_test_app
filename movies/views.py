
from django.http import HttpResponse, request
from django.shortcuts import render
from .models import Movies


def movies(request):
    data =  Movies.objects.all()
    return render(request, "hello.html", {'movies' : data})

def home(request):
    return HttpResponse("Homepage")

def detail(request, id):
    data = Movies.objects.get(pk=id)
    # pk is primary key
    return render(request, 'detail.html', {'movies' : data})
