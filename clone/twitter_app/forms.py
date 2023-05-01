

from pyexpat import model
from statistics import mode
from typing_extensions import Required
from django import forms
from django.forms import ModelForm, fields, widgets
from twitter_app.models import User,Tweet
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class UserRegisterForm(UserCreationForm):

  class Meta:
      model = User
      fields = ['username','first_name','last_name','email','password1','password2']
      widgets={forms.CharField()}
class UserEditForm(UserChangeForm):

        model=User
        fields=['username','first_name','last_name','img','email']

class user_model(ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
class UserTweetForm(forms.ModelForm):
    class Meta:
        model=Tweet
        fields=['post','img']
        widgets={'post':forms.Textarea(attrs={'class':'form-control','placeholder':'Whats happening?','id':'txtpost','class':'text','autocomplete':'off'})}
       
      
# class tweet_modelform(ModelForm):
#     class Meta:
#         model=Tuser_tweets
#         fields='__all__'