from django.conf.urls import url,include
from .views import deletePlace

urlpatterns = [
    url(r'^delete/(?P<place_id>.*)/$' , deletePlace.as_view() , name = "DeletePlace"),
]
