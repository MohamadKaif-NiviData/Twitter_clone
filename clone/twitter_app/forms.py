
from pyexpat import model
 
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