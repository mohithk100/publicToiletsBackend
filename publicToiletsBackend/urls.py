from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^user/',include('user_accounts.urls')),
    url(r'^ratings/',include('ratings.urls')),
    url(r'^toilets/',include('toilets.urls')),
    url(r'^reviews/',include('reviews.urls')),
    url(r'^add-delete/',include('add_delete.urls')),
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
