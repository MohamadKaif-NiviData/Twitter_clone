from django.contrib import admin
from django.urls import path,include
from twitter_app import views
from django.urls import path
from twitter_app.views import UserRegister,ProfileTemplateView

urlpatterns = [
    path('',views.home),
    path('register',UserRegister.as_view(),name='register'),
    path('base1',views.home,name='base1'),
    # path('login',UserLogin.as_view(),name='login'),
    path('userhome',views.userhome,name='userhome'),
    path('profile/',views.ProfileTemplateView.as_view(),name='profile'),
    path('userhomeside',views.userhomeside,name='userhomeside'),
    path('userprofile<pk>',views.userprofile,name='userprofile'),
    path('registration/login',views.ProfileTemplateView.as_view(),name='registration/login'),
    path('userdyanmicprofile<pk>',views.userdyanmicprofile,name='userdyanmicprofile'),
    path('followToggle<pk>' , views.followToggle,name='followToggle'),
]
