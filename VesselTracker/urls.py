from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('VesselAPIs.urls')),
    path('admin/', admin.site.urls),
]
