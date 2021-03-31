from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.Translator2, name='home'),
    path("About", views.About, name='About'),
    
]