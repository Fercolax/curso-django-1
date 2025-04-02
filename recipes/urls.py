from django.urls import path
from recipes import views


urlpatterns = [
    path('', views.home, name='home'),  # URL for the home page
    path('contato/', views.contato, name='contato'),  # URL for the contact page
    path('sobre/', views.sobre, name='sobre'),  # URL for the about page
]
