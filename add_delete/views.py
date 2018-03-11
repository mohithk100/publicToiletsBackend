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
class deletePlace(views.APIView):
    def get(request,*args,**kwargs):
        place_id = kwargs['place_id']
        auth_key = "AIzaSyBT2bthEFpaHd6zDOkhfpXrnI7eICYbv74"
        request_url = "https://maps.googleapis.com/maps/api/place/delete/json?key="+auth_key+"&place_id="+place_id
        print request_url
        response = requests.get(request_url).json()
        response_dict = json.loads(json.dumps(response))
        return Response(response_dict)
