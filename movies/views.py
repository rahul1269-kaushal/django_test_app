
from django.http import HttpResponse, request
from django.shortcuts import render


def movies(request):
    return HttpResponse("Hello World")

def home(request):
    return HttpResponse("Homepage")
