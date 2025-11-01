from django.contrib import admin
from django.urls import path
from homeapp import views


urlpatterns = [
    path('',views.home,name='home'),
    path('/about',views.about,name='about'),
]


