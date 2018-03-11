from django.conf.urls import url,include
from .views import CreateApiView,ViewUserRatings,OverallRatings


urlpatterns = [
    url(r'CreateApiView$',CreateApiView.as_view(),name='RatingsCreateApiView'),
    url(r'ViewUserRatings/(?P<username>[\w.@+-]+)/$',ViewUserRatings.as_view(),name='RatingsViewUserRatings'),
    url(r'ViewOverallRatings/$',OverallRatings.as_view() , name = 'TotalRatingsListApiView'),
]
