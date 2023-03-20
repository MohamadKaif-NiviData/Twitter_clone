
from django.contrib import admin
from django.urls import path,include
from twitter_app import views

from django.urls import path
from twitter_app.views import UserRegister,ProfileTemplateView,followdoneview,useredit

urlpatterns = [
    path('',views.home,name='home'),
    path('register',UserRegister.as_view(),name='register'),
    
    # path('login',UserLogin.as_view(),name='login'),
    path('userhome',views.userhome,name='userhome'),
    path('profile/',views.ProfileTemplateView.as_view(),name='profile'),
    path('userhomeside',views.userhomeside,name='userhomeside'),
    path('userprofile<pk>',views.userprofile,name='userprofile'),
    
    path('templates/login',views.ProfileTemplateView.as_view(),name='templates/login'),
   
    path('follow/done',views.followdoneview.as_view(),name='follow_done_view'),
    path('unfollow/done',views.unfollow_done_view.as_view(),name='unfollow_done_view'),
    path('useredit<pk>',views.useredit.as_view(),name='useredit'),
    path('user_converte_csv<pk>',views.user_converte_csv,name='user_converte_csv'),
    path('user_converte_pdf',views.user_converte_pdf,name='user_converte_pdf'),
    

    

]
