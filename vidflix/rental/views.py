from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("We in the houuuuuuse!")

def catalog(request):
    return render(request, 'catalog.html')

def about(request):
    return HttpResponse("More About VidFlix!")