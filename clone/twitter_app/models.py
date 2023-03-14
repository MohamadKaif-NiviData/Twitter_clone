
from django.db import models

from django.contrib.auth.models import AbstractUser

from crum import get_current_user 
from twitter_app.manager import CustomeManagers
# Create your models here.

class User(AbstractUser):
    img=models.ImageField()
    email=models.EmailField(unique=True)

    Dob=models.DateField(null=True)
 
    objects= CustomeManagers()


class Follow(models.Model):
    pass
    # user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='follow_follower',editable=False)
    # follow=models.ForeignKey(User,on_delete=models.CASCADE,related_name='follow_following')
    # follow_on=models.DateTimeField(auto_now_add=True)
    # def save(self,*args,**kwargs):
        
    #     user = get_current_user()
    #     if user and not user.pk:
    #         user = None
    #     if not self.pk:
    #         self.user = user
    #     super(Follow,self).save(*args,**kwargs)
    # @property   
    # def followerse_count(self):
    #     count=10
    #     return count




  



# Create your models here.

