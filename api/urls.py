from django.urls import path
from django.conf.urls import include
from.import views
from rest_framework import routers
from .views import MovieViewSet,RatingViewSet,UserViewSet


router = routers.DefaultRouter()
router.register('movie',MovieViewSet)
router.register('rating',RatingViewSet)
router.register('users',UserViewSet)
urlpatterns = [
    path('',include(router.urls)),
]
