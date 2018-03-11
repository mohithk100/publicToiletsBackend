from __future__ import unicode_literals
from django.db import models

class UserRatings(models.Model):
    place_id = models.CharField(max_length = 500)
    username = models.CharField(max_length = 100)
    ratings= models.CharField(max_length = 10)
    hygiene_ratings = models.CharField(max_length = 10 , null = True)
    cleanliness_ratings = models.CharField(max_length = 10 ,null = True )


class TotalRatings(models.Model):
    place_id = models.CharField(max_length = 500)
    ratings= models.CharField(max_length = 10)
