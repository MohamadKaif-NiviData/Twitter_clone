from django.contrib import admin
from django.urls import path,include
from twitter_app import views

urlpatterns = [
    path('',views.home),
    path('register',views.register,name='register'),
    path('base',views.home,name='base'),
    path('login',views.Ulogin,name='login'),
    path('userhome',views.userhome,name='userhome'),
    path('userprofile',views.userprofile,name='userprofile'),
    path('userhomeside',views.userhomeside,name='userhomeside'),
]
