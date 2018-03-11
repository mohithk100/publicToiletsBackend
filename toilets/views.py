from django.shortcuts import render
from toilets.api.serializers import ToiletSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import views
import urllib2
import requests
import json
from django.http.response import HttpResponse





@permission_classes((permissions.IsAuthenticated,))
class get_toilets(views.APIView):
    def get(request,*args,**kwargs):
        latitude = kwargs['latitude']
        longitude = kwargs['longitude']
        auth_key = "AIzaSyApVUbn52tg-jZx-l-WqncGbf-OPfnmj6U"
        query = "Public Toilets"
        request_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"+"key="+auth_key+"&query="+query+"&location="+str(latitude)+","+str(longitude)+"&radius=1000"
        response = requests.get(request_url).json()
        response_dict = json.loads(json.dumps(response))
        list_of_keys = response_dict.keys()
        if 'next_page_token' in list_of_keys:
            next_page_token = response_dict['next_page_token']
        queryset = response_dict['results']
        results = ToiletSerializer(queryset, many=True).data
        return Response({"array":results})
