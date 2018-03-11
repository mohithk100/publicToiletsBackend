from django.conf.urls import url,include
from .views import get_toilets




urlpatterns = [
    url(r'location/(?P<latitude>[1-9]\d*(\.\d+)?)/(?P<longitude>[1-9]\d*(\.\d+)?)/$' , get_toilets.as_view() , name = 'get_toilets'),
]
