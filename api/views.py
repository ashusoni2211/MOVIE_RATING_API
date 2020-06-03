from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.decorators import action
from .models import Movie,Rating
from rest_framework import response
from .serializers import MovieSerializers,RatingSerializers,UserSerializers 
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    autherntication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    @action(detail=True,methods=['POST'])
    def rate_movie(self,request,pk=None):
        if 'stars' in request.data:
            movie = Movie.object.get(id=pk)
            stars = request.data['stars']
            user = request.user
            try:
                rating = Rating.objects.get(user=user.id,movie=movie.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializers(rating,many=False)
                responses = {'message':'rating updated','result':serializer.data}
                return response(responses,status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(user=user , movie=movie , stars=stars)
                serializer = RatingSerializers(rating,many=False)
                responses = {'message':'rating Created','result':serializer.data}
                return response(responses,status=status.HTTP_200_OK)
        else:
            responses = {'message':'u need to provide stars'}
            return response(responses,status=status.HTTP_404_NOT_FOUND)

        
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers
    autherntication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def update(self,request,*args,**kwargs):
            responses = {'message':'u cant update rating like that'}
            return response(responses,status=status.HTTP_404_NOT_FOUND)
    def create(self,request,*args,**kwargs):
        responses = {'message':'u cant create rating like that'}
        return response(responses,status=status.HTTP_404_NOT_FOUND)