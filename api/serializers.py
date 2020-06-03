from rest_framework import serializers
from .models import Movie,Rating
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','password')
        extra_kwargs = {'password':{'write_only':True,'required':True}}
    def create(self, validated_data):
        user = User.objecta.create_user(**validated_data)
        token = Token.object.create(user=user)
        return user


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description','no_of_ratings','average_rating')

class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user' , 'movie')

