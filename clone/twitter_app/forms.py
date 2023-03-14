
from pyexpat import model


from django.forms import ModelForm, fields, widgets
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):

    
  class Meta:
      model = User
      fields = ['username','first_name','last_name', 'email','password1','password2']



class user_model(ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']

# class tweet_modelform(ModelForm):
#     class Meta:
#         model=Tuser_tweets
#         fields='__all__'