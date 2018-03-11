from django.conf.urls import url,include
from .views import CreateApiView,ViewReviews


urlpatterns = [
    url(r'CreateApiView$',CreateApiView.as_view(),name='ReviewsCreateApiView'),
    url(r'ViewReviews/(?P<place_id>.*)/$',ViewReviews.as_view(),name='ViewReviews'),
    # url(r'ViewOverallRatings/$',OverallRatings.as_view() , name = 'TotalRatingsListApiView'),
]
