from rest_framework import serializers
from ratings.models import UserRatings,TotalRatings
from django.core.exceptions import ObjectDoesNotExist


class UserRatingsCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRatings
        fields = ('place_id','username','ratings','hygiene_ratings','cleanliness_ratings')

    def create(self,validated_data):
        place_id = validated_data['place_id']
        username = validated_data['username']
        ratings = validated_data['ratings']
        hygiene_ratings = validated_data['hygiene_ratings']
        cleanliness_ratings = validated_data['cleanliness_ratings']
        try:
            r = UserRatings.objects.get(place_id = place_id , username = username)
            r.ratings = ratings
            r.hygiene_ratings = hygiene_ratings
            r.cleanliness_ratings = cleanliness_ratings
            r.save()
        except ObjectDoesNotExist:
            r = UserRatings.objects.create(
                place_id = place_id,
                username = username,
                ratings = ratings,
                hygiene_ratings = hygiene_ratings,
                cleanliness_ratings =cleanliness_ratings,
            )
        objects = UserRatings.objects.filter(place_id = place_id)
        ratings_sum = 0
        count = 0
        for obj in objects:
            ratings_sum += float(obj.ratings)
            count+=1
        avg_rating = ratings_sum/count
        print avg_rating
        try:
            t = TotalRatings.objects.get(place_id = place_id)
            t.ratings = avg_rating
            t.save()
        except ObjectDoesNotExist:
            t = TotalRatings.objects.create(
                place_id = place_id,
                ratings = avg_rating,
            )
        return r


class TotalRatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalRatings
        fields = ('place_id','ratings')
