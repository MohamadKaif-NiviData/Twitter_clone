
from django.contrib import admin
from django.urls import path,include
from . import views

from django.conf.urls.i18n import i18n_patterns 
from django.utils.translation import gettext_lazy as _
from django.urls import path
from twitter_app.views import UserRegister,ProfileTemplateView,FollowDoneView,UserEdit,user_home



urlpatterns = [
    path('',views.home,name='home'),
    path('userregister',views.UserRegister.as_view(),name='register'),
    path('userhome',views.user_home.as_view(),name='userhome'),
    
    path('userhomeside',views.user_home_side,name='userhomeside'),
    path('userprofile<pk>',views.user_profile,name='userprofile'),
    path('templates/login',views.ProfileTemplateView.as_view(),name='templates/login'),
    path('follow/done',views.FollowDoneView.as_view(),name='follow_done_view'),
    path('unfollow/done',views.UnfollowDoneView.as_view(),name='unfollow_done_view'),
    path('useredit<pk>',views.UserEdit.as_view(),name='useredit'),
    path('user_converte_csv<pk>',views.user_converte_csv,name='user_converte_csv'),
    path('user_converte_pdf',views.user_converte_pdf,name='user_converte_pdf'),
    path('user/<str:username>',views.user_profile_name,name='userprofile<uname>'),
    path('usertweet',views.UserTweet,name='usertweet'),
    path('post_create_view',views.post_create_view.as_view(),name='post_create_view'),
    path('post_like_view',views.post_like_view,name='post_like_view'),
    path('user_retweet',views.user_retweet,name='user_retweet'),
    path('set_lenguage',views.set_lenguage,name='set_lenguage'),
    path('Delete_post',views.Delete_post,name='Delete_post'),
    path('logout_user',views.logout_user,name='logout_user'),
    path('Like',views.LikeAPIs.as_view(),name='Like'),

    path('Retweet',views.ReTweetAPI.as_view(),name='Retweet'),

    path('Delete/<int:id>',views.DeletePost.as_view(),name='Delete'),
    path('Tweet',views.TweetCreate.as_view(),name='Tweet'),

]


