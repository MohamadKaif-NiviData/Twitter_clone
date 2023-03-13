
from pyexpat import model


from django.forms import ModelForm, fields, widgets
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
  first_name=forms.CharField(max_length=30,required=True)
  last_name=forms.CharField(max_length=30,required=True)
  email=forms.EmailField(max_length=300,required=True)
   
  class Meta:
      model = User
      fields = ['username', 'email', 'first_name','last_name','password1','password2']


 
from django.forms import ModelForm, fields, widgets
from django.contrib.auth.models import User

class user_model(ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']

# class tweet_modelform(ModelForm):
#     class Meta:
#         model=Tuser_tweets
#         fields='__all__'