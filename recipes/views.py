from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'recipes/home.html')  # Render the home.html template

def contato(request):
    return HttpResponse("<h1>Contact Us</h1>")

def sobre(request):
    return HttpResponse("<h1>About Us</h1>")    