from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=32,blank=False)
    description = models.TextField(max_length=256,blank=True)


    def no_of_ratings(self):
        rating = Rating.object.filter(movie=self)
        return len(rating)

    def average_rating(self):
        rating = Rating.object.filter(movie=self)
        sum = 0
        for rate in rating:
            sum+=rate.stars
        if len(rating) > 0:
            return sum/len(rating)
        else:
            return 0

    def __str__(self):
        return self.title

class Rating(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    class Meta:
        unique_together = (('user','movie'),)
        index_together = (('user','movie'),)

