from django.db import models
from django.contrib.auth.models import User
# Create your models here.
<<<<<<< HEAD
class Fllow(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='follow_follower')
    follow=models.ForeignKey(User,on_delete=models.CASCADE,related_name='follow_following')
    follow_on=models.DateTimeField(auto_now_add=True)



  
=======
class userfollow(models.Model):
    user = models.ManyToManyField(User,null=False)
    following = models.CharField(max_length=100)
    followerse = models.CharField(max_length=100)
    
>>>>>>> add files
