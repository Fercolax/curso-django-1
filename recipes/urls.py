from django.urls import path
from recipes import views


urlpatterns = [
    path('', views.home,),  # URL for the home page
  
]
