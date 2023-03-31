
from django.contrib import admin

from .models import Follow,User,Tweet,Like,ReTweet
# Register your models here.
class FollowAdmin(admin.ModelAdmin):
    model=Follow
    list_display=('user','follow')
admin.site.register(Follow,FollowAdmin)
admin.site.register(User)

class UserTweet(admin.ModelAdmin):
    model=Tweet
    list_display=('user','post','img')

admin.site.register(Tweet,UserTweet)

class LikeAdmin(admin.ModelAdmin):
    model=Like
    list_display=('user','tweet')
admin.site.register(Like,LikeAdmin)

class UserReTweet(admin.ModelAdmin):
    model=ReTweet
    list_display=('user','tweet','value')
admin.site.register(ReTweet,UserReTweet)






