from django.conf.urls import url,include

urlpatterns = [
    url(r'^api/',include('user_accounts.api.urls')),
]
