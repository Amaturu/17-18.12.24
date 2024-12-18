from django.contrib.auth.models import User
from rest_framework import serializers
from movies.models import Movie

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Movie
        fields = ['url', 'id', 'owner', 'title', 'description', 'release_date', 'rating'] 

class UserSerializer(serializers.HyperlinkedModelSerializer):
    movies = serializers.HyperlinkedRelatedField(many=True, view_name='movie-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'movies']