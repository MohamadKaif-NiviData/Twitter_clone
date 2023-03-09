from django.contrib import admin
from django.urls import path,include
from twitter_app import views
from django.urls import path
from twitter_app.views import UserRegister,UserLogin

urlpatterns = [
    path('',views.home),
    path('register',UserRegister.as_view(),name='register'),
    path('base1',views.home,name='base1'),
    path('login',UserLogin.as_view(),name='login'),
    path('userhome',views.userhome,name='userhome'),
    path('userprofile',views.userprofile,name='userprofile'),
    path('userhomeside',views.userhomeside,name='userhomeside'),
    
]
