from rest_framework import serializers

class ToiletSerializer(serializers.Serializer):
    place_id = serializers.CharField(max_length = 5000)
    name = serializers.CharField(max_length = 5000)
    rating = serializers.FloatField(max_value = None , min_value = None , default = 0)
    formatted_address = serializers.CharField(max_length = 5000)
