from django.contrib import admin
from django.urls import path,include
from twitter_app import views

from django.urls import path
from twitter_app.views import UserRegister,ProfileTemplateView,followdoneview

urlpatterns = [
    path('',views.home,name='home'),
    path('register',UserRegister.as_view(),name='register'),
    
    # path('login',UserLogin.as_view(),name='login'),
    path('userhome',views.userhome,name='userhome'),
    path('profile/',views.ProfileTemplateView.as_view(),name='profile'),
    path('userhomeside',views.userhomeside,name='userhomeside'),
    path('userprofile<pk>',views.userprofile,name='userprofile'),
    path('registration/login',views.ProfileTemplateView.as_view(),name='registration/login'),
    path('userdyanmicprofile<pk>',views.userdyanmicprofile,name='userdyanmicprofile'),
    path('followUser<str:uname>',views.followUser,name='followUser'),
    path('followdone',views.followdoneview.as_view(),name='followdoneview'),
    

]
