from .models import Like,Tweet,ReTweet
from rest_framework  import  serializers

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields =['tweet','user','value']
class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['user','post','img']
class ReTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReTweet
        fields = ['tweet','user','value']


