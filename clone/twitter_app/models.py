from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class userfollow(models.Model):
    user = models.ManyToManyField(User,null=False)
    following = models.CharField(max_length=100)
    followerse = models.CharField(max_length=100)
    
