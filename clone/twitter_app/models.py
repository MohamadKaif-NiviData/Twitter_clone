

from email.policy import default
from django.db import models

from django.contrib.auth.models import AbstractUser

from crum import get_current_user 
from twitter_app.manager import CustomeManagers
# Create your models here.

class User(AbstractUser):
    img=models.ImageField(default='user.png')
    email=models.EmailField(unique=True)

    objects= CustomeManagers()
    
    @property   
    def followerse_count(self):
        count=self.follow_followed.count()
        return count 

    @property   
    def followeing_count(self):
        count=self.follow_follower.count()
        return count
    @property
    def tweet_count(self):
        count=self.user_tweet.count()
        return count      

class Follow(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='follow_follower',editable=False,null=True)
    follow=models.ForeignKey(User,on_delete=models.CASCADE,related_name='follow_followed',null=True)
    follow_on=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.user)

    def save(self,*args,**kwargs): 
        user = get_current_user()
        
        if not self.pk:
            self.user = user
        super(Follow,self).save(*args,**kwargs)
   
class Tweet(models.Model):
    user = models.ForeignKey(User,related_name='user_tweet',on_delete=models.CASCADE,editable=False)
    post = models.CharField(max_length=200,null=True,blank=True)
    img=models.ImageField( null=True,blank=True)
    created_by = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(User,default=None,blank=True,related_name='liked_user')
    retweet = models.ManyToManyField(User,default=None,blank=True,related_name='retweet_user')
    def save(self,*args,**kwargs): 
        user = get_current_user()
        
        if not self.pk:
            self.user = user
        super(Tweet,self).save(*args,**kwargs)
    @property
    def count_like(self):
        count=self.liked.count()
        return count 
    @property
    def count_retweet(self):
        count = self.retweet.count()
        return count
LIKE_CHOICES = (
        ('Like','Like'),
        ('Unlike','Unlike')
    )
class Like(models.Model):  
    tweet = models.ForeignKey(Tweet,on_delete=models.CASCADE,related_name='user_tweet')
    user = models.ForeignKey(User,on_delete=models.CASCADE,editable=False,related_name='user_like')
    value = models.CharField(choices=LIKE_CHOICES,default='Like',max_length=10)
   
    def save(self,*args,**kwargs): 
        user = get_current_user()
        
        if not self.pk:
            self.user = user
        super(Like,self).save(*args,**kwargs)

LIKE_CHOICES = (
        ('ReTweet','ReTweet'),
        ('Remove','Remove')
    )
class ReTweet(models.Model):
    tweet = models.ForeignKey(Tweet,on_delete=models.CASCADE,related_name='user_retweet')
    user = models.ForeignKey(User,on_delete=models.CASCADE,editable=False,related_name='user_retweet')
    value = models.CharField(choices=LIKE_CHOICES,default='ReTweet',max_length=20)
    def save(self,*args,**kwargs): 
        user = get_current_user()
        
        if not self.pk:
            self.user = user
        super(ReTweet,self).save(*args,**kwargs)
# Create your models here.

