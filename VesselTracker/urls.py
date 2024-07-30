from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import handler404
from user.views import custom_404
handler404 = custom_404
urlpatterns = [
    path('api/v1/', include('VesselAPIs.urls')),
    path('', include('user.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
