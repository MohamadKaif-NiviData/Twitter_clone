
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
    
    @property   
    def followerse_count(self):
        count=self.follow_followed.count()
        return count 

    @property   
    def followeing_count(self):
        count=self.follow_follower.count()
        return count
          


class Follow(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='follow_follower',editable=False,null=True)
    follow=models.ForeignKey(User,on_delete=models.CASCADE,related_name='follow_followed',null=True)
    follow_on=models.DateTimeField(auto_now_add=True,null=True)
    def save(self,*args,**kwargs): 
        user = get_current_user()
        
        if not self.pk:
            self.user = user
        super(Follow,self).save(*args,**kwargs)
   



  



# Create your models here.

