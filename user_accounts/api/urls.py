from django.conf.urls import url,include
from .views import  (
                    ListApiView,
                    RetrieveApiView,
                    CreateApiView,
                    UpdateApiView,
                    DestroyApiView,
)

urlpatterns = [
    url(r'^ListApiView/$',ListApiView.as_view(),name = 'UserListApiView'),
    url(r'^RetrieveApiView/(?P<username>[\w.@+-]+)/$',RetrieveApiView.as_view(),name = 'UserRetrieveApiView'),
    url(r'^CreateApiView/$',CreateApiView.as_view(),name = 'UserCreateApiView'),
    url(r'^UpdateApiView/(?P<username>[\w.@+-]+)/$',UpdateApiView.as_view(),name = 'UserUpdateApiView'),
    url(r'^DestroyApiView/(?P<username>[\w.@+-]+)/$',DestroyApiView.as_view(),name = 'UserDestroyApiView'),

]
