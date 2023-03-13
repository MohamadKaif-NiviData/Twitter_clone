from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Follow(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='follow_follower')
    follow=models.ForeignKey(User,on_delete=models.CASCADE,related_name='follow_following')
    follow_on=models.DateTimeField(auto_now_add=True)




  



# Create your models here.

