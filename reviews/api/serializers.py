from rest_framework import serializers
from reviews.models import UserReviews


class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReviews
        fields = ('place_id','username','reviews')
