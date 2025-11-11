from django.contrib import admin
from django.urls import path
from myapp import views
from django.shortcuts import render

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), 
    path('index/',views.index,name="index"),
    path('contact/',views.contact_us,name="contact"),
    path('about/',views.about,name="about"),
     path('team/', views.team, name="team"),
       path('menu/', views.menu, name='menu'),
    path('booking/', views.booking, name='booking'),
    path('feature/', views.feature, name='feature'),
    path('booking/', views.booking, name='booking'),
    path('all_dishes/', views.all_dishes, name='all_dishes'),

   
]