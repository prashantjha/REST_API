from rest_framework import serializers
from rstApi.models import VideoData
from django.contrib.auth.models import User

class VideoSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = VideoData
		fields=('url','name','popularity','director','genere','imdb_score','owner')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    

    class Meta:
        model = User
        fields = ('id', 'username','email')