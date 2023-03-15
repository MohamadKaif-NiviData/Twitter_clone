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
    path('templates/login',views.ProfileTemplateView.as_view(),name='templates/login'),
    path('userdyanmicprofile<pk>',views.userdyanmicprofile,name='userdyanmicprofile'),
    path('followToggle<str:uname>',views.followToggle,name='followToggle'),
    path('follow/done',views.followdoneview.as_view(),name='follow_done_view'),
    path('unfollow/done',views.unfollow_done_view.as_view(),name='unfollow_done_view'),

    

]
