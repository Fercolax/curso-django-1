from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'recipes/home.html')  # Render the home.html template

