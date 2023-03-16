
from logging import PlaceHolder
from pyexpat import model
from statistics import mode


from django.forms import ModelForm, fields, widgets
from twitter_app.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class UserRegisterForm(UserCreationForm):

    
  class Meta:
      model = User
      fields = ['username','first_name','last_name','img','email','password1','password2']

class UserEditForm(UserChangeForm):

        model=User
        fields=['username','first_name','last_name','img','email']

class user_model(ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']

# class tweet_modelform(ModelForm):
#     class Meta:
#         model=Tuser_tweets
#         fields='__all__'