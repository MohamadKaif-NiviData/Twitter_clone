
from django.contrib import admin

from .models import Follow,User,tweet
# Register your models here.
class FollowAdmin(admin.ModelAdmin):
    model=Follow
    list_display=('user','follow')
admin.site.register(Follow,FollowAdmin)
admin.site.register(User)
admin.site.register(tweet)



