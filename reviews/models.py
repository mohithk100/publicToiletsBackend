from __future__ import unicode_literals
from django.db import models

class UserReviews(models.Model):
    place_id = models.CharField(max_length = 500)
    username = models.CharField(max_length = 100)
    reviews= models.CharField(max_length = 280)
