from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User
# Create your models here.
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> add files
class Fllow(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='follow_follower')
    follow=models.ForeignKey(User,on_delete=models.CASCADE,related_name='follow_following')
    follow_on=models.DateTimeField(auto_now_add=True)



<<<<<<< HEAD
  
=======
class userfollow(models.Model):
    user = models.ManyToManyField(User,null=False)
    following = models.CharField(max_length=100)
    followerse = models.CharField(max_length=100)
    
>>>>>>> add files
=======
  
>>>>>>> add files
=======

# Create your models here.
>>>>>>> 5fe2e037ebe96b1172fa37018724f811d383728c
