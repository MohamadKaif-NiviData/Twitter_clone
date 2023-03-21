
from django.contrib import admin
from django.urls import path,include
from twitter_app import views

from django.urls import path
from twitter_app.views import UserRegister,ProfileTemplateView,FollowDoneView,UserEdit

urlpatterns = [
    path('',views.home,name='home'),
    path('userregister',views.UserRegister.as_view(),name='register'),
    path('userhome',views.user_home,name='userhome'),
    path('userhomeside',views.user_home_side,name='userhomeside'),
    path('userprofile<pk>',views.user_profile,name='userprofile'),
    path('templates/login',views.ProfileTemplateView.as_view(),name='templates/login'),
    path('follow/done',views.FollowDoneView.as_view(),name='follow_done_view'),
    path('unfollow/done',views.UnfollowDoneView.as_view(),name='unfollow_done_view'),
    path('useredit<pk>',views.UserEdit.as_view(),name='useredit'),
    path('user_converte_csv<pk>',views.user_converte_csv,name='user_converte_csv'),
    path('user_converte_pdf',views.user_converte_pdf,name='user_converte_pdf'),
    # path('<str:username>',views.user_profile_name,name='userprofile<uname>')
]
